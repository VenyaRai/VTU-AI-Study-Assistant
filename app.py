import streamlit as st
from ui.home import show_home
from ui.sidebar import create_sidebar
from rag.pdf_loader import extract_text_from_pdf


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

    st.success("Your chatbot will answer here!")

    st.write(user_settings)

    st.write(question)

    uploaded_file = user_settings["uploaded_file"]

    if uploaded_file is None:

        st.warning("Please upload a PDF first.")

    else:

        text, pages = extract_text_from_pdf(uploaded_file)

        st.success("PDF Loaded Successfully!")

        st.write(f"Pages: {pages}")

        st.write(f"Characters: {len(text)}")

        st.text_area(
            "Preview",
            text[:2000],
            height=300
        )