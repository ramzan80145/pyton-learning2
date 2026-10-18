import streamlit as st
import google.generativeai as genai

# 1. Configure the AI
API_KEY = st.secrets["GEMINI_API_KEY"]
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-3.5-flash")

# 2. Set up the page title and layout
st.set_page_config(page_title="My AI Chatbot", page_icon="🤖")
st.title("🤖 Ramzan's AI Chatbot")
st.caption("Built with Python, Gemini, and Streamlit")

# 3. Initialize chat history in the session
if "messages" not in st.session_state:
    st.session_state.messages = []

# 4. Display all past messages from the history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 5. The Chat Input box at the bottom
if prompt := st.chat_input("Ask me anything..."):
    
    # Display the user's message immediately
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Add user message to history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Get the AI response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = model.generate_content(prompt)
            st.markdown(response.text)
            
    # Add AI response to history
    st.session_state.messages.append({"role": "assistant", "content": response.text})