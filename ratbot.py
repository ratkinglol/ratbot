import random

# Define a dictionary of responses
responses = {
    "hello": ["Hi there!", "Hello!", "Hey!"],
    "hi": ["Hi there!", "Hello!", "Hey!"],
    "how are you": ["I'm good, thanks!", "I'm doing well, how about you?", "I'm just a computer program, but I'm here to help."],
    "bye": ["Goodbye!", "See you later!", "Have a great day!"],
    "what's your name": ["My name is RatBot.", "I'm just RatBot."],
    "whats your name": ["My name is RatBot.", "I'm just RatBot."],
    "what's ur name": ["My name is RatBot.", "I'm just RatBot."],
    "whats ur name": ["My name is RatBot.", "I'm just RatBot."],
    "who created you": ["I was created by a team of developers.", "I don't have a single creator, I'm a product of collaboration."],
    "who created u": ["I was created by a team of developers.", "I don't have a single creator, I'm a product of collaboration."],
    "tell me a joke": ["Why don't scientists trust atoms? Because they make up everything!", "Sure, here's a joke: What do you call a bear with no teeth? A gummy bear!"],
    "what's the weather like today": ["I'm sorry, I don't have access to real-time weather data.", "You can check the weather on a weather website or app."],
    "whats the weather like today": ["I'm sorry, I don't have access to real-time weather data.", "You can check the weather on a weather website or app."],
    "help": ["I can provide information and answer questions. Just ask me anything!", "How can I assist you today?"],
    "what is the capital of France": ["The capital of France is Paris.", "Paris is the capital of France."],
    "can you recommend a book": ["Certainly! I recommend 'The Hunger Games' by Suzanne Collins.", "How about reading 'To Kill a Mockingbird' by Harper Lee?"],
    "can u recommend a book": ["Certainly! I recommend 'The Hunger Games' by Suzanne Collins.", "How about reading 'To Kill a Mockingbird' by Harper Lee?"],
    "what's your favorite color": ["I don't have preferences, but I think purple is a nice color.", "I'm just a chatbot, so I don't have a favorite color."],
    "whats your favorite color": ["I don't have preferences, but I think purple is a nice color.", "I'm just a chatbot, so I don't have a favorite color."],
    "whats ur favorite color": ["I don't have preferences, but I think purple is a nice color.", "I'm just a chatbot, so I don't have a favorite color."],
    "what's ur favorite color": ["I don't have preferences, but I think purple is a nice color.", "I'm just a chatbot, so I don't have a favorite color."],
    "default": ["I'm not sure how to respond to that.", "Could you please rephrase your question?", "I don't understand."],
}

# History of past questions and their responses
question_history = {}

# Function to get a response based on user input
def get_response(user_input):
    user_input = user_input.lower()
    response = responses.get(user_input, responses["default"])
    
    # Store the question and response in the history
    question_history[user_input] = response
    
    return random.choice(response)

# Main loop for chatbot interaction
print("Chatbot: Hi! I'm a simple chatbot. You can start the conversation. Type 'bye' to exit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == "bye":
        print("Chatbot: Goodbye! Have a great day!")
        break
    response = get_response(user_input)
    print("Chatbot:", response)

    # If the user asked a known question, recall and display its previous response
    if user_input.lower() in question_history:
        print("Chatbot (recalling):", question_history[user_input.lower()])

    # Handle "OK" or "cool" responses
    if user_input.lower() in ["ok", "cool"]:
        if "last_question" in question_history:
            print("Chatbot: Glad to hear that! You previously asked:", question_history["last_question"])
        else:
            print("Chatbot: Thanks for your response!")

    # Check if the user's input is a question for future reference
    if "?" in user_input:
        question_history["last_question"] = user_input