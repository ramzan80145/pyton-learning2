messages = [
    {"role": "user", "content": "Hello AI!"},
    {"role": "assistant", "content": "Hello Ramzan! How can I help?"}
]

for msg in messages:
    print(f"[{msg['role']}]: {msg['content']}")