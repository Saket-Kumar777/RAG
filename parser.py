import json
import re


def parse_decision(decision_text):

    # Extract JSON from text (important)
    match = re.search(r"\{.*\}", decision_text, re.DOTALL)

    if not match:
        raise ValueError("No JSON found in LLM output")

    json_text = match.group()

    try:
        decision = json.loads(json_text)
        return decision["action"], decision["input"]
    except Exception:
        raise ValueError("Invalid LLM decision format")