import requests
import os
from dotenv import load_dotenv
from langchain.messages import HumanMessage
from langchain_openrouter import ChatOpenRouter

load_dotenv()

llm = ChatOpenRouter(
    model = os.getenv("MODEL_NAME"),
)


def ask_llm(question,context_chunks):

    context = "\n\n".join(context_chunks)

    prompt = f"""
    Answer the question using ONLY the context below.

    Context: 
    {context}

    Question:
    {question}

    Answer:
    """

    response = llm.invoke([HumanMessage(content=prompt)])

    return response.content