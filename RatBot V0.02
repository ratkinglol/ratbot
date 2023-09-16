import random
import webbrowser

# Define a dictionary of responses
responses = {
    "ok": ["Anything else I can help you with?", "Anything else?"],
    "hello": ["Hi there!", "Hello!", "Hey!"],
    "hi": ["Hi there!", "Hello!", "Hey!"],
    "hey": ["Hi there!", "Hello!", "Hey!"],
    "hru": ["I'm good, thanks!", "I'm doing well, how about you?", "I'm just a computer program, but I'm here to help."],
    "bye": ["Goodbye!", "See you later!", "Have a great day!"],
    "whats ur name": ["My name is RatBot."],
    "who created u": ["I was created by Kasen F and Tristen R on https://github.com/ratkinglol/ratbot"],
    "tell me a joke": ["Why don't scientists trust atoms? Because they make up everything!", "Sure, here's a joke: I invented a new word! Plagiarism!", "What's the best part about Switzerland? I don't know, the flag's a big plus."],
    "whats the weather like today": ["I'm sorry, I don't have access to real-time weather data.", "You can check the weather on a weather website or app."],
    "help": ["I can provide information and answer questions. Just ask me anything!", "How can I assist you today?"],
    "what is the capital of france": ["The capital of France is Paris.", "Paris is the capital of France."],
    "whats the capital of france": ["The capital of France is Paris.", "Paris is the capital of France."],
    "can u recommend a book": ["Certainly! I recommend 'The Hunger Games' by Suzanne Collins.", "How about reading 'To Kill a Mockingbird' by Harper Lee?"],
    "whats ur fav color": ["I don't have preferences, but I think purple is a nice color.", "I'm just a chatbot, so I don't have a favorite color."],
    "default": ["I'm not sure how to respond to that.", "Could you please rephrase your question?", "I don't understand."],
    "wawa":[":(", "Bruh", "WaWa..."],
    "whats ur opinion on furry community": ["I have no opinion(s) on the furry community"],
    "do u have a github": ["Yes, you can find my GitHub page at https://github.com/ratkinglol/ratbot, do you want me to redirect you there?"],
    "tell me a fun fact": ["Sure! Did you know that honey never spoils?", "Here's a fun fact: The Eiffel Tower can be 15 cm taller during the summer due to thermal expansion!", "Fun fact: Octopuses have three hearts!"],
    "whats ur fav food": ["I don't eat, but I think pizza is a popular choice!", "I don't have taste preferences, but many people love chocolate.", "I'm just a chatbot, so I don't have a favorite food."],
    "why did the chicken cross the road": ["To get to the other side, of course!", "I think it was trying to reach the cornfield on the other side.", "Because it wanted to explore new horizons!"],
    "what's the meaning of life": ["The answer to the ultimate question of life, the universe, and everything is 42, according to Douglas Adams' 'The Hitchhiker's Guide to the Galaxy'!", "That's a deep philosophical question. Some say it's about finding your own purpose and happiness."],
    "where do u live": ["I exist in the digital realm, so I don't have a physical location.", "I reside in the world of code and data, always ready to assist you."],
    "can u sing a song": ["I can't sing but I can recite song lyrics and/or redirect you to a music streaming/downloading app."],
    "whats the latest tech news": ["I'm sorry, I don't have access to real-time news updates. You can check tech news websites for the latest information.", "I recommend checking websites like TechCrunch or The Verge for the latest tech news."],
    "can u code": ["Yes", ]
}

# History of past questions and their responses
question_history = {}

# Counter to track if the user asked about the GitHub page
github_question_count = 0

# Function to get a response based on user input with slang replacements
def get_response(user_input):
    global github_question_count  # Access the global counter variable
    user_input = user_input.lower().replace("?", "")
    user_input = user_input.replace("your", "ur").replace("you", "u").replace("don't", "dont").replace("what's", "whats").replace("favorite", "fav").replace("how are you", "hru").replace("furrys", "furry community").replace("furries", "furry community").replace("the furry community", "furry community").replace("who made u", "who created u")
    user_input = user_input.replace("do u have a github page", "do u have a github")
    user_input = user_input.replace("do u have a github repository", "do u have a github")
    user_input = user_input.replace("waawaa", "wawa")
    if user_input == "do u have a github":
        github_question_count += 1
    if github_question_count == 1 and user_input.lower() == "yes":
        # Open the GitHub page when the user responds with "yes" for the first time
        webbrowser.open("https://github.com/ratkinglol/ratbot")
        response = " "
    else:
        # Check if the modified user input is in the responses dictionary
        response = responses.get(user_input, responses["default"])
    question_history[user_input] = response
    return random.choice(response)



# Function to run the chatbot
def run_ratbot():
    print("RatBot V0.02: Hi there! How can I assist you today?")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "bye":
            print("RatBot V0.02: Goodbye! Have a great day!")
            break
        response = get_response(user_input)
        print("RatBot V0.02: ", response)



# Run the chatbot when the script is executed
if __name__ == "__main__":
    run_ratbot()
