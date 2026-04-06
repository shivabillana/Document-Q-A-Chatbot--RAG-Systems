import chromadb
import os
from dotenv import load_dotenv
load_dotenv()

client = chromadb.CloudClient(
  api_key= os.getenv("CHROMA_DB_API_KEY"),
  tenant= os.getenv("CHROMA_DB_TENANT"),
  database= os.getenv("CHROMA_DB_DATABASE")
  )


def create_collection(session_id):
    collection = client.get_or_create_collection(
        name = session_id
    )

    return collection

def store_chunks(collection,texts,embeddings):
    ids = [f"chunk_{i}" for i in range(len(texts))]

    collection.add(documents=texts,
                   embeddings=embeddings,
                   ids=ids)
    
    print("chunks stored:", collection.count())

def delete_session_collection(session_id):
    client.delete_collection(name=session_id)

