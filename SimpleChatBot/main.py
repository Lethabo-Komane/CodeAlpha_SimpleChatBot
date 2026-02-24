def chatbot():
    print("Chatbot: Hello! Welcome to LeeWorld. Type 'bye' to exit.")

    while True:
        user_input = input("You: ").lower()

        if user_input == "hi" or user_input == "hello":
            print("Chatbot: Hello there! How can I help you?")
        elif "how are you" in user_input:
            print("Chatbot: I'm fine,thanks!How are you?")
        elif "good" in user_input:
            print("Great,what can I help you with today?")
        elif "who are you" in user_input:
            print("Chatbot: I'm LeeBot, your friendly chatbot!")
        elif "help" in user_input:
            print("Chatbot: Sure! You can ask me things like 'how are you', 'who are you', etc.")
        elif "what is python" in user_input:
            print("Chatbot: Python is a powerful programming language used for many types of software.")

        elif user_input == "bye":
            print("Chatbot: Goodbye! Have a nice day!")
            break
        else:
            print("Chatbot: Sorry, I don't understand that yet.")

# Run the chatbot
if __name__ == "__main__":
    chatbot()
    
