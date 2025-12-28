from model_loader import generate_text

def summarize_text(text):
    prompt = f"""
You are a summarization system.

Task:
Rewrite the content as a neutral summary.

Rules:
- Write ONLY one paragraph
- Do NOT add titles, headings, or labels
- Do NOT start with words like "Recommendation", "Conclusion", or "Summary"
- Do NOT give advice
- Do NOT use bullet points
- Only restate the main ideas clearly

Content:
{text}
"""
    return generate_text(prompt, max_tokens=150)





