# chatbot.py
def simple_chatbot():
    print("Bot: Hi! I'm a simple chatbot. Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ").lower()
        
        if "hello" in user_input or "hi" in user_input:
            print("Bot: Hello there!")
        elif "how are you" in user_input:
            print("Bot: I'm just a bot, but thanks for asking!")
        elif "bye" in user_input:
            print("Bot: Goodbye! Have a nice day.")
            break
        else:
            print("Bot: I didn't understand that. Can you rephrase?")

# Run the chatbot
if __name__ == "__main__":
    simple_chatbot()