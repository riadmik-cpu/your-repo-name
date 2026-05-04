# PDF QA Bot Web App

This project builds a question-answering web app using LangChain, IBM Watsonx embeddings, Chroma, and Gradio.

## What it does

- Loads PDF documents using `PyPDFLoader`
- Splits PDF text into chunks with `RecursiveCharacterTextSplitter`
- Generates embeddings with IBM Watsonx using `WatsonxEmbeddings`
- Stores embeddings in a Chroma vector database
- Uses a retriever with `RetrievalQA` to answer user questions
- Serves the app with a Gradio interface

## Setup

1. Create and activate a Python virtual environment (recommended):

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

2. Install dependencies:

```powershell
python -m pip install -r requirements.txt
```

> Important: This version of the app is configured for Python 3.14 and uses OpenAI for embeddings and LLM responses.

3. Set OpenAI environment variables:

```powershell
$env:OPENAI_API_KEY = "your_openai_api_key"
$env:OPENAI_EMBEDDING_MODEL = "text-embedding-3-large"
$env:OPENAI_LLM_MODEL = "gpt-4o-mini"
```

4. Run the app:

```powershell
python app.py
```

5. Open the local Gradio URL and upload a PDF.

## Screenshots to capture

- `pdf_loader.png` — completed `document_loader` implementation
- `code_splitter.png` — completed `text_splitter` implementation
- `embedding.png` — completed `watsonx_embedding` implementation
- `vectordb.png` — completed `vector_database` implementation
- `retriever.png` — completed `retriever` implementation
- `QA_bot.png` — Gradio interface with PDF loaded and query answered

## Notes

- The Gradio interface uses `gr.Interface` as requested.
- The app stores Chroma data in `qa_bot/chroma_db`.
- Change `WATSONX_EMBEDDING_MODEL` and `WATSONX_LLM_MODEL` in your environment if needed.
