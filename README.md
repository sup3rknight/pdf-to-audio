# pdf-to-audio 🎧

A structured Python application that converts PDF documents into playable MP3 audiobooks. This project uses a modular architecture to handle text extraction and speech synthesis separately.

## 📂 Project Structure

```text
pdf-to-audio/
├── data/               # Input: Drop your PDF files here
├── exports/            # Output: MP3 files are generated here
├── src/                # Source code
│   ├── __init__.py     # Package initialization
│   ├── processor.py    # PDF text extraction logic
│   ├── speaker.py      # Text-to-Speech engine
│   └── main.py         # Main entry point
├── tests/              # Unit tests
├── .gitignore          # Prevents pushing venv and large data files
├── requirements.txt    # Project dependencies
└── README.md           # Documentation
```

🚀 Installation & Setup
1. Clone the repository
```Bash

git clone [https://github.com/YOUR_USERNAME/pdf-to-audio.git](https://github.com/YOUR_USERNAME/pdf-to-audio.git)
cd pdf-to-audio
```

2. Create a Virtual Environment
```Bash

# Windows
python -m venv venv
.\venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
3. Install Dependencies
Bash

pip install -r requirements.txt
```
## 📖 How to Use
Add your PDF: Place any .pdf file you want to convert into the data/ folder.

Run the Script: From the root folder, run:
```Bash

python -m src.main
```

Listen: Once finished, check the exports/ folder for your new .mp3 file.

## 📝 Important Notes
- AI Collaboration: This project was developed with the assistance of AI to help structure the professional folder hierarchy and modular logic.

- Audio Quality: This tool uses pyttsx3, which relies on your computer's built-in speech engine. As a result, the voice may sound robotic and is not as "human-like" or "perfect" as advanced cloud-based AI voices (like ElevenLabs or OpenAI TTS). It is designed for offline, functional use.

- Text Extraction: Complexity in PDF layouts (like multi-column papers or images) may affect the reading order.

## 🛠 Built With
PyPDF2 - PDF parsing

pyttsx3 - Offline Text-to-Speech


---