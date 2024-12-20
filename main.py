from textblob import TextBlob
import colorama
from colorama import Fore, Style
import sys
import time

colorama.init(autoreset=True)

user_name=""
conversation_history=[]

positive_count=0
negative_count=0
natural_count=0

def show_processing_animation():
    print(f"{Fore.CYAN}Detecting sentiment clues", end="")
    for _ in range(3):
        time.sleep(0.5)
        print(".",end="")
        sys.stdout.flush()


def analyse_sentiment(text):
    """
    Analyzes the sentiment of the input text using TextBlob.
    Categories:
    - Positive: Polarity > 0.25
    - Neutral: Polarity between -0.25 and 0.25
    - Negative: Polarity < -0.25
    """
    global positive_count, negative_count, neutral_count

    try:
        blob=TextBlob(text)
        sentiment=blob.sentiment.polarity
        conversation_history.append(text)

        if sentiment>0.75:
            positive_count+=1
            return f"\n{Fore.GREEN} Very Positive sentiment detected, Agent{user_name}! (Score:{sentiment:.2f}) "
        elif -0.25 <= sentiment <= 0.25:
            neutral_count += 1  # Increment neutral counter
            return f"\n{Fore.YELLOW}😐 Neutral sentiment detected."
        elif -0.75 <= sentiment < -0.25:
            negative_count += 1  # Increment negative counter
            return f"\n{Fore.RED}💔 Negative sentiment detected, Agent {user_name}. (Score: {sentiment:.2f})"
        else:
            negative_count += 1  # Increment negative counter
            return f"\n{Fore.RED}💔 Very Negative sentiment detected, Agent {user_name}. (Score: {sentiment:.2f})"

    except Exception as e:
        # Handles any errors that might occur during sentiment analysis
        return f"{Fore.RED}An error occurred during sentiment analysis: {str(e)}"
    
def execute_command(command):
    """
    Executes predefined commands:
    - 'summary': Displays sentiment statistics
    - 'reset': Clears conversation history and counters
    - 'history': Shows all user inputs
    - 'help': Lists available commands
    """
    global conversation_history, positive_count, negative_count, neutral_count

    if command == "summary":
        # Display a summary of sentiment analysis results
        return (f"{Fore.CYAN}🕵️ Mission Report:\n"
                f"{Fore.GREEN}Positive messages detected: {positive_count}\n"
                f"{Fore.RED}Negative messages detected: {negative_count}\n"
                f"{Fore.YELLOW}Neutral messages detected: {neutral_count}")
    elif command == "reset":
        # Clear all data
        conversation_history.clear()
        positive_count = negative_count = neutral_count = 0  # Reset counters
        return f"{Fore.CYAN}🕵️ Mission reset! All previous data has been cleared."
    elif command == "history":
        # Show all previous inputs and sentiments
        return "\n".join([f"{Fore.CYAN}Message {i+1}: {msg}" for i, msg in enumerate(conversation_history)]) \
               if conversation_history else f"{Fore.YELLOW}No conversation history available."
    elif command == "help":
        # Display a list of available commands
        return (f"{Fore.CYAN}🔍 Available commands:\n"
                f"- Type any sentence to analyze its sentiment.\n"
                f"- Type 'summary' to get a mission report on analyzed sentiments.\n"
                f"- Type 'reset' to clear all mission data and start fresh.\n"
                f"- Type 'history' to view all previous messages and analyses.\n"
                f"- Type 'exit' to conclude your mission and leave the chat.")
    else:
        # Handle unknown commands
        return f"{Fore.RED}Unknown command. Type 'help' for a list of commands."

# Function to validate and retrieve the user's name
def get_valid_name():
    """
    Continuously prompts the user until they provide a valid name containing only alphabetic characters.
    """
    while True:
        name = input("What’s your name? ").strip()  # Get user input and remove extra spaces
        if name and name.isalpha():  # Ensure the name is non-empty and alphabetic
            return name
        else:
            print(f"{Fore.RED}Please enter a valid name with only alphabetic characters.")

