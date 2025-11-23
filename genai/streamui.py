# import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from decouple import config

from genai.streamuiPrompt import prompt

GOOGLE_GEMINI_KEY = config("GOOGLE_GEMINI_KEY")
llm=ChatGoogleGenerativeAI(model="gemini-2.5-flash", google_api_key=GOOGLE_GEMINI_KEY)

# st.title("ARMaxAI")

# question = st.text_input("Your Question")

# if question:
#     response = llm.invoke(question)
#     st.write(response.content)

def ask_gemini(q):
    p = "Answer the question in less than 50 words.The question is -"
    full_question = p + q
    if q:
        answer = llm.invoke(full_question)
        return answer.content
    else:
        return "Sorry. I did not get you."