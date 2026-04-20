import time
import importlib

modules = [
    'gradio',
    'langchain_community.document_loaders',
    'langchain_openai',
    'langchain_text_splitters',
    'langchain_community.vectorstores',
    'langchain_core.prompts',
    'langchain_core.runnables',
]

for module in modules:
    print(f'Importing {module}...')
    start = time.time()
    try:
        importlib.import_module(module)
        print(f'  Success ({time.time() - start:.2f}s)')
    except Exception as e:
        print(f'  Failed: {e}')
        break
print('Done')
