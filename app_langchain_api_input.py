import streamlit as st
# From here down is all the StreamLit UI
st.set_page_config(page_title="LangChain Demo", page_icon=":robot:")
st.header("Hey, I'm your Chat GPT")


from langchain_google_genai import ChatGoogleGenerativeAI

with st.sidebar:
    # Text input
    api_key = st.text_input("Enter your API key here:")

import os

os.environ["GOOGLE_API_KEY"] = api_key

from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)




if "sessionMessages" not in st.session_state:
     st.session_state.sessionMessages = [
        SystemMessage(content="You are a helpful assistant.")
    ]



def load_answer(question):

    st.session_state.sessionMessages.append(HumanMessage(content=question)) # human message
    input_message = [st.session_state.sessionMessages[i].content for i in range(len(st.session_state.sessionMessages))]

    assistant_answer  = chat.invoke(input_message) # system + human


    st.session_state.sessionMessages.append(AIMessage(content=assistant_answer.content)) # ai message

    return assistant_answer.content, input_message


def get_text():
    input_text = st.text_input("You: ")
    return input_text


chat = ChatGoogleGenerativeAI(model="gemini-pro")


user_input=get_text()
submit = st.button('Generate')  

if submit:
    
    try:
        response, messages = load_answer(user_input)
        st.subheader("Answer:")
        st.write(response)
    except:
        st.warning('Please provide your valid API key to continue')
    

    
    # st.write(messages)