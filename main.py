# Task 1 : "Chatbot with rule-based Response":
# Build a simple chatbot that responds to user inputs based on
# predefined rules. Use if-else statements or pattern matching
# techniques to identify user queries and provide appropriate
# responses. This will give you a basic understanding of natural
# language processing and conversation flow.

import streamlit as st
from datetime import datetime

# Rule-based response logic
def chatbot_response(user_input):
    user_input = user_input.lower()

    if 'hello' in user_input or 'hi' in user_input:
        return "👋 Hello! How can I assist you today?"
    elif 'how are you' in user_input:
        return "😊 I'm just a bot, but I'm doing great! How about you?"
    elif 'your name' in user_input:
        return "🤖 I'm a simple chatbot created to assist you."
    elif 'what can you do' in user_input:
        return "🧠 I can respond to basic greetings and questions. Try asking me something!"
    elif 'bye' in user_input or 'goodbye' in user_input:
        return "👋 Goodbye! Have a great day!"
    elif 'time' in user_input:
        now = datetime.now()
        return f"⏰ The current time is {now.strftime('%H:%M:%S')}."
    elif 'date' in user_input:
        today = datetime.today()
        return f"📅 Today's date is {today.strftime('%Y-%m-%d')}."
    elif 'weather' in user_input:
        return "🌤️ I can't check the weather right now, but you can try a weather app or website!"
    elif 'joke' in user_input:
        return "😂 When does a joke become a 'dad' joke? When it becomes apparent."
    elif 'help' in user_input:
        return "🛠️ I can assist with basic questions like telling the time, date, or even a joke. Just ask!"
    elif 'your favorite color' in user_input:
        return "🎨 As a bot, I don't have preferences, but I think blue is quite nice!"
    elif 'hobby' in user_input:
        return "🎮 I enjoy helping people with their questions. What's your hobby?"
    else:
        return "❓ I'm sorry, I don't understand that. Can you rephrase?"

# Streamlit UI
st.set_page_config(page_title="Simple Chatbot", page_icon="🤖", layout="centered")

st.title("🤖 Rule-Based Chatbot")
st.write("Ask me anything! Type your message below.")

# Session state to store chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# User input
user_input = st.text_input("You:", key="input")

# Handle input
if user_input:
    response = chatbot_response(user_input)
    st.session_state.chat_history.append(("You", user_input))
    st.session_state.chat_history.append(("Bot", response))

# Display chat history
for sender, message in st.session_state.chat_history:
    if sender == "You":
        st.markdown(f"**🧑 You:** {message}")
    else:
        st.markdown(f"**🤖 Bot:** {message}")
