import gradio as gr
import os

print("Starting PDF QA Bot...")
print(f"OpenAI API Key set: {bool(os.getenv('OPENAI_API_KEY'))}")

def test_function(file, query):
    return "Test answer", "Test sources"

interface = gr.Interface(
    fn=test_function,
    inputs=[
        gr.File(label="Upload PDF", file_count="single", type="filepath"),
        gr.Textbox(label="Question", placeholder="What is this paper about?"),
    ],
    outputs=[
        gr.Textbox(label="Answer"),
        gr.Textbox(label="Source documents"),
    ],
    title="PDF QA Bot",
    description="Upload a PDF document and ask questions using LangChain + OpenAI embeddings.",
)

print("Launching Gradio interface...")
interface.launch(share=False, server_name="127.0.0.1", server_port=7860)
print("Gradio interface launched!")