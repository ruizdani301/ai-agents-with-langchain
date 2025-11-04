import PyPDF2
from io import BytesIO

def extract_text_from_pdf(file_path):
    try:
        pdf_reader = PyPDF2.PdfReader(BytesIO(file_path.read()))
        text = ""
        for num_pag, page in enumerate(pdf_reader.pages, 1):
            pages_text = page.extract_text()
            if pages_text.strip():
                text += f"\n\n--- Page {num_pag} ---\n\n"
                text += pages_text + "\n"
        full_text = text.strip()
        if not full_text:
            return ValueError("No text found in PDF.")
        return full_text
    except Exception as e:
        return  ValueError(f"Error processing PDF: {e}")
