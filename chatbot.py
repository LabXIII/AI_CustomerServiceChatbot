def chatbot_response(user_input):
    # Simple response logic for demonstration
    responses = {
        "hello": "Hi there! How can I assist you today?",
        "bye": "Goodbye! Have a great day!",
        "help": "I'm here to help! What do you need assistance with?"
    }
    return responses.get(user_input.lower(), "I'm sorry, I didn't understand that.")

# Example interaction
user_input = input("You: ")
print("Chatbot:", chatbot_response(user_input))
