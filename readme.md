# ResearchPal - Research Paper Q&A Bot

ResearchPal is a Streamlit-based AI assistant that allows you to upload research papers (PDFs) and ask questions about their content. The system uses **LangChain**, **FAISS**, and **Hugging Face models** to generate answers based purely on the uploaded document.

---

## Features

- Upload research papers in PDF format.
- Ask questions about the paper.
- Answers are generated **only from the uploaded document**.
- Provides structured summaries for broad questions.
- Step-by-step reasoning when needed.

---

## How It Works

1. **Document Loading:** PDFs are loaded and parsed using `PyPDFLoader`.
2. **Document Chunking:** Large documents are split into chunks for easier retrieval using `RecursiveCharacterTextSplitter`.
3. **Vector Store:** Chunks are converted to embeddings using `HuggingFaceEmbeddings` and stored in FAISS for semantic search.
4. **RAG Pipeline:** A Retriever-Augmented Generation chain fetches relevant document chunks and passes them to a Hugging Face LLM (Llama 3.3) to generate answers.
5. **Streamlit Frontend:** Users can upload papers and query the model directly from the web interface.

---

## Setup & Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/researchpal.git
cd researchpal

2. Create a virtual environment and activate it

python -m venv venv
source venv/bin/activate  # Linux / macOS
venv\Scripts\activate     # Windows

3. Install dependencies

pip install -r requirements.txt

4. Create a .env file in the root directory with your hugging face token

HUGGINGFACEHUB_API_TOKEN=your_huggingface_api_key

5. Run the app locally

streamlit run app.py

