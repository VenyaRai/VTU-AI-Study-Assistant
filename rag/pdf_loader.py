import pdfplumber


def extract_text_from_pdf(uploaded_file):
    """
    Extracts text from the uploaded PDF.

    Returns:
        text (str)
        total_pages (int)
    """

    text = ""

    with pdfplumber.open(uploaded_file) as pdf:

        total_pages = len(pdf.pages)

        for page in pdf.pages:

            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

    return text, total_pages