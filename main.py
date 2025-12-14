
import os
import random
from dotenv import load_dotenv
from scenarios import SCENARIOS
from interview import InterviewSession

def main():
    """
    The main function of the application.
    """
    # Load environment variables from a .env file
    load_dotenv()

    # Check for the API key
    if not os.getenv("GOOGLE_API_KEY"):
        print("Error: GOOGLE_API_KEY environment variable not set.")
        print("Please create a .env file and add your API key to it.")
        return

    print("Welcome to the Managerial Behavioral Interview Tool!")
    print("=" * 50)
    print("This tool will help you practice for behavioral interviews.")
    print("You will be presented with a scenario, and an AI interviewer will ask you follow-up questions.")
    print("The goal is to practice structuring your answers using the STAR method.")
    print("=" * 50)

    while True:
        print("\nMain Menu:")
        print("1. Start a new interview")
        print("2. Exit")

        choice = input("> ")

        if choice == '1':
            # Select a random scenario
            scenario = random.choice(SCENARIOS)
            
            # Create and start the interview session
            session = InterviewSession(scenario)
            session.start()

        elif choice == '2':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
