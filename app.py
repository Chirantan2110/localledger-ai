import streamlit as st
import fitz  # PyMuPDF

st.set_page_config(
    page_title="LocalLedger AI",
    page_icon="📄",
    layout="centered",
)

st.title("LocalLedger AI")
st.subheader("Your private invoice and receipt organizer")

st.write(
    "Upload an invoice or receipt PDF to extract its text. "
    "This first version processes files locally on your computer."
)

uploaded_file = st.file_uploader(
    "Choose a PDF invoice",
    type=["pdf"],
)

if uploaded_file is not None:
    try:
        pdf_bytes = uploaded_file.getvalue()

        with fitz.open(stream=pdf_bytes, filetype="pdf") as pdf:
            page_count = len(pdf)
            extracted_text = "\n\n".join(
                page.get_text() for page in pdf
            )

        st.success(f"PDF loaded successfully: {page_count} page(s)")

        if extracted_text.strip():
            st.subheader("Extracted text")
            st.text_area(
                "Review the text from your document",
                value=extracted_text,
                height=300,
            )

            st.download_button(
                label="Download extracted text",
                data=extracted_text,
                file_name="extracted_invoice.txt",
                mime="text/plain",
            )
        else:
            st.warning(
                "No selectable text was found. "
                "This PDF may be a scanned image. "
                "We'll add OCR support in a later step."
            )

    except Exception as error:
        st.error(
            "Could not read this PDF. "
            "Check that it is a valid, unencrypted PDF."
        )
        st.caption(f"Technical details: {error}")

st.divider()
st.caption("LocalLedger AI • Early development version")
