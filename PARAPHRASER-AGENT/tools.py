# tools.py
from langchain.tools import Tool
from langchain_google_genai import ChatGoogleGenerativeAI
from prompts import rephrase_prompt, humanize_prompt, grammar_prompt, plagiarism_prompt
import os
from dotenv import load_dotenv

load_dotenv()

gemini_llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY"),
    temperature=0.7
)

tools = [
    Tool(
        name="RephraseTool",
        func=lambda paragraph: gemini_llm.invoke(rephrase_prompt.format(paragraph=paragraph)).content,
        description="Professionally rewrites the input paragraph to improve phrasing, clarity, fluency, and style, while preserving its original meaning."
    ),
    Tool(
        name="HumanizerTool",
        func=lambda rephrased: gemini_llm.invoke(humanize_prompt.format(rephrased=rephrased)).content,
        description="Transforms the rephrased paragraph into a naturally flowing, human-like narrative with emotional resonance and personal tone."
    ),
    Tool(
        name="GrammarTool",
        func=lambda humanized: gemini_llm.invoke(grammar_prompt.format(humanized=humanized)).content,
        description="Analyzes and corrects grammatical, punctuation, and syntactic errors without altering the tone or intent of the paragraph."
    ),
    Tool(
        name="PlagiarismTool",
        func=lambda corrected: gemini_llm.invoke(plagiarism_prompt.format(corrected=corrected)).content,
        description="Rewrites the paragraph in a highly original way to minimize similarity with existing content and ensure plagiarism-free output."
    )
]
