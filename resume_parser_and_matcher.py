import fitz
import spacy
import re
import nltk

nltk.download("stopwords")
from nltk.corpus import stopwords

nlp = spacy.load("en_core_web_sm")

def extract_pdf_text(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text("text")
    return text

def extract_name(text):
    lines = text.split("\n")
    
    lines = [line for line in lines if line.strip() and len(line.split()) > 1]

    for line in lines:
        doc = nlp(line)
        names = [ent.text for ent in doc.ents if ent.label_ == "PERSON"]
        print(names)
        
        if names:
            return names[0]
    
    return "Not found"

def extract_email(text):
    email_pattern = r"[a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    emails = re.findall(email_pattern, text)
    return emails[0] if emails else "Not found"

def extract_phone(text):
    phone_pattern = r"\+?\d[\d\s\-\(\)]{8,}\d"
    phones = re.findall(phone_pattern, text)
    return phones[0] if phones else "Not found"

def extract_skills(text, skills_list):
    detected_skills = set()
    
    for skill in skills_list:
        if skill.lower() in text.lower():
            detected_skills.add(skill)
    
    return list(detected_skills)

def parse_resume(resume_path, skills_list):
    text = extract_pdf_text(resume_path)

    return {
        "Name": extract_name(text),
        "Email": extract_email(text),
        "Phone": extract_phone(text),
        "Skills": extract_skills(text, skills_list)
    }

resume_path = "./resume.pdf"
skills_input = input("Enter the required skills (comma-separated): ")
skills_list = [skill.strip() for skill in skills_input.split(",")]

parsed_data = parse_resume(resume_path, skills_list)

print("\nExtracted Resume Data:")
for key, value in parsed_data.items():
    print(f"{key}: {value}")
