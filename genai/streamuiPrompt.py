import streamlit as st
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from decouple import config

GOOGLE_GEMINI_KEY = config("GOOGLE_GEMINI_KEY")
llm=ChatGoogleGenerativeAI(model="gemini-2.5-flash", google_api_key=GOOGLE_GEMINI_KEY)

st.title("ARMax Currency Info AI")
prompt = PromptTemplate(
    input_variables=["country", "paragraph", "language"],
    template="What is the currency of{country}? Answer in{paragraph} short paragraph in {language}",
)
country = st.text_input("Country")
paragraph = st.number_input("Paragraph",min_value=1, max_value=5)
language = st.text_input("Language")

if country and paragraph and language:
    response = llm.invoke(prompt.format(country=country, paragraph=paragraph, language=language))
    st.write(response.content)