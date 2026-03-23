from sentence_transformers import SentenceTransformer
from langchain_text_splitters import RecursiveCharacterTextSplitter

# Load embedding model (free, local)
model = SentenceTransformer("all-MiniLM-L6-v2")


def chunk_text(text: str):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )

    chunks = splitter.split_text(text)
    return chunks


def generate_embeddings(chunks):
    embeddings = model.encode(chunks)
    return embeddings