def build_prompt(query, context):

    return f"""
You are an AI assistant.

Use ONLY the provided context to answer.

Context:
{context}

Question:
{query}

Answer:
"""