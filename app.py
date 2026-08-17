import streamlit as st

from ui.home import show_home
from ui.sidebar import create_sidebar


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