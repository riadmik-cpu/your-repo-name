---
title: PDF QA Bot
emoji: 🤖
colorFrom: blue
colorTo: green
sdk: gradio
sdk_version: 6.12.0
app_file: app.py
pinned: false
license: mit
---

# PDF QA Bot

A powerful question-answering bot that can analyze PDF documents using OpenAI's GPT models and LangChain. Upload any PDF and ask questions about its content!

## Features

- 📄 **PDF Upload**: Support for PDF document uploads
- 🤖 **AI-Powered**: Uses OpenAI GPT-4o-mini for intelligent answers
- 🔍 **Context-Aware**: Retrieves relevant information from the document
- 🚀 **Fast**: Optimized for quick responses
- 🌐 **Web Interface**: User-friendly Gradio interface

## How to Use

1. **Upload a PDF**: Click the upload button and select your PDF file
2. **Ask a Question**: Type your question in the text box
3. **Get Answer**: The bot will analyze the document and provide a detailed answer

## Examples

- "What is the main topic of this document?"
- "Summarize the key findings"
- "Explain the methodology used"
- "What are the conclusions?"

## Technical Details

- **Backend**: Python with LangChain and OpenAI
- **Frontend**: Gradio web interface
- **Embeddings**: OpenAI text-embedding-3-large
- **LLM**: OpenAI GPT-4o-mini
- **Vector Store**: ChromaDB for document retrieval

## Privacy

Your uploaded PDFs are processed temporarily and not stored permanently. The analysis happens in real-time using OpenAI's API.