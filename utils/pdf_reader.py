import fitz
import os

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text +=page.get_text()
    return text


def extract_all_resumes_text(folder_path):
    resume_texts = []
    filenames = []
    for file in os.listdir(folder_path):
        if file.endwith(".pdf"):
            path = os.path.join(folder_path, file)
            text = extract_text_from_pdf(path)
            resume_texts.append(text)
            filenames.append(file)
    return filenames, resume_texts