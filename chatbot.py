import random

# Enhanced chatbot with more responses and dynamic interaction
def chatbot_response(user_input):
    responses = {
        "hello": ["Hi there! How can I assist you today?", "Hello! What can I do for you?"],
        "bye": ["Goodbye! Have a great day!", "See you later!"],
        "help": ["I'm here to help! What do you need assistance with?", "How can I assist you?"]
    }
    
    # Lowercase the user input for case-insensitive matching
    user_input = user_input.lower()
    
    # Check if the user input matches any predefined responses
    if user_input in responses:
        return random.choice(responses[user_input])
    else:
        return "I'm sorry, I didn't understand that. Could you please rephrase?"

# Example interaction
user_input = input("You: ")
print("Chatbot:", chatbot_response(user_input))
