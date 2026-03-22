import requests
from bs4 import BeautifulSoup
from langchain.tools import tool
from pydantic import BaseModel, Field


class WebCrawlerInput(BaseModel):
    url: str = Field(description="URL of the webpage to crawl and extract text from")


@tool("web_crawler", args_schema=WebCrawlerInput)
def crawl_webpage(url: str) -> str:
    """
    Fetch a webpage and return extracted clean text content.
    """

    response = requests.get(url, timeout=10)

    soup = BeautifulSoup(response.text, "html.parser")

    # remove unwanted tags
    for tag in soup(["script", "style", "nav", "footer", "header"]):
        tag.decompose()

    text = soup.get_text(separator=" ", strip=True)

    return text[:5000]