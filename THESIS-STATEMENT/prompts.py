# prompts.py
from langchain.prompts import PromptTemplate

thesis_prompt = PromptTemplate.from_template("""
You are an expert academic writing assistant.
Your task is to generate 3–5 unique, strong, and well-crafted thesis statements for the topic below:

Topic: "{topic}"

Guidelines:
- Each thesis must be concise, specific, and academically arguable.
- Avoid vague, overly general, or purely factual statements.
- Ensure logical clarity and formal academic tone.
- Statements should reflect original insight or critical stance.

Return only the thesis statements as a numbered list.
""")

humanize_prompt = PromptTemplate.from_template("""
You are a human-writing expert. Rewrite each thesis statement below to sound more natural, emotionally intelligent, and less robotic.

Guidelines:
- Keep the original argumentative meaning intact.
- Add subtle nuance, rhythm, and natural sentence variety.
- Ensure the language feels fluid and human.

Input Thesis Statements:


{thesis}


Return only the fully humanized list of thesis statements.
""")

grammar_prompt = PromptTemplate.from_template("""
You are a professional academic editor.
Your task is to correct all grammar, punctuation, and sentence structure issues in the list of thesis statements below.

Guidelines:
- Keep the academic tone and intent intact.
- Improve sentence clarity, conciseness, and coherence.
- Ensure advanced grammar and vocabulary throughout.

Input Thesis Statements:


{humanized}


Return only the grammatically correct and polished list.
""")

plagiarism_prompt = PromptTemplate.from_template("""
You are a plagiarism reduction assistant.
Your task is to rewrite the following thesis statements to ensure they are highly unique and plagiarism-safe.

Guidelines:
- Do not change the core idea or argumentative stance.
- Paraphrase sentence structures and word choices thoroughly.
- Avoid patterns that resemble typical online phrasing.

Input Thesis Statements:


{corrected}


Return only the final plagiarism-safe thesis statements as a numbered list.
""")
