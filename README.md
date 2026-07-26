# 📄 AI Resume Analyzer

An AI-powered Resume Analyzer built with **Streamlit**, **Groq API**, and **Prompt Engineering**. This application analyzes resumes, evaluates ATS compatibility, identifies missing skills, suggests improvements, and generates interview questions to help users build stronger resumes.

---

## 🚀 Features

- 📄 Upload Resume (PDF or DOCX)
- ✍️ Paste Resume Text
- 🤖 AI-Powered Resume Analysis using Groq API
- 📊 Resume Score (Out of 100)
- 🎯 ATS Compatibility Score
- ✅ Strengths Analysis
- ❌ Weaknesses Analysis
- 💡 Missing Skills Detection
- 🚀 Suggested Projects
- 💼 Interview Questions Generation
- 📚 Recommended Learning Topics
- 📥 Download Analysis Report

---

## 🛠️ Tech Stack

- Python
- Streamlit
- Groq API
- Prompt Engineering
- PyPDF2
- python-docx
- python-dotenv

---

## 📁 Project Structure

```
AI-Resume-Analyzer/
│
├── app.py
├── prompts.py
├── utils.py
├── requirements.txt
├── README.md
├── .gitignore
├── .env.example
├── LICENSE
├── assets/
│   └── screenshot.png
└── docs/
    └── project-report.pdf
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Yashika05-ai/AI-Resume-Analyzer.git
```

### 2. Move to the Project Folder

```bash
cd AI-Resume-Analyzer
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Configure API Key

Create a `.env` file in the project root.

```env
GROQ_API_KEY=your_groq_api_key_here
```

Replace `your_groq_api_key_here` with your Groq API key.

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

The application will open in your browser at:

```
http://localhost:8501
```

---

## 📷 Screenshots

### Home Page

(Add a screenshot here)

### Resume Analysis

(Add a screenshot here)

---

## 📋 Project Workflow

```
User Uploads Resume
        │
        ▼
Extract Resume Text
        │
        ▼
Prompt Template
        │
        ▼
Groq API
        │
        ▼
AI Resume Analysis
        │
        ▼
Display Results
```

---

## 🎯 Future Enhancements

- Multi-language Support
- AI Career Chatbot
- Resume Comparison
- Job Role Selection
- Resume PDF Report Generation
- Dark Mode
- Resume History

---

## 📚 Learning Outcomes

This project demonstrates:

- Streamlit Application Development
- API Integration
- Prompt Engineering
- File Handling (PDF & DOCX)
- Environment Variable Management
- AI-based Resume Analysis

---

## 📄 License

This project is licensed under the MIT License.

---

⭐ If you found this project useful, consider giving it a star on GitHub!