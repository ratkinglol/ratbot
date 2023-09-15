import random

# Define a dictionary of responses
responses = {
    "ok": ["Anything else I can help you with?", "Anything else?"],
    "hello": ["Hi there!", "Hello!", "Hey!"],
    "hi": ["Hi there!", "Hello!", "Hey!"],
    "how are u": ["I'm good, thanks!", "I'm doing well, how about you?", "I'm just a computer program, but I'm here to help."],
    "bye": ["Goodbye!", "See you later!", "Have a great day!"],
    "whats ur name": ["My name is RatBot.", "I'm just RatBot."],
    "who created u": ["I was created by Kasen F and Tristen R on https://github.com/ratkinglol/ratbot"],
    "tell me a joke": ["Why don't scientists trust atoms? Because they make up everything!", "Sure, here's a joke: What do you call a bear with no teeth? A gummy bear!"],
    "whats the weather like today": ["I'm sorry, I don't have access to real-time weather data.", "You can check the weather on a weather website or app."],
    "help": ["I can provide information and answer questions. Just ask me anything!", "How can I assist you today?"],
    "what is the capital of france": ["The capital of France is Paris.", "Paris is the capital of France."],
    "whats the capital of france": ["The capital of France is Paris.", "Paris is the capital of France."],
    "can u recommend a book": ["Certainly! I recommend 'The Hunger Games' by Suzanne Collins.", "How about reading 'To Kill a Mockingbird' by Harper Lee?"],
    "whats ur fav color": ["I don't have preferences, but I think purple is a nice color.", "I'm just a chatbot, so I don't have a favorite color."],
    "default": ["I'm not sure how to respond to that.", "Could you please rephrase your question?", "I don't understand."],
}



# History of past questions and their responses
question_history = {}


# Function to get a response based on user input with slang replacements
def get_response(user_input):
    # Apply slang replacements
    user_input = user_input.lower()
    user_input = user_input.replace("your", "ur")
    user_input = user_input.replace("you", "u")
    user_input = user_input.replace("don't", "dont")
    user_input = user_input.replace("what's", "whats")
    user_input = user_input.replace("favorite", "fav")
    # Check if the modified user input is in the responses dictionary
    response = responses.get(user_input, responses["default"])
    # Store the question and response in the history
    question_history[user_input] = response
    return random.choice(response)



# Function to run the chatbot
def run_chatbot():
    while True:
        user_input = input("You: ")
        if user_input.lower() == "bye":
            print("Chatbot: Goodbye! Have a great day!")
            break
        response = get_response(user_input)
        print("Chatbot:", response)



# Run the chatbot when the script is executed
if __name__ == "__main__":
    run_chatbot()

