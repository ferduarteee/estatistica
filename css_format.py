import streamlit as st
def css():    
    st.write(
    """
    <style>
    .main {
        margin-left: 0px; /* Ajuste a margem esquerda conforme necessário */
        margin-right: 500px; /* Ajuste a margem direita conforme necessário */
    }
    </style>
    """,
    unsafe_allow_html=True,
)