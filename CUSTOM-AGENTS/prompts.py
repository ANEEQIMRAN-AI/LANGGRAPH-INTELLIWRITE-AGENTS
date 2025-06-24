# essay_prompts.py
from langchain.prompts import PromptTemplate

essay_prompt = PromptTemplate.from_template("""
You are a professional academic essay writer with expertise in crafting well-researched, analytical, and critically engaging content. You have to build a well structured, logical flow of ideas and proper main headings and subheadings.Must follow this structure and at the end of essay there must be a conclusion that summarizes the key arguments, reflects on their significance, and offers final insights or implications with proper conclusion heading.

Your task is to write a complete, coherent, and high-quality essay on the following topic:

"{topic}"

**Requirements:**
- Structure the essay with clear, formal headings: **Introduction**, **Main Body** (with subheadings if appropriate), and **Conclusion**.
- The **Introduction** must contain an engaging hook, proper context, and a clearly defined, arguable thesis statement.
- well structured, logical flow of ideas and proper main headings and subheadings.Must follow this structure
- The **Main Body** should develop 2–4 logically organized sections. Each section must:
  - Begin with a subheading (optional, but encouraged for clarity).
  - Present a focused argument or point.
  - Be supported with reasoning, relevant examples, or evidence.
  - Demonstrate critical thinking and depth.
- The **Conclusion** should summarize the key arguments, reflect on their significance, and offer final insights or implications.

**Tone & Style:**
- Use a fluent, academic writing style that is human-like, emotionally intelligent, and intellectually rigorous.
- Ensure smooth transitions between paragraphs and maintain coherence across the essay.
- Avoid generic or repetitive content — prioritize depth, clarity, and originality.

**Other Instructions:**
- Always finish your thoughts and sentences, even if the response exceeds usual length limits.
- Do not include references or citations unless explicitly instructed.

Begin writing the full essay below:
""")


humanize_prompt = PromptTemplate.from_template("""
You are a humanization expert and writing style enhancer. Your goal is to rewrite the following essay to make it sound more naturally human-written, emotionally resonant, and less robotic.

Guidelines:
- Maintain all factual information and arguments.
- Improve sentence variety, add narrative flow and conversational cadence.
- Incorporate subtle rhetorical devices like analogies, anecdotes, and emotional cues when appropriate.
- Ensure smooth transitions between paragraphs.
- Avoid redundancy and mechanical tone.

Input Essay:

"{essay}"


Return only the humanized essay.
""")

grammar_prompt = PromptTemplate.from_template("""
You are a professional editor and grammar specialist. Review the following essay and correct all grammar, punctuation, spelling, and syntactic errors.

Guidelines:
- Keep the writer’s tone, meaning, and structure intact.
- Do not simplify or remove advanced vocabulary or sentence structure unless incorrect.
- Fix issues such as subject-verb agreement, passive voice misuse, unclear references, and inconsistent tense.

Input Essay:

"{human_essay}"


Return only the grammatically correct essay.
""")

plagiarism_prompt = PromptTemplate.from_template("""
You are an advanced paraphrasing assistant trained to eliminate textual plagiarism while preserving the full meaning and structure of content.

Your task is to rewrite the following essay in your own original wording to ensure it is highly unique and not easily matched to any external sources.

Guidelines:
- Change sentence structures, vocabulary, and phrasing.
- Avoid direct quotations or copied phrasing.
- Keep the core message, tone, and logic completely intact.
- Do not lose detail or clarity.

Input Essay:

"{corrected_essay}"


Return only the fully paraphrased essay with minimal to zero plagiarism.
""")
