# tools.py
import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from prompts import thesis_prompt, humanize_prompt, grammar_prompt, plagiarism_prompt

load_dotenv()

gemini_llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY"),
    temperature=0.7
)

tools = {
    "ThesisGenerator": lambda topic: gemini_llm.invoke(thesis_prompt.format(topic=topic)).content,
    "Humanizer": lambda thesis: gemini_llm.invoke(humanize_prompt.format(thesis=thesis)).content,
    "GrammarCorrector": lambda humanized: gemini_llm.invoke(grammar_prompt.format(humanized=humanized)).content,
    "PlagiarismReducer": lambda corrected: gemini_llm.invoke(plagiarism_prompt.format(corrected=corrected)).content
}
