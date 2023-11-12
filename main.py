import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/me.JPG")

with col2:
    st.title("Yui Otaka")
    content = """
    Hello, I am Yui Otaka, from Japan. living Tokyo.
    """
    st.info(content)