import os
from dotenv import load_dotenv
from openai import OpenAI

# Load the API key from the .env file
load_dotenv()

# Initialize the OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

print("🤖 AI Bot Initialized! Type 'quit' to exit.\n")

# Start a simple conversation loop
while True:
    user_input = input("You: ")
    
    # Check if the user wants to exit
    if user_input.lower() == "quit":
        print("AI: Goodbye!")
        break

    try:
        # Send the user's message to the AI model
        response = client.chat.completions.create(
            model="gpt-4o-mini",  # A fast, cost-effective model ideal for beginners
            messages=[
                {"role": "system", "content": "You are a helpful, witty AI assistant."},
                {"role": "user", "content": user_input}
            ]
        )
        
        # Extract and print the reply from the AI
        ai_reply = response.choices[0].message.content
        print(f"\nAI: {ai_reply}\n")
        
    except Exception as e:
        print(f"\nAn error occurred: {e}\n")
