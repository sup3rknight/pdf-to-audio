import os
from src import extract_text_from_pdf, Speaker

def run():
    # Define paths
    base_dir = os.getcwd()
    data_dir = os.path.join(base_dir, "data")
    export_dir = os.path.join(base_dir, "exports")

    # 1. Automatically find the first PDF in the data folder
    pdf_files = [f for f in os.listdir(data_dir) if f.endswith('.pdf')]

    if not pdf_files:
        print(f"Error: No PDF files found in {data_dir}")
        return

    # Take the first PDF found
    target_pdf = pdf_files[0]
    input_path = os.path.join(data_dir, target_pdf)
    
    # Create output name based on the PDF name
    output_filename = target_pdf.replace(".pdf", ".mp3")
    output_path = os.path.join(export_dir, output_filename)

    print(f"--- VoxPDF: Processing '{target_pdf}' ---")
    
    # 2. Extract Text
    text = extract_text_from_pdf(input_path)
    
    if not text or text.startswith("Error"):
        print(f"Extraction failed: {text}")
        return

    # 3. Convert to Audio
    narrator = Speaker(rate=160)
    print(f"Generating audio: {output_filename}...")
    
    success = narrator.save_audio(text, output_path)
    
    if success:
        print(f"✅ Success! File saved to: {output_path}")
    else:
        print("❌ Failed to generate audio.")

if __name__ == "__main__":
    run()