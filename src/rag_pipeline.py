from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

def create_vector_store(chunks):
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    return FAISS.from_texts(chunks, embeddings)


def ask_question(vector_store, query):
    docs = vector_store.similarity_search(query)

    context = "\n".join([doc.page_content for doc in docs])

    return f"""
Relevant info from your data:

{context}

Your question:
{query}
"""