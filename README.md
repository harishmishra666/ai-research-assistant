# 🔬 AI Research Assistant

An AI-powered research assistant built with **Python, Streamlit, Google Gemini AI, Web Research, and PDF Analysis**.

The AI Research Assistant helps students, researchers, and academic professionals discover research sources, analyze research papers, generate structured research summaries, ask questions from uploaded PDFs, and create professional research reports.

---

## 🚀 Features

### 🔬 AI Research Generation

Enter a research topic and generate an AI-powered research report using Google Gemini AI.

The system can generate:

* Research Overview
* Research Questions
* Key Findings
* Major Concepts
* Applications
* Challenges
* Research Gaps
* Future Scope
* Conclusion

---

### 🌐 Web Research

Search the web for relevant research sources directly from the application.

Features include:

* Web source discovery
* Source titles
* Source descriptions
* Clickable source links
* Research snippets
* Multiple research sources
* AI-powered source analysis

---

### 🤖 AI Research Summary

The application analyzes discovered web sources and generates a structured research summary using Google Gemini AI.

Generated sections include:

* Research Overview
* Key Findings
* Major Concepts
* Applications
* Challenges
* Research Gaps
* Future Scope
* Conclusion
* References

The generated summary uses the discovered web sources as research context.

---

### 📄 PDF Research Paper Analyzer

Upload a research paper in PDF format and analyze it using AI.

The PDF analyzer provides:

* Paper Summary
* Research Objective
* Methodology
* Key Findings
* Important Contributions
* Limitations
* Research Gaps
* Future Scope
* Possible Research Questions

---

### 💬 Ask AI from PDF

After uploading a research paper, users can ask questions about the document.

The AI answers questions using the extracted PDF content as context.

Example questions:

```text
What is the main objective of this research?

What methodology was used?

What are the major findings?

What are the limitations of this research?

What future research is suggested?
```

---

### 📊 Professional Research Report

The application can generate a professional PDF research report from AI-generated research content.

The report includes:

* Research topic
* Structured research content
* Research sections
* Source references
* Original source URLs

---

### 📥 Download Research Results

Users can download generated research content as:

* `.txt`
* Professional `.pdf`

---

## 🧠 AI Capabilities

The project uses **Google Gemini AI** for:

* Research generation
* Research summarization
* PDF analysis
* Question answering
* Research insights
* Academic content generation

---

## 🛠️ Technologies Used

| Technology            | Purpose                          |
| --------------------- | -------------------------------- |
| Python                | Core programming language        |
| Streamlit             | Web application framework        |
| Google Gemini AI      | AI-powered research and analysis |
| Google GenAI SDK      | Gemini API integration           |
| PyPDF                 | PDF text extraction              |
| ReportLab             | PDF report generation            |
| DDGS                  | Web search                       |
| BeautifulSoup         | Web content processing           |
| Requests              | HTTP requests                    |
| python-dotenv         | Environment variable management  |
| Streamlit Option Menu | Application navigation           |
| Git & GitHub          | Version control                  |

---

## 📁 Project Structure

```text
ai-research-assistant/
│
├── app.py
│
├── research.py
│
├── utils/
│   ├── __init__.py
│   └── research.py
│
├── .gitignore
│
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/harishmishra666/ai-research-assistant.git
```

### 2. Open the project

```bash
cd ai-research-assistant
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

#### Windows

```powershell
.\venv\Scripts\Activate.ps1
```

#### macOS / Linux

```bash
source venv/bin/activate
```

---

## 📦 Install Dependencies

Install the required Python packages:

```bash
python -m pip install streamlit google-genai python-dotenv pypdf reportlab streamlit-option-menu ddgs requests beautifulsoup4
```

---

## 🔑 Gemini API Configuration

The application requires a **Google Gemini API key**.

Create a `.env` file in the project root:

```text
GEMINI_API_KEY=your_gemini_api_key_here
```

### ⚠️ Security

Never upload your `.env` file or API key to GitHub.

The project `.gitignore` already excludes:

```text
.env
venv/
__pycache__/
```

---

## ▶️ Run the Application

Start the Streamlit application with:

```bash
python -m streamlit run app.py
```

The application will open in your browser.

Usually:

```text
http://localhost:8501
```

---

## 🖥️ Application Sections

The application provides a simple navigation menu:

```text
🏠 Home
🔬 Research
🌐 Web Research
📄 PDF Analyzer
💬 Ask AI
```

---

## 🔬 How It Works

### Research Generation

```text
Research Topic
       ↓
Google Gemini AI
       ↓
Structured Research Report
       ↓
Download TXT / PDF
```

### Web Research

```text
Research Topic
       ↓
Web Search
       ↓
Research Sources
       ↓
Source Snippets
       ↓
Gemini AI Analysis
       ↓
AI Research Summary
       ↓
Professional Research PDF
```

### PDF Analysis

```text
Upload Research Paper
       ↓
PDF Text Extraction
       ↓
Google Gemini AI
       ↓
Research Paper Analysis
       ↓
Insights & Research Gaps
```

### Ask AI

```text
Upload PDF
       ↓
Extract PDF Content
       ↓
Ask Question
       ↓
Gemini AI
       ↓
Context-based Answer
```

---

## 🎯 Use Cases

This project can be useful for:

* 🎓 B.Tech students
* 🎓 M.Tech students
* 🔬 Researchers
* 👨‍🏫 Teachers and professors
* 📚 Academic projects
* 📄 Research paper analysis
* 🧠 Literature review preparation
* 💡 Research topic exploration
* 📝 Academic research assistance

---

## 🚀 Future Enhancements

Planned improvements include:

* 🧠 AI Research Question Generator
* 🎯 Research Objectives Generator
* 🧪 Hypothesis Generator
* 📚 Literature Review Generator
* 🔎 Advanced academic search
* 📰 Research paper source discovery
* 📊 Research trend analysis
* 📈 Research visualization
* 🔗 Citation management
* 📑 Multiple PDF comparison
* 🗂️ Research project workspace
* 💾 Research history
* 🌐 Public cloud deployment
* 👥 Multi-user support

---

## 🔐 Security

This project follows basic API-key security practices.

Sensitive configuration is stored in:

```text
.env
```

The `.env` file is excluded from Git using:

```text
.env
```

**Never commit API keys, passwords, tokens, or other secrets to GitHub.**

---

## 📌 Project Status

🚧 **Active Development**

The project is continuously being improved with additional AI research and automation features.

---

## 👨‍💻 Author

### Harish Mishra

**AI & Automation Enthusiast | Agentic AI | Generative AI | Python | Automation Workflows**

GitHub:
https://github.com/harishmishra666

LinkedIn:
https://www.linkedin.com/in/harishmishra666/

Portfolio:
https://harishmishra666.netlify.app/

Instagram:
https://www.instagram.com/harishmishra_ai_and_automation/

---

## ⭐ Support

If you find this project useful, consider giving the repository a ⭐ on GitHub.

---

## 📄 License

This project is intended for educational, research, and portfolio purposes.
