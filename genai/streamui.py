import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from decouple import config

GOOGLE_GEMINI_KEY = config("GOOGLE_GEMINI_KEY")
llm=ChatGoogleGenerativeAI(model="gemini-2.5-flash", google_api_key=GOOGLE_GEMINI_KEY)

st.title("ARMaxAI")

question = st.text_input("Your Question")

if question:
    response = llm.invoke(question)
    st.write(response.content)