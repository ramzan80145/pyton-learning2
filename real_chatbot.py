import google.generativeai as genai

# 1. Put your API key inside the quotes below:
API_KEY = "PASTE_YOUR_KEY_HERE"

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-3.5-flash")# 2. Choose the AI model

# 3. The Chat Loop
print("🤖 Real Gemini AI: Hello Ramzan! Type 'quit' to exit.")

while True:
    user_input = input("\nYou: ")
    
    if user_input.lower() == "quit":
        print("🤖 AI: Goodbye!")
        break
    
    print("🤖 AI is thinking...")
    
    # Send the message to Google and get the response
    response = model.generate_content(user_input)
    
    print(f"🤖 AI: {response.text}")

