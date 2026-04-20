try:
    from langchain_community.document_loaders import PyPDFLoader
    print("PyPDFLoader imported")
    
    from langchain_openai import OpenAIEmbeddings, OpenAI
    print("OpenAI components imported")
    
    from langchain_text_splitters import RecursiveCharacterTextSplitter
    print("Text splitter imported")
    
    from langchain_community.vectorstores import Chroma
    print("Chroma imported")
    
    from langchain_core.prompts import PromptTemplate
    from langchain_core.runnables import RunnablePassthrough
    print("LCEL components imported")
    
    print("All imports successful!")
    
except Exception as e:
    print(f"Import error: {e}")
    import traceback
    traceback.print_exc()