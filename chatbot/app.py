# chatbot/app.py
import os
import streamlit as st
import openai
from utils import call_llm

# 環境変数からAPIキーを取得
openai.api_key = os.getenv("OPENAI_API_KEY")

st.title("生成AIチャットボット")
user_input = st.text_input("メッセージを入力してください:")

if user_input:
    response = call_llm(user_input)
    st.write("Bot:", response)
