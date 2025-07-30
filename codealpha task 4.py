hellohdef chatbot():
    print("Chatbot: Hi! I'm your simple chatbot. Type 'bye' to exit.")
    while True:
        user_input = input("You: ").strip().lower()
        
        if user_input == "hello":
            print("Chatbot: Hi!")
        elif user_input == "how are you":
            print("Chatbot: I'm fine, thanks!")
        elif user_input == "bye":
            print("Chatbot: Goodbye!")
            break
        else:
            print("Chatbot: I'm sorry, I didn't understand that.")


chatbot()
