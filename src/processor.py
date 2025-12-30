import PyPDF2
import os

def extract_text_from_pdf(pdf_path):
    """
    Extracts all text from a PDF file.
    """
    if not os.path.exists(pdf_path):
        return "Error: File not found."

    text_content = []
    
    try:
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            
            # Check if PDF is encrypted
            if reader.is_encrypted:
                return "Error: PDF is encrypted. Please provide an unencrypted file."

            print(f"Reading {len(reader.pages)} pages...")
            
            for page_num in range(len(reader.pages)):
                page = reader.pages[page_num]
                page_text = page.extract_text()
                
                if page_text:
                    # Basic cleaning: removing extra whitespace
                    clean_text = " ".join(page_text.split())
                    text_content.append(clean_text)
            
            # Combine all pages into one large string
            return "\n".join(text_content)

    except Exception as e:
        return f"Error during extraction: {str(e)}"