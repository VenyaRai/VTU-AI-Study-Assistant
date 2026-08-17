import streamlit as st


def create_sidebar():
    """
    Creates the sidebar and returns all user selections.
    """

    with st.sidebar:

        st.header("📂 Upload Notes")

        uploaded_file = st.file_uploader(
            "Choose a PDF",
            type=["pdf"]
        )

        st.divider()

        st.header("📝 Answer Type")

        marks = st.radio(
            "Select Marks",
            (
                "5 Marks",
                "6–7 Marks",
                "8 Marks",
                "10 Marks",
                "Custom"
            )
        )

        word_limit = None

        if marks == "Custom":

            word_limit = st.slider(
                "Word Limit",
                min_value=100,
                max_value=1500,
                value=500,
                step=50
            )

        st.divider()

        st.header("🎯 Answer Style")

        style = st.selectbox(
            "Choose Style",
            (
                "Exam Ready",
                "Easy Explanation",
                "Revision Notes",
                "Bullet Notes"
            )
        )

        include_diagram = st.checkbox(
            "Include Diagram (if applicable)"
        )

    return {
        "uploaded_file": uploaded_file,
        "marks": marks,
        "word_limit": word_limit,
        "style": style,
        "include_diagram": include_diagram
    }