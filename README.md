# Resume Parser & Matcher

A Python-based Resume Parser that extracts key information from resumes, including **Name, Email, Phone Number, and Skills**. It also allows users to input a list of required skills and matches them against the extracted text from the resume.

## Features
- **Extracts Personal Information:** Name, Email, and Phone Number.
- **Skill Matching:** Users can input required skills, and the script will match them with those found in the resume.
- **Multi-Word Skill Matching:** Detects both single and multi-word skills like "Integration Suite."
- **Text Extraction:** Uses `PyMuPDF` (fitz) to extract text from PDF resumes.
- **NLP-Based Parsing:** Utilizes `spaCy` for name detection and `nltk` for stopword filtering.

## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/resume-parser-matcher.git
   cd resume-parser-matcher

2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt

3. **Download Required NLP Models & Stopwords:**
   ```bash
   import nltk
   nltk.download("stopwords")
   python -m spacy download en_core_web_sm

## Usage

1. **Prepare Your Resume (PDF Format):** Place the resume file in the project directory and update the `resume_path` in the script.

2. **Run the Script:**

   ```bash
   python resume_parser.py

3. **Input Required Skills:** The script will prompt you to enter a comma-separated list of skills.

4. **View Extracted Data:** The script will output the parsed resume details, including matched skills.

## Example Output

- **Example:**

   ```bash
   Enter the required skills (comma-separated): Python, Azure, React, Integration Suite

   Extracted Resume Data:
   Name: John Doe
   Email: johndoe@example.com
   Phone: (123) 456-7890
   Skills: ['Python', 'React']

## Technologies used

- Python 3.9+
- PyMuPDF (fitz) - PDF text extraction
- spaCy - NLP for name recognition
- nltk - Stopwords filtering
- re (Regex) - Email and phone number extraction