# Main function to start the sentiment analysis chat
def start_sentiment_chat():
    """
    Main loop for interacting with the Sentiment Spy chatbot. Users can:
    - Analyze the sentiment of sentences
    - Use commands like 'help', 'summary', and 'reset'
    - Exit the chat anytime
    """
    print(f"{Fore.CYAN}{Style.BRIGHT}🕵️ Welcome to Sentiment Spy! Your personal emotion detective is here. 🎉")

    # Retrieve and store the user's name
    global user_name
    user_name = get_valid_name()
    print(f"\n{Fore.CYAN}Nice to meet you, Agent {user_name}! Type your sentences to analyze emotions. Type 'help' for options.")

    while True:
        # Get user input
        user_input = input(f"\n{Fore.MAGENTA}{Style.BRIGHT}Agent {user_name}: {Style.RESET_ALL}").strip()

        if not user_input:  # Handle empty input
            print(f"{Fore.RED}Please enter a non-empty message or type 'help' for available commands.")
            continue

        if user_input.lower() == 'exit':  # Exit the program
            print(f"\n{Fore.BLUE}🔚 Mission complete! Exiting Sentiment Spy. Farewell, Agent {user_name}!")
            print(execute_command("summary"))  # Display final summary
            break
        elif user_input.lower() in ["summary", "reset", "history", "help"]:  # Handle special commands
            print(execute_command(user_input.lower()))
        else:
            # Simulate processing animation and analyze sentiment
            show_processing_animation()
            result = analyze_sentiment(user_input)
            print(result)

# Function to handle special commands like 'summary', 'reset', 'history', and 'help'
def execute_command(command):
    """
    Executes predefined commands:
    - 'summary': Displays sentiment statistics
    - 'reset': Clears conversation history and counters
    - 'history': Shows all user inputs
    - 'help': Lists available commands
    """
    global conversation_history, positive_count, negative_count, neutral_count

    if command == "summary":
        # Display a summary of sentiment analysis results
        return (f"{Fore.CYAN}🕵️ Mission Report:\n"
                f"{Fore.GREEN}Positive messages detected: {positive_count}\n"
                f"{Fore.RED}Negative messages detected: {negative_count}\n"
                f"{Fore.YELLOW}Neutral messages detected: {neutral_count}")
    elif command == "reset":
        # Clear all data
        conversation_history.clear()
        positive_count = negative_count = neutral_count = 0  # Reset counters
        return f"{Fore.CYAN}🕵️ Mission reset! All previous data has been cleared."
    elif command == "history":
        # Show all previous inputs and sentiments
        return "\n".join([f"{Fore.CYAN}Message {i+1}: {msg}" for i, msg in enumerate(conversation_history)]) \
               if conversation_history else f"{Fore.YELLOW}No conversation history available."
    elif command == "help":
        # Display a list of available commands
        return (f"{Fore.CYAN}🔍 Available commands:\n"
                f"- Type any sentence to analyze its sentiment.\n"
                f"- Type 'summary' to get a mission report on analyzed sentiments.\n"
                f"- Type 'reset' to clear all mission data and start fresh.\n"
                f"- Type 'history' to view all previous messages and analyses.\n"
                f"- Type 'exit' to conclude your mission and leave the chat.")
    else:
        # Handle unknown commands
        return f"{Fore.RED}Unknown command. Type 'help' for a list of commands."

# Function to validate and retrieve the user's name
def get_valid_name():
    """
    Continuously prompts the user until they provide a valid name containing only alphabetic characters.
    """
    while True:
        name = input("What’s your name? ").strip()  # Get user input and remove extra spaces
        if name and name.isalpha():  # Ensure the name is non-empty and alphabetic
            return name
        else:
            print(f"{Fore.RED}Please enter a valid name with only alphabetic characters.")

# Main function to start the sentiment analysis chat
def start_sentiment_chat():
    """
    Main loop for interacting with the Sentiment Spy chatbot. Users can:
    - Analyze the sentiment of sentences
    - Use commands like 'help', 'summary', and 'reset'
    - Exit the chat anytime
    """
    print(f"{Fore.CYAN}{Style.BRIGHT}🕵️ Welcome to Sentiment Spy! Your personal emotion detective is here. 🎉")

    # Retrieve and store the user's name
    global user_name
    user_name = get_valid_name()
    print(f"\n{Fore.CYAN}Nice to meet you, Agent {user_name}! Type your sentences to analyze emotions. Type 'help' for options.")

    while True:
        # Get user input
        user_input = input(f"\n{Fore.MAGENTA}{Style.BRIGHT}Agent {user_name}: {Style.RESET_ALL}").strip()

        if not user_input:  # Handle empty input
            print(f"{Fore.RED}Please enter a non-empty message or type 'help' for available commands.")
            continue

        if user_input.lower() == 'exit':  # Exit the program
            print(f"\n{Fore.BLUE}🔚 Mission complete! Exiting Sentiment Spy. Farewell, Agent {user_name}!")
            print(execute_command("summary"))  # Display final summary
            break
        elif user_input.lower() in ["summary", "reset", "history", "help"]:  # Handle special commands
            print(execute_command(user_input.lower()))
        else:
            # Simulate processing animation and analyze sentiment
            show_processing_animation()
            result = analyze_sentiment(user_input)
            print(result)

