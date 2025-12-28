from model_loader import generate_text

def urban_chatbot(issue):
    prompt = f"""
You are a smart city and urban planning expert.

Urban problem:
{issue}

Provide exactly 5 practical and realistic solutions.
Avoid generic or meaningless statements.
Number each solution clearly.
"""
    return generate_text(prompt)





