print("Script started")

def get_response(user_input):
    user_input = user_input.lower()
    
    if "hello" in user_input or "hi" in user_input:
        return "Hello there! How can I assist you today?"
    elif "how are you" in user_input:
        return "I'm just a simple chatbot made for my internship project, but thanks for asking!"
    elif "what is your name" in user_input:
        return "I'm a rule based chatbot made for your assitance."
    elif "bye" in user_input or "exit" in user_input or "quit" in user_input or "goodbye" in user_input:
        return "Goodbye! Have a great day!"
    else: 
        return "I'm sorry, I dont understand. Can you please rephrase?"

def main():
    print("Welcome to the Rule-Based Chatbot! Type 'exit', 'quit', or 'goodbye' to end the conversation.")
    
    while True:
        user_input = input("You:")
        if user_input.lower() == "bye" or user_input.lower() == "exit" or user_input.lower() == "quit" or user_input.lower() == "goodbye":
            print("Chatbot: Goodbye! Have a great day!")
            break
        response = get_response(user_input)
        print("Chatbot:", response)
        
        
if __name__ == "__main__":
    main()