from langchain_core.messages import HumanMessage, SystemMessage


def agent_decide(llm, query):

    response = llm.invoke([
        SystemMessage(content="""
You are an AI decision engine.

Rules:
- If input contains a URL → use web_crawler
- If input contains ".pdf" → use research_paper_scraper

IMPORTANT:
- Return ONLY valid JSON
- Do NOT add explanation
- Do NOT add text before or after JSON

Format:
{
  "action": "tool_name",
  "input": "tool_input"
}
"""),
        HumanMessage(content=query)
    ])

    return response.content
