import os

from langchain_google_genai import ChatGoogleGenerativeAI
from decouple import config

GOOGLE_GEMINI_KEY = config("GOOGLE_GEMINI_KEY")
llm=ChatGoogleGenerativeAI(model="gemini-2.5-flash", google_api_key=GOOGLE_GEMINI_KEY)

print("Q and A with VOAGPT")
print("-------------------")

question=input("Q :")
# print("Q :",question)
response=llm.invoke(question)
print("A :",response.content)
