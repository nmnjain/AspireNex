import random
responses = {
    "greetings": ["Hello! How can I assist you today?", "Hi! What's on your mind?", "Hey! How's it going?"],
    "goodbyes": ["Goodbye! It was nice chatting with you.", "See you later! Have a great day."],
    "introductions": ["I'm Chatty, your friendly chatbot!", "My name is Chatty, nice to meet you!"],
    "emotions": ["I'm doing great, thanks! How about you?", "I'm feeling happy today, thanks for asking!"],
    "unknown": ["I didn't understand that. Can you please rephrase?", "Sorry, I'm not sure what you mean. Can you explain?"],
    "thanks": ["You're welcome! It was my pleasure to assist you.", "No problem, happy to help!"]
}


def respond(user_input):
    user_input = user_input.lower()
    
    if "hello" in user_input or "hi" in user_input or "hey" in user_input:
        return random.choice(responses["greetings"])
    
    elif "bye" in user_input or "goodbye" in user_input or "see you later" in user_input:
        return random.choice(responses["goodbyes"])
    
    elif "what's your name" in user_input or "who are you" in user_input:
        return random.choice(responses["introductions"])
    
    elif "how are you" in user_input or "what's your mood" in user_input:
        return random.choice(responses["emotions"])
    
    elif "tell me a joke" in user_input or "make me laugh" in user_input:
        return random.choice(responses["jokes"])
    
    elif "help" in user_input or "what can you do" in user_input:
        return random.choice(responses["help"])
    
    elif "math" in user_input or "calculate" in user_input:
        return random.choice(responses["math"])

    elif "translate" in user_input or "language" in user_input:
        return random.choice(responses["language"])

    elif "thanks" in user_input or "thank you" in user_input:
        return random.choice(responses["thanks"])
    
    else:
        return random.choice(responses["unknown"])

print("Welcome to Chatty! Type 'quit' to exit.")
while True:
    user_input = input("You: ")
    response = respond(user_input)
    print("Chatty:", response)
    if "bye" in user_input or "goodbye" in user_input or "see you later" in user_input:
        break