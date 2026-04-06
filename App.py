import streamlit as st
import uuid
import time
import os
from sentence_transformers import SentenceTransformer
from DocumentLoaders import fileloader
from Chunking import divdingchunks
from EmbeddingGenerator import generate_embeddings
from VectorStorage import create_collection, store_chunks, delete_session_collection
from Retriever import retrieve_chunks
from LLM import ask_llm



@st.cache_resource
def load_model():
    return SentenceTransformer("all-MiniLM-L6-v2")

model = load_model()


st.title("Document Q&A Chat")
st.write("Upload a document and ask questions about it.")


if "collection" not in st.session_state:
    st.session_state.collection = None

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "session_id" not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())

if "last_activity" not in st.session_state:
    st.session_state.last_activity = time.time()

if "uploaded_files_list" not in st.session_state:
    st.session_state.uploaded_files_list = []

TIMEOUT = 600

if st.session_state.collection:
    if time.time() - st.session_state.last_activity>TIMEOUT:
        delete_session_collection(st.session_state.session_id)

        st.session_state.collection = None
        st.session_state.chat_history = []

        st.warning("session expired due to inactivity.Document deleted.")
        st.stop()

if st.session_state.collection is None:
    st.session_state.collection = create_collection(st.session_state.session_id)

uploaded_files = st.file_uploader("Upload a Document", type=["pdf", "docx", "txt", "html"],accept_multiple_files=True)


if uploaded_files:
    for uploaded_file in uploaded_files:

        if uploaded_file.name in st.session_state.uploaded_files_list:
            continue

        file_path = f"{st.session_state.session_id}_{uploaded_file.name}"


        with open(file_path,"wb") as f:
            f.write(uploaded_file.getbuffer())

        st.session_state.last_activity = time.time()

        with st.spinner(f"Processing {uploaded_file.name}....."):
            documents = fileloader(file_path)

            chunks = divdingchunks(documents)

            texts, embeddings = generate_embeddings(chunks, model)

            store_chunks(st.session_state.collection, texts, embeddings)

        if os.path.exists(file_path):
            os.remove(file_path)

        st.session_state.uploaded_files_list.append(uploaded_file.name)

        st.success(f"{uploaded_file.name} added successfully!")


if st.session_state.uploaded_files_list:
    st.write("📂 Uploaded Files:")
    for file in st.session_state.uploaded_files_list:
        st.write(f"- {file}")


if st.session_state.collection and st.session_state.uploaded_files_list:

    for role,message in st.session_state.chat_history:
        st.chat_message(role).write(message)

    question = st.chat_input("Ask a question about the Document")

    if question:

        # Update activity
        st.session_state.last_activity = time.time()

        st.chat_message("user").write(question)

        context = retrieve_chunks(
            st.session_state.collection,
            question,
            model
        )

        answer = ask_llm(question,context)

        st.chat_message("assistant").write(answer)

        st.session_state.chat_history.append(("user",question))
        st.session_state.chat_history.append(("assistant",answer))


if st.session_state.collection:
    if st.button("End Chat Session"):
         
         delete_session_collection(st.session_state.session_id)

         st.session_state.collection = None
         st.session_state.chat_history = []
         st.session_state.uploaded_files_list = []

         st.success("Session ended and document deleted.")