def execute_command(command):
    """
    Executes predefined commands:
    - 'summary': Displays sentiment statistics
    - 'reset': Clears conversation history and counters
    - 'history': Shows all user inputs
    - 'help': Lists available commands
    """
    global conversation_history, positive_count, negative_count, neutral_count

    if command == "summary":
        # Display a summary of sentiment analysis results
        return (f"{Fore.CYAN}🕵️ Mission Report:\n"
                f"{Fore.GREEN}Positive messages detected: {positive_count}\n"
                f"{Fore.RED}Negative messages detected: {negative_count}\n"
                f"{Fore.YELLOW}Neutral messages detected: {neutral_count}")
    elif command == "reset":
        # Clear all data
        conversation_history.clear()
        positive_count = negative_count = neutral_count = 0  # Reset counters
        return f"{Fore.CYAN}🕵️ Mission reset! All previous data has been cleared."
    elif command == "history":
        # Show all previous inputs and sentiments
        return "\n".join([f"{Fore.CYAN}Message {i+1}: {msg}" for i, msg in enumerate(conversation_history)]) \
               if conversation_history else f"{Fore.YELLOW}No conversation history available."
    elif command == "help":
        # Display a list of available commands
        return (f"{Fore.CYAN}🔍 Available commands:\n"
                f"- Type any sentence to analyze its sentiment.\n"
                f"- Type 'summary' to get a mission report on analyzed sentiments.\n"
                f"- Type 'reset' to clear all mission data and start fresh.\n"
                f"- Type 'history' to view all previous messages and analyses.\n"
                f"- Type 'exit' to conclude your mission and leave the chat.")
    else:
        # Handle unknown commands
        return f"{Fore.RED}Unknown command. Type 'help' for a list of commands."

# Function to validate and retrieve the user's name
def get_valid_name():
    """
    Continuously prompts the user until they provide a valid name containing only alphabetic characters.
    """
    while True:
        name = input("What’s your name? ").strip()  # Get user input and remove extra spaces
        if name and name.isalpha():  # Ensure the name is non-empty and alphabetic
            return name
        else:
            print(f"{Fore.RED}Please enter a valid name with only alphabetic characters.")

# Main function to start the sentiment analysis chat
def start_sentiment_chat():
    """
    Main loop for interacting with the Sentiment Spy chatbot. Users can:
    - Analyze the sentiment of sentences
    - Use commands like 'help', 'summary', and 'reset'
    - Exit the chat anytime
    """
    print(f"{Fore.CYAN}{Style.BRIGHT}🕵️ Welcome to Sentiment Spy! Your personal emotion detective is here. 🎉")

    # Retrieve and store the user's name
    global user_name
    user_name = get_valid_name()
    print(f"\n{Fore.CYAN}Nice to meet you, Agent {user_name}! Type your sentences to analyze emotions. Type 'help' for options.")

    while True:
        # Get user input
        user_input = input(f"\n{Fore.MAGENTA}{Style.BRIGHT}Agent {user_name}: {Style.RESET_ALL}").strip()

        if not user_input:  # Handle empty input
            print(f"{Fore.RED}Please enter a non-empty message or type 'help' for available commands.")
            continue

        if user_input.lower() == 'exit':  # Exit the program
            print(f"\n{Fore.BLUE}🔚 Mission complete! Exiting Sentiment Spy. Farewell, Agent {user_name}!")
            print(execute_command("summary"))  # Display final summary
            break
        elif user_input.lower() in ["summary", "reset", "history", "help"]:  # Handle special commands
            print(execute_command(user_input.lower()))
        else:
            # Simulate processing animation and analyze sentiment
            show_processing_animation()
            result = analyze_sentiment(user_input)
            print(result)

