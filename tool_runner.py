from tools.web_crawler import crawl_webpage
from tools.pdf_scraper import scrape_pdf


tools = {
    "web_crawler": crawl_webpage,
    "research_paper_scraper": scrape_pdf
}


def run_tool(action, tool_input):

    if action not in tools:
        raise ValueError(f"Unknown tool: {action}")

    result = tools[action].invoke({
        "url": tool_input
    } if action == "web_crawler" else {
        "pdf_path": tool_input
    })

    return result