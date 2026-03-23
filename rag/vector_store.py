import chromadb

# Create client (local DB)
client = chromadb.Client()

# Create / get collection
collection = client.get_or_create_collection(name="documents")

def store_embeddings(chunks, embeddings):

    ids = [str(i) for i in range(len(chunks))]

    collection.add(
        ids=ids,
        documents=chunks,
        embeddings=embeddings
    )

    print("\nStored in ChromaDB:", len(chunks))

def query_chroma(query_embedding, top_k=3):

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )

    return results["documents"][0]

def retrieve_context(query, embedding_fn, top_k=3):

    query_embedding = embedding_fn([query])[0]

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )

    return results["documents"][0]