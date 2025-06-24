# essay_tools.py
import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from prompts import essay_prompt, humanize_prompt, grammar_prompt, plagiarism_prompt

load_dotenv()

gemini_llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY"),
    temperature=0.7
)

tools = {
    "EssayWriter": lambda topic: gemini_llm.invoke(essay_prompt.format(topic=topic)).content,
    "Humanizer": lambda essay: gemini_llm.invoke(humanize_prompt.format(essay=essay)).content,
    "GrammarCorrector": lambda human_essay: gemini_llm.invoke(grammar_prompt.format(human_essay=human_essay)).content,
    "PlagiarismReducer": lambda corrected_essay: gemini_llm.invoke(plagiarism_prompt.format(corrected_essay=corrected_essay)).content
}
