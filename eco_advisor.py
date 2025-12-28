from model_loader import generate_text

def eco_tips(topic):
    prompt = f"""
You are an environmental sustainability expert.

Topic:
{topic}

Give 5 simple and practical eco-friendly tips.
Number them clearly.
"""
    return generate_text(prompt)


