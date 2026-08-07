from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import Chroma
import os
from dotenv import load_dotenv

load_dotenv()

embeddings = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-001",
    google_api_key=os.getenv("GOOGLE_API_KEY")
)


def create_vector_store(chunks):

    db = Chroma.from_texts(
        texts=chunks,
        embedding=embeddings,
        persist_directory="vector_db"
    )

    db.persist()

    return db


def load_vector_store():

    db = Chroma(
        persist_directory="vector_db",
        embedding_function=embeddings
    )

    return db