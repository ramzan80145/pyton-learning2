# 1. The list to store our conversation
chat_history = []

# 2. A fake AI function (we'll replace this with the real AI later)
def get_ai_response(messages):
    # For now, we just look at the last message the user sent
    last_user_message = messages[-1]["content"]
    
    # We make up a reply based on what they said
    if "hello" in last_user_message.lower():
        return "Hello! I am your AI assistant."
    elif "name" in last_user_message.lower():
        return "I am a Python program created by Ramzan."
    else:
        return f"You said: '{last_user_message}'. That's interesting!"

# 3. The main chat loop
print("🤖 Fake AI: Hello! Type 'quit' to exit.")

while True:
    # Get user input
    user_input = input("\nYou: ")
    
    # Exit condition
    if user_input.lower() == "quit":
        print("🤖 Fake AI: Goodbye!")
        break
    
    # Add user message to history (using the exact format AI uses)
    chat_history.append({"role": "user", "content": user_input})
    
    # Get the "AI" response
    response = get_ai_response(chat_history)
    
    # Print the response
    print(f"🤖 Fake AI: {response}")
    
    # Add AI response to history
    chat_history.append({"role": "assistant", "content": response})