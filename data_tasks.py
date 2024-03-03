import streamlit as st
from gpt4all import GPT4All

model = GPT4All(model_name='orca-mini-3b-gguf2-q4_0.gguf')

st.title("Question Generator App")

user_input = st.text_input("enter a phrase:")

if st.button("generate question"):
    question = model.generate(prompt='write a question based on this text' + user_input, temp=0)
    st.write("generated question:", question)
