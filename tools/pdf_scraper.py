import pdfplumber
from langchain.tools import tool
from pydantic import BaseModel, Field


class PDFScraperInput(BaseModel):
    pdf_path: str = Field(description="Path to the research paper PDF file")


@tool("research_paper_scraper", args_schema=PDFScraperInput)
def scrape_pdf(pdf_path: str) -> str:
    """
    Extract text from a research paper PDF.
    """

    text = ""

    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text

    return text[:5000]