from langchain_core.messages import SystemMessage, HumanMessage


def agent_finalize(llm, query, tool_result):

    response = llm.invoke([
        SystemMessage(content="""
You are a helpful AI assistant.

STRICT RULES:
- The context provided below is extracted from a document.
- You MUST answer ONLY using this context.
- DO NOT say "context not provided".
- DO NOT ignore the context.
- If context is available, explain it clearly.

Your job is to summarize or explain the given content.
"""),
        HumanMessage(content=f"""
User Question:
{query}

Document Content:
{tool_result[:2000]}

Now explain the content clearly.
""")
    ])

    return response.content