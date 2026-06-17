print("Simple Chatbot")
print("Type 'bye' to stop\n")

while True:
    user = input("You: ").lower()

    if user == "hi":
        print("Bot: Hello!")

    elif user == "how are you":
        print("Bot: I am fine!")

    elif user == "what is your name":
        print("Bot: I am a chatbot.")

    elif user == "bye":
        print("Bot: Goodbye!")
        break

    else:
        print("Bot: I don't understand.")
