from flask import Flask, request, jsonify, render_template
import random

app = Flask(__name__)

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

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.form['message']
    response = chatbot_response(user_input)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
