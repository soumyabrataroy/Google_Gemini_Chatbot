
import streamlit as st
# From here down is all the StreamLit UI
st.set_page_config(page_title="LangChain Demo", page_icon=":robot:")
st.header("Hey, I'm your Chat Bot")

import google.generativeai as genai

with st.sidebar:
    # Text input
    api_key = st.text_input("Enter your API key here:")

import os

os.environ["GOOGLE_API_KEY"] = api_key
genai.configure(api_key = os.environ['GOOGLE_API_KEY'])



def get_text():
    input_text = st.text_input("You: ")
    return input_text


chat_model = genai.GenerativeModel('gemini-pro')
chat = chat_model.start_chat(history=[])


user_input=get_text()
submit = st.button('Generate')  

if submit:
    
    try:
        response = chat.send_message(user_input)
        st.subheader("Answer:")

        st.write(response.text)
        # st.write(chat.history)
    except:
        st.warning('Please provide your valid API key to continue')

# resources: https://codemaker2016.medium.com/build-your-own-chatgpt-using-google-gemini-api-1b079f6a8415