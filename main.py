from dotenv import load_dotenv
import os

from langchain_groq import ChatGroq

from decision import agent_decide
from parser import parse_decision
from tool_runner import run_tool
from agent_finalize import agent_finalize

load_dotenv()

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    api_key=os.getenv("GROQ_API_KEY"),
    temperature=0
)

query = "Read and explain the content of test.pdf"

# Step 1: Decide tool
decision_text = agent_decide(llm, query)
print("Decision:", decision_text)

# Step 2: Parse
action, tool_input = parse_decision(decision_text)
print("Action:", action)
print("Input:", tool_input)

# Step 3: Run tool
tool_result = run_tool(action, tool_input)
print("Tool Result Preview:", tool_result[:300])

# Step 4: Final answer
final_answer = agent_finalize(llm, query, tool_result)

print("\nFinal Answer:\n")
print(final_answer)