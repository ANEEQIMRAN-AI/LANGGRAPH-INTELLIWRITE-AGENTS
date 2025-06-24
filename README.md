# LANGGRAPH-INTELLIWRITE-AGENTS

**LangGraph IntelliWrite Agents** is a modular, professional AI writing toolkit built with **LangChain**, **LangGraph**, and **Gemini LLM**. It provides intelligent, multi-agent pipelines to assist in academic writing with human-level fluency, grammar accuracy, and plagiarism reduction.

---

## ✨ Features

✅ Modular architecture using LangGraph and LangChain  
✅ Multi-agent pipelines with Humanizer, Grammar, and Plagiarism tools  
✅ Supports:
- 🎯 Thesis Statement Generation
- 📝 Essay Writing
- ♻️ Paragraph Paraphrasing

✅ Gemini 1.5 Flash-powered natural language understanding  
✅ Ready for CLI and UI integration  
✅ Clean, production-ready Python code

---

## 🧠 Agent Pipelines

### 1. Thesis Statement Generator
```text
USER → LLM → H.AGENT → G.AGENT → P.AGENT → FINAL OUTPUT
```
- Generates 3–5 high-quality, arguable thesis statements.
- Humanizes tone, fixes grammar, and reduces plagiarism.

### 2. Essay Writer Agent
```text
USER → LLM → H.AGENT → G.AGENT → P.AGENT → FINAL OUTPUT
```
- Writes structured essays (800–1000 words).
- Academic tone, sectioned format, and humanized language.

### 3. Paraphrasing Agent
```text
USER → LLM → H.AGENT → G.AGENT → P.AGENT → FINAL OUTPUT
```
- Rewrites any paragraph with improved fluency and uniqueness.

---

## 📁 Folder Structure
```bash
LANGGRAPH-INTELLIWRITE-AGENTS/
├── prompts.py          # LLM and agent prompt templates
├── tools.py            # Gemini LLM tool wrappers
├── graphbuilder.py     # LangGraph agent flow logic
├── main.py             # CLI entry point
├── requirements.txt    # Python dependencies
├── .env.template       # API key and config template
```

---

## 🚀 Quickstart

### 1. Clone the Repo
```bash
git clone https://github.com/your-username/LANGGRAPH-INTELLIWRITE-AGENTS.git
cd LANGGRAPH-INTELLIWRITE-AGENTS
```

### 2. Create Environment
```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

### 3. Setup API Key
Create a `.env` file from the template:
```env
GOOGLE_API_KEY=your_gemini_api_key
```

### 4. Run Any Agent
```bash
python main.py  # Modify per agent logic (thesis, essay, etc.)
```

---

## 🧩 Built With
- [LangChain](https://www.langchain.com/)
- [LangGraph](https://github.com/langchain-ai/langgraph)
- [Gemini LLM](https://deepmind.google/technologies/gemini)
- Python 3.10+

---

## 📄 License
MIT License © 2025 Aneeq Imran

---

## 🤝 Contributing
Pull requests and feedback are welcome. For major changes, please open an issue first to discuss what you would like to change.

---

## 📬 Contact
**Author**: Aneeq Imran  
**Email**: aneeqimran.ai@gmail.com  
**LinkedIn**: [ANEEQ IMRAN](https://www.linkedin.com/in/aneeq-imran-977077340/)
