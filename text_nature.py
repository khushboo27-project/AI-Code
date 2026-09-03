from textblob import TextBlob

def analyze_sentiment(text):
    # Pass the text into the AI text processor
    blob = TextBlob(text)
    
    # The AI calculates polarity: -1.0 (very negative) to +1.0 (very positive)
    score = blob.sentiment.polarity
    
    # Classify the score into human-readable feelings
    if score > 0:
        return f"Positive Mood (Score: {score:.2f})"
    elif score < 0:
        return f"Negative Mood (Score: {score:.2f})"
    else:
        return f"Neutral Mood (Score: {score:.2f})"

# Main loop to chat with your AI
print("--- Your First AI Program is Ready! ---")
print("Type a sentence to let the AI read your mood. Type 'exit' to quit.")

while True:
    user_input = input("\nEnter text: ")
    if user_input.lower() == 'exit':
        print("Goodbye!")
        break
        
    result = analyze_sentiment(user_input)
    print(f"AI Analysis: {result}")
