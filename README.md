# LocalLedger AI

A private, offline-first invoice and receipt processor built with Python and Streamlit.

## Features
- **Local PDF Processing**: Reads and extracts text from invoices/receipts using PyMuPDF.
- **Privacy First**: Files never leave your local machine.
- **Streamlit Interface**: Clean, simple web UI for uploading documents and downloading parsed text.

## Setup & Running

1. **Clone the repository**:
   ```bash
   git clone <YOUR_REPO_URL>
   cd localledger-ai
   ```

2. **Create and activate a virtual environment**:
   ```bash
   python -m venv .venv
   # Windows:
   .venv\Scripts\activate
   # macOS/Linux:
   source .venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**:
   ```bash
   streamlit run app.py
   ```
   Open your browser at `http://localhost:8501`.
