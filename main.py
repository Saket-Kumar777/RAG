from dotenv import load_dotenv
import os
from rag.vector_store import store_embeddings
from rag.vector_store import store_embeddings, query_chroma
from rag.vector_store import retrieve_context
from rag.embedding import generate_embeddings
from rag.prompt import build_prompt

from langchain_groq import ChatGroq

from decision import agent_decide
from parser import parse_decision
from tool_runner import run_tool
from agent_finalize import agent_finalize

#  NEW IMPORTS
from rag.embedding import chunk_text, generate_embeddings

load_dotenv()

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    api_key=os.getenv("GROQ_API_KEY"),
    temperature=0
)

query = "Read and explain the content of test.pdf"

# STEP 1: Get data using tool
decision_text = agent_decide(llm, query)
action, tool_input = parse_decision(decision_text)

tool_result = run_tool(action, tool_input)
print("\nTool Result Preview:\n", tool_result[:300])


# STEP 2: Prepare vector DB (only once ideally)
chunks = chunk_text(tool_result)
embeddings = generate_embeddings(chunks)

store_embeddings(chunks, embeddings)


# STEP 3: Retrieval (core RAG)
query_embedding = generate_embeddings([query])[0]

retrieved_chunks = query_chroma(query_embedding, top_k=3)

print("\nRetrieved Chunks:\n", retrieved_chunks)


# STEP 4: Build context
context = "\n".join(retrieved_chunks)


# STEP 5: Final LLM call (RAG answer)
final_answer = agent_finalize(llm, query, context)

print("\nFinal Answer:\n")
print(final_answer)