def execute_command(command):
    """
    Executes predefined commands:
    - 'summary': Displays sentiment statistics
    - 'reset': Clears conversation history and counters
    - 'history': Shows all user inputs
    - 'help': Lists available commands
    """
    global conversation_history, positive_count, negative_count, neutral_count

    if command == "summary":
        # Display a summary of sentiment analysis results
        return (f"{Fore.CYAN}🕵️ Mission Report:\n"
                f"{Fore.GREEN}Positive messages detected: {positive_count}\n"
                f"{Fore.RED}Negative messages detected: {negative_count}\n"
                f"{Fore.YELLOW}Neutral messages detected: {neutral_count}")
    elif command == "reset":
        # Clear all data
        conversation_history.clear()
        positive_count = negative_count = neutral_count = 0  # Reset counters
        return f"{Fore.CYAN}🕵️ Mission reset! All previous data has been cleared."
    elif command == "history":
        # Show all previous inputs and sentiments
        return "\n".join([f"{Fore.CYAN}Message {i+1}: {msg}" for i, msg in enumerate(conversation_history)]) \
               if conversation_history else f"{Fore.YELLOW}No conversation history available."
    elif command == "help":
        # Display a list of available commands
        return (f"{Fore.CYAN}🔍 Available commands:\n"
                f"- Type any sentence to analyze its sentiment.\n"
                f"- Type 'summary' to get a mission report on analyzed sentiments.\n"
                f"- Type 'reset' to clear all mission data and start fresh.\n"
                f"- Type 'history' to view all previous messages and analyses.\n"
                f"- Type 'exit' to conclude your mission and leave the chat.")
def execute_command(command):
    """
    Executes predefined commands:
    - 'summary': Displays sentiment statistics
    - 'reset': Clears conversation history and counters
    - 'history': Shows all user inputs
    - 'help': Lists available commands
    """
    global conversation_history, positive_count, negative_count, neutral_count

    if command == "summary":
        # Display a summary of sentiment analysis results
        return (f"{Fore.CYAN}🕵️ Mission Report:\n"
                f"{Fore.GREEN}Positive messages detected: {positive_count}\n"
                f"{Fore.RED}Negative messages detected: {negative_count}\n"
                f"{Fore.YELLOW}Neutral messages detected: {neutral_count}")
    elif command == "reset":
        # Clear all data
        conversation_history.clear()
        positive_count = negative_count = neutral_count = 0  # Reset counters
        return f"{Fore.CYAN}🕵️ Mission reset! All previous data has been cleared."
    elif command == "history":
        # Show all previous inputs and sentiments
        return "\n".join([f"{Fore.CYAN}Message {i+1}: {msg}" for i, msg in enumerate(conversation_history)]) \
               if conversation_history else f"{Fore.YELLOW}No conversation history available."
    elif command == "help":
        # Display a list of available commands
        return (f"{Fore.CYAN}🔍 Available commands:\n"
                f"- Type any sentence to analyze its sentiment.\n"
                f"- Type 'summary' to get a mission report on analyzed sentiments.\n"
                f"- Type 'reset' to clear all mission data and start fresh.\n"
                f"- Type 'history' to view all previous messages and analyses.\n"
                f"- Type 'exit' to conclude your mission and leave the chat.")
    else:
        # Handle unknown commands
        return f"{Fore.RED}Unknown command. Type 'help' for a list of commands."
def get_valid_name():
    """
    Continuously prompts the user until they provide a valid name containing only alphabetic characters.
    """
    while True:
        name = input("What’s your name? ").strip()  # Get user input and remove extra spaces
        if name and name.isalpha():  # Ensure the name is non-empty and alphabetic
            return name
        else:
            print(f"{Fore.RED}Please enter a valid name with only alphabetic characters.")
# Main function to start the sentiment analysis chat
def start_sentiment_chat():
    """
    Main loop for interacting with the Sentiment Spy chatbot. Users can:
    - Analyze the sentiment of sentences
    - Use commands like 'help', 'summary', and 'reset'
    - Exit the chat anytime
    """
    print(f"{Fore.CYAN}{Style.BRIGHT}🕵️ Welcome to Sentiment Spy! Your personal emotion detective is here. 🎉")

    # Retrieve and store the user's name
    global user_name
    user_name = get_valid_name()
    print(f"\n{Fore.CYAN}Nice to meet you, Agent {user_name}! Type your sentences to analyze emotions. Type 'help' for options.")

    while True:
        # Get user input
        user_input = input(f"\n{Fore.MAGENTA}{Style.BRIGHT}Agent {user_name}: {Style.RESET_ALL}").strip()

        if not user_input:  # Handle empty input
            print(f"{Fore.RED}Please enter a non-empty message or type 'help' for available commands.")
            continue

        if user_input.lower() == 'exit':  # Exit the program
            print(f"\n{Fore.BLUE}🔚 Mission complete! Exiting Sentiment Spy. Farewell, Agent {user_name}!")
            print(execute_command("summary"))  # Display final summary
            break
        elif user_input.lower() in ["summary", "reset", "history", "help"]:  # Handle special commands
            print(execute_command(user_input.lower()))
        else:
            # Simulate processing animation and analyze sentiment
            show_processing_animation()
            result= analyze_sentiment(user_input)
            print(result)

if __name__ == "__main__":
    start_sentiment_chat()  # Start the Sentiment Spy chat




