import PyPDF2
from gtts import gTTS
import webbrowser

def pdf_to_text(pdf_path):
    text = ""
    with open(pdf_path, "rb") as file:
        pdf_reader = PyPDF2.PdfReader(file)
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()
    return text

def text_to_speech(text, output_path):
    tts = gTTS(text=text, lang="en")
    tts.save(output_path)

def pdf_to_mp3(pdf_path, output_path):
    text = pdf_to_text(pdf_path)
    text_to_speech(text, output_path)

if __name__ == "__main__":
    # Enter name of file to be converted to audio
    pdf_file = 'path/to/your/file.pdf'
    mp3_file = 'audio.mp3'

    pdf_to_mp3(pdf_file, mp3_file)

    # Open the generated MP3 file.
    webbrowser.open(mp3_file)
