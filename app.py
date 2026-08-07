import streamlit as st
from google import genai
from dotenv import load_dotenv
import os

from pdf_utils import extract_text, split_text
from vector_store import create_vector_store, load_vector_store
from history import save_message, load_messages, clear_history

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GOOGLE_API_KEY")
)

st.set_page_config(
    page_title="AI PDF Chatbot",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI PDF Chatbot")

mode = st.sidebar.radio(
    "Select Mode",
    ["📄 PDF Chat", "🤖 Normal Chat"]
)


if st.sidebar.button("🗑 Clear Chat History"):
    clear_history()
    st.rerun()

uploaded_file = None

if mode == "📄 PDF Chat":

    st.sidebar.title("📄 Upload PDF")

    uploaded_file = st.sidebar.file_uploader(
        "Choose PDF",
        type=["pdf"]
    )

    if uploaded_file:

        pdf_text = extract_text(uploaded_file)

        chunks = split_text(pdf_text)

        create_vector_store(chunks)

        st.sidebar.success("✅ PDF Indexed Successfully")

        with st.expander("📄 PDF Preview"):
            st.write(pdf_text[:1000])


messages = load_messages()

for role, message in messages:
    with st.chat_message(role):
        st.markdown(message)

prompt = st.chat_input("Ask something...")

if prompt:

    save_message("user", prompt)

    with st.chat_message("user"):
        st.markdown(prompt)

    if mode == "📄 PDF Chat":

        if uploaded_file is None:

            answer = "⚠ Please upload a PDF first."

        else:

            db = load_vector_store()

            docs = db.similarity_search(
                prompt,
                k=3
            )

            context = "\n\n".join(
                [doc.page_content for doc in docs]
            )

            final_prompt = f"""
You are an AI assistant.

Answer ONLY using the PDF information below.

PDF Context:
{context}

Question:
{prompt}

If the answer is not present in the PDF, reply exactly:

I don't know based on the provided PDF.
"""

            response = client.models.generate_content(
                model="gemini-flash-latest",
                contents=final_prompt
            )

            answer = response.text

    else:

        response = client.models.generate_content(
            model="gemini-flash-latest",
            contents=prompt
        )

        answer = response.text

    save_message("assistant", answer)

    with st.chat_message("assistant"):
        st.markdown(answer)