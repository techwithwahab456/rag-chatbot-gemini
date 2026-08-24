from pypdf import PdfReader


def load_pdf(file_path):
    reader = PdfReader(file_path)

    text = ""

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    return text


if __name__ == "__main__":
    pdf_path = "documents/sample.pdf"

    text = load_pdf(pdf_path)

    print("PDF loaded successfully!")
    print(f"Characters extracted: {len(text)}")

    print("\n--- First 1000 characters ---\n")
    print(text[:1000])