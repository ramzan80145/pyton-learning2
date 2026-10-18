chat_history = []


def get_ai_response(messages):
    last_user_message = messages[-1]["content"]

    if "hello" in last_user_message.lower():
        return "Hello! I am your AI assistant"
    elif "name" in last_user_message.lower():
        return "I am a Python program created by Ramzan"
    else:
        return f"you said: '{last_user_message}'. that's interesting!"


print("fake AI: Hello! type 'quit' to exit.")

while True:
    user_input = input("/nyou:")
    if user_input.lower() == "quit":
        break

    chat_history.append({"role": "user", "content": user_input})
    response = get_ai_response(chat_history)
    print(f"AI: {response}")
    chat_history.append({"role": "assistant", "content": response})


