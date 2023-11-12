import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)


with col1:
    st.image("images/me.JPG")

with col2:
    st.title("Yui Otaka")
    content = """
    Hello, I am Yui Otaka, from Tokyo in Japan. I work for an IT industry as a maintenance. 
    After graduate high school, I became a police officer in Tokyo, after that I used to work for a
    study abroad agency as a copy writer in Sydney and Cebu in Philippine. Bacause of covid situation,
    I went to back to Japan, I worked are a customer support and IT industry. 
    """
    st.info(content)

content2 = """
    Language:  Japanese(Native), 
               English(conversation level), 
               Korean(Intermediate level)
    """
st.write(content2)