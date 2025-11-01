import streamlit as st
from dotenv import load_dotenv
from llm import get_ai_response

# Set up Streamlit app configuration
st.set_page_config(page_title="Korean Tax Chatbot", page_icon="🤖")


# App title and short description
st.title("🤖 Tax Chatbot")
st.caption("I will answer your questions about Korean taxes")


# Load environment variables (e.g., API keys)
load_dotenv()


# Initialize session state for conversation history
if 'message_list' not in st.session_state:
    st.session_state.message_list = []


# Display previous chat messages (conversation history)
print(f"before == {st.session_state.message_list}")
for message in st.session_state.message_list:
    with st.chat_message(message["role"]):
        st.write(message["content"])


# Optional tip or description above the chat input
st.caption("💡 Example: Try asking 'How much tax for a $50K salary?'")


# Handle user input and generate AI response
if user_question := st.chat_input(placeholder="Ask me anything about Korean taxes"):
    with st.chat_message("user"):
        st.write(user_question)
    st.session_state.message_list.append({"role": "user", "content": user_question})

    with st.spinner("In progress..."):
        ai_response = get_ai_response(user_question)
        with st.chat_message("ai"): 
            ai_message = st.write_stream(ai_response)
            st.session_state.message_list.append({"role": "ai", "content": ai_message})
