import os
import tempfile
from pathlib import Path
from typing import Optional, Tuple

import gradio as gr
from langchain_community.document_loaders import PyPDFLoader
from langchain_openai import OpenAIEmbeddings, OpenAI
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough

# Configuration
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200
EMBEDDING_MODEL = os.getenv("OPENAI_EMBEDDING_MODEL", "text-embedding-3-large")
LLM_MODEL = os.getenv("OPENAI_LLM_MODEL", "gpt-4o-mini")


def document_loader(file_path: str) -> PyPDFLoader:
    """Load a PDF document using LangChain's PDF loader."""
    return PyPDFLoader(file_path)


def text_splitter(documents: list, chunk_size: int = CHUNK_SIZE, chunk_overlap: int = CHUNK_OVERLAP):
    """Split loaded documents into smaller chunks for embedding."""
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        separators=["\n\n", "\n", " ", ""],
    )
    return splitter.split_documents(documents)


def openai_embedding() -> OpenAIEmbeddings:
    """Create an OpenAI embedding client for LangChain."""
    return OpenAIEmbeddings(model=EMBEDDING_MODEL)


def get_llm() -> OpenAI:
    """Create an OpenAI LLM instance for answer generation."""
    return OpenAI(model=LLM_MODEL, temperature=0)


def vector_database(documents: list, embedding: OpenAIEmbeddings, persist_directory: Optional[Path] = None) -> Chroma:
    """Create or reuse a Chroma vector store for embedded documents."""
    if persist_directory:
        persist_directory.mkdir(parents=True, exist_ok=True)
        return Chroma.from_documents(documents=documents, embedding=embedding, persist_directory=str(persist_directory))
    return Chroma.from_documents(documents=documents, embedding=embedding)


def retriever(file_path: str):
    """Load, split, embed, and return a retriever for a PDF."""
    loader = document_loader(file_path)
    documents = loader.load()
    chunks = text_splitter(documents)
    embedding = openai_embedding()
    # Use temporary directory for Chroma DB to avoid persistence issues on HF Spaces
    with tempfile.TemporaryDirectory() as temp_dir:
        store = vector_database(chunks, embedding, persist_directory=Path(temp_dir))
        return store.as_retriever(search_kwargs={"k": 4})


def retriever_qa(file_path: str, query: str) -> Tuple[str, str]:
    """Run retrieval-augmented question answering over the uploaded PDF."""
    # Create the retrieval chain using LCEL
    template = """Use the following pieces of context to answer the question at the end. If you don't know the answer, just say that you don't know, don't try to make up an answer.

{context}

Question: {question}
Answer:"""
    prompt = PromptTemplate.from_template(template)

    retriever_instance = retriever(file_path)
    llm_instance = get_llm()

    def format_docs(docs):
        return "\n\n".join(doc.page_content for doc in docs)

    chain = (
        {"context": retriever_instance | format_docs, "question": RunnablePassthrough()}
        | prompt
        | llm_instance
    )

    response = chain.invoke(query)
    answer = response.content if isinstance(response, str) is False and hasattr(response, 'content') else str(response) # type: ignore

    # Get source documents for sources
    docs = retriever_instance.get_relevant_documents(query) # type: ignore
    sources = "\n".join(
        {doc.metadata.get("source", "Unknown source") for doc in docs}
    )
    return answer, sources or "No sources available."


def answer_pdf(pdf_file, query: str) -> Tuple[str, str]:
    """Gradio callback for the PDF QA interface."""
    if not os.getenv("OPENAI_API_KEY"):
        return "Missing OPENAI_API_KEY. Please set it in the Space settings.", ""
    if not pdf_file:
        return "Please upload a PDF file.", ""
    if not query:
        return "Please enter a query.", ""

    # Save uploaded file temporarily
    with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as temp_file:
        temp_file.write(pdf_file)
        temp_path = temp_file.name

    try:
        return retriever_qa(temp_path, query)
    except Exception as error:
        return f"Error: {error}", ""
    finally:
        # Clean up temporary file
        if os.path.exists(temp_path):
            os.unlink(temp_path)


# Create the Gradio interface
interface = gr.Interface(
    fn=answer_pdf,
    inputs=[
        gr.File(label="Upload PDF", file_count="single", type="binary"),
        gr.Textbox(label="Question", placeholder="What is this paper about?"),
    ],
    outputs=[
        gr.Textbox(label="Answer"),
        gr.Textbox(label="Source documents"),
    ],
    title="PDF QA Bot",
    description="Upload a PDF document and ask questions using LangChain + OpenAI embeddings.",
    examples=[
        ["test_document.pdf", "What is artificial intelligence?"],
        ["test_document.pdf", "Explain the main concepts discussed"],
    ]
)

if __name__ == "__main__":
    interface.launch()