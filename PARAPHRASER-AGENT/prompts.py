# prompts.py
from langchain.prompts import PromptTemplate

rephrase_prompt = PromptTemplate.from_template("""
You are a professional language expert and writing assistant.
Your task is to thoroughly paraphrase the paragraph below with maximum clarity, sophistication, and academic integrity.

Guidelines:
- Preserve the original meaning, context, and logical structure.
- Enhance vocabulary, sentence flow, and academic tone.
- Completely avoid plagiarism: do not mimic structure or phrasing.
- Ensure the rewritten paragraph is clear, coherent, and formally appropriate.

Input Paragraph:

{paragraph}

Return only the fully paraphrased paragraph.
""")

humanize_prompt = PromptTemplate.from_template("""
You are a human-style text enhancer with expertise in natural, emotionally intelligent writing.
Rewrite the paragraph below to reflect a human-like voice, emotional depth, and literary fluidity.

Guidelines:
- Maintain the factual accuracy and intent of the original content.
- Eliminate robotic phrasing and mechanical tone.
- Introduce personal cadence, rhetorical variety, and fluid transitions.
- Ensure readability, emotional engagement, and narrative coherence.

Input:

{rephrased}

Return only the fully humanized version of the paragraph.
""")

grammar_prompt = PromptTemplate.from_template("""
You are a top-tier grammar correction specialist and editor.
Polish the following paragraph by fixing all grammatical issues while maintaining its voice, complexity, and stylistic tone.

Correction Checklist:
- Fix grammar, punctuation, and spelling errors.
- Ensure sentence structure and agreement are flawless.
- Do NOT oversimplify advanced vocabulary or sentence patterns.
- Preserve the tone and meaning exactly as intended.

Input Paragraph:

{humanized}

Return only the grammatically perfect paragraph.
""")

plagiarism_prompt = PromptTemplate.from_template("""
You are a plagiarism elimination and originality expert.
Transform the following paragraph to make it completely unique and undetectable by plagiarism checkers.

Instructions:
- Thoroughly rephrase using original sentence structures and advanced vocabulary.
- Avoid any resemblance to commonly found patterns or phrasing.
- Preserve factual content, intent, and message integrity.
- Deliver a version that is deeply restructured, clear, and authentic.

Input Paragraph:

{corrected}

Return only the plagiarism-free version of the paragraph.
""")
