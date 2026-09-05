import os

import streamlit as st
from dotenv import load_dotenv

from ui.home import show_home
from ui.sidebar import create_sidebar

from rag.pdf_loader import extract_text_from_pdf
from rag.chunker import split_into_chunks
from rag.embeddings import create_embedding_model
from rag.vector_store import create_vector_store

load_dotenv()



st.set_page_config(
    page_title="VTU AI Study Assistant",
    page_icon="🎓",
    layout="wide"
)

show_home()

user_settings = create_sidebar()

question = st.text_area(
    "Ask your question",
    height=150,
    placeholder="Example: Explain Deadlock."
)

ask_button = st.button(
    "🚀 Ask Question",
    use_container_width=True
)

if ask_button:

    uploaded_file = user_settings["uploaded_file"]

    if uploaded_file is None:

        st.warning("Please upload a PDF first.")

    elif not question.strip():

        st.warning("Please enter a question.")

    else:

        text, pages = extract_text_from_pdf(uploaded_file)

        if not text.strip():

            st.error(
                "No readable text was found in this PDF. "
                "It may be a scanned/image-based PDF."
            )

        else:

            chunks = split_into_chunks(text)

            embedding_model = create_embedding_model()

            vector_store = create_vector_store(
                chunks,
                embedding_model
            )
            st.success("FAISS vector store created successfully!")
            with st.expander("🔍 View Generated Chunks"):

                for i, chunk in enumerate(chunks, start=1):

                    st.write(f"### Chunk {i}")

                    st.write(chunk)

                st.divider()

            st.success("PDF processed successfully!")

            st.write(f" Pages: {pages}")
            st.write(f" Characters extracted: {len(text)}")
            st.write(f" Chunks created: {len(chunks)}")
            #st.write(f"Vectors created: {len(vectors)}")
            #st.write(f"Vector dimensions: {len(vectors[0])}")