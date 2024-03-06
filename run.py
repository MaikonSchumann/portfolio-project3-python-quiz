# Import libraries
import colorama
from colorama import Fore, Style
import pyfiglet
from pyfiglet import figlet_format
import time
import gspread
from google.oauth2.service_account import Credentials
import random

# Scopes for accessing credentials from Google Cloud

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

# Scopes for accessing credentials from Google Cloud
CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD.open("PythonQuizDatabase")

# setting a variable to a specific google worksheet
questions = SHEET.worksheet('questions')
history = SHEET.worksheet('history')

# Available user choices
choices = ["a", "b", "c", "d"]

username = ''


def separator():
    """
    Display a separator line
    """
    print()
    print(f'{Fore.CYAN}-' * 60)
    print(f'{Fore.CYAN}-' * 60 + '\n' + Style.RESET_ALL)


def clear():
    """
    Clears the terminal

    Credits:
    https://stackoverflow.com/questions/29887629/how-to-clear-terminal-mac-osx-scrollback/29887659#29887659
    """
    print('\033c')


def game_rules():

    """
    Displays the game rules to the user.

    Explains the quiz format: friendly multiple-choice questions.
    Instructs users to answer by typing 'a', 'b', 'c', or 'd'
    and pressing 'Enter'.
    Emphasizes the simplicity of the process.

    """
    separator()
    print('Have some fun testing your Python skills with friendly multiple-choice questions!\n')
    print(f"Answer each question by typing {Fore.CYAN}(a, b, c, or d)" + Style.RESET_ALL + " and then press 'Enter'.\n")
    print('Easy as that!\n')
    time.sleep(1)
    print('Are you ready?\n')
    time.sleep(1)
    print("Let's rock!\n")
    time.sleep(1)
    print("Good luck!")
    separator()
    time.sleep(5)
    clear()


def get_user_name():

    """
    Obtains the username from the user input.

    - Prompts the user to enter their username.
    - Stores the username in a global variable for accessibility.
    - Returns the entered username.

    """
    global username  # Access the global variable for username
    username = input('Hey, please enter your username:\n')
    return username


def welcome_screen():
    """
    Displays the welcome screen for the Python Quiz game.

    Prints a starting message, waits briefly for effect, and showcases an artistic title.
    Captures the user's name and provides a personalized welcome message.

    """
    separator()
    print('Starting the ultimate Python Quiz game..\n')
    time.sleep(2)
    separator()

    # Artistic representation of the game title.
    art = figlet_format("Python Quiz", font='doom')
    print(Fore.CYAN + art + Style.RESET_ALL)
    separator()

    # Capture the user's name and offer a personalized welcome.
    user_name = get_user_name()
    print(f'Welcome to the Python Quiz game {Fore.CYAN}{user_name.capitalize()}!\n' + Style.RESET_ALL)


def verify_input():
    """
    Validates user input for a quiz answer.

    - Prompts the user to choose an answer.
    - Ensures the input is one of the valid choices: 'a', 'b', 'c', or 'd'.
    - Returns the valid answer or displays an error message and prompts for input again.

    """
    choices = ['a', 'b', 'c', 'd']

    while True:
        try:
            answer = input('Choose your answer:\n').lower()

            if answer in choices:
                return answer
            else:
                raise ValueError(f'Invalid input! Choose a valid option: {Fore.CYAN}a, b, c, or d{Style.RESET_ALL}!\n')

        except ValueError as ve:
            print(ve)


def show_score(correct_answers, wrong_answers):
    """
    Display the current quiz play score to the user.

    Parameters:
    - correct_answers (int): Number of correct answers in the quiz.
    - wrong_answers (int): Number of incorrect answers in the quiz.
    """

    if correct_answers >= 7:
        separator()
        print('Well done, you are really into Python!')
        print(f"You got {Fore.GREEN}{correct_answers} correct answers{Style.RESET_ALL}, that's very good!")
        print(f'Only got {Fore.RED}{wrong_answers} wrong answers{Style.RESET_ALL} this time.')

    elif correct_answers <= 4:
        separator()
        print('Hmm, not quite there yet. Consider putting in some more study time and giving it another shot!')
        print(f'Only got {Fore.GREEN}{correct_answers} correct answers{Style.RESET_ALL} this time.')
        print(f'And then you got {Fore.RED}{wrong_answers} wrong answers{Style.RESET_ALL}.')

    else:
        separator()
        print('Not bad, but you can do better!')
        print(f'You got {Fore.GREEN}{correct_answers} correct answers{Style.RESET_ALL} with {Fore.RED}{wrong_answers} wrong answers{Style.RESET_ALL}.')


def user_history(username, correct_answer, wrong_answer):
    """
    Append user's quiz history to the 'history' sheet.

    Parameters:
    - username (str): User's name.
    - correct_answer (int): Count of correct answers.
    - wrong_answer (int): Count of incorrect answers.
    """
    history.append_row([username.capitalize(), correct_answer, wrong_answer])


def quiz():
    """
    Run the quiz, displaying questions and scoring.

    - Randomly selects questions from a database.
    - Prompts user input to guess answers.
    - Tracks correct and wrong answers, showing partial scores after each question.
    - Displays the final score at the end of the quiz.
    - Appends the final score to the 'history' sheet.

    Credits to unpacking the questions:
    https://stackoverflow.com/questions/36901/what-does-double-star-asterisk-and-star-asterisk-do-for-parameters/36908#36908

    """

    # Import answers from the database
    answers = questions.get("F2:F31")

    # Initialize scores
    correct_answers = 0
    wrong_answers = 0

    x = 0
    while x < 10:
        separator()

        # Generate a random number to select a question from the database
        random_num_question = random.randint(0, 29)

        # Retrieve the current answer from the database
        current_answer = str(answers[random_num_question])

        # Format the answer string (remove '[]' and quotes)
        current_answer_formatted = current_answer.strip("[]").replace("'", "")

        # Retrieve the current question from the database
        row = questions.row_values(random_num_question + 2)

        # Print user name and current score
        print(f"{username.capitalize()}'s Score:")
        print(f'Correct answers: {Fore.GREEN} {correct_answers} {Style.RESET_ALL} | Wrong answers: {Fore.RED} {wrong_answers} {Style.RESET_ALL}\n')

        # Remove the answer column to show the question to the user
        question = row[:-1]

        # Print the current question to the user
        print(f'{x + 1}º Question:\n')
        print(*question, sep='\n')
        x += 1
        separator()

        # Ask the user to guess the answer and verify the input
        guess = verify_input()

        # Check if the answer is correct and update the scores
        if guess == current_answer_formatted:
            print(f'Well done! Your answer is {Fore.GREEN}correct{Style.RESET_ALL}!')
            correct_answers += 1
            time.sleep(2)
        else:
            # Display a message for incorrect answers, show the correct answer, and update the scores
            print(f'Oops! Your answer is {Fore.RED}incorrect{Style.RESET_ALL}.')
            print(f'The correct answer is option: {Fore.GREEN}{current_answer_formatted}{Style.RESET_ALL}')
            wrong_answers += 1
            time.sleep(3)

        clear()

    # Update user history and show the final score
    user_history(username, correct_answers, wrong_answers)
    show_score(correct_answers, wrong_answers)


def try_again():
    """
    Encourages the user to participate in another round of the quiz. If the user inputs 'Y', the quiz restarts.
    If 'N' is entered, a thank-you message is displayed, and the program exits.

    The function is designed with error handling to ensure a smooth user experience. If any unexpected errors occur during
    the input processing, they are caught, and an error message is displayed.

    Returns:
    - True: If the user chooses to restart the quiz.
    - False: If the user decides to exit the program.
    """
    while True:
        try:

            separator()

            # Prompt the user for another round and process their choice.
            print("Ready for another round? Take the quiz again and enjoy the learning journey!\n")
            choice = input("Choose Y or N and press enter:\n").upper().strip()

            # If the user chooses to restart the quiz ('Y'), clear the screen and return True.
            if choice == "Y":
                time.sleep(2)
                clear()
                return True

            # If the user chooses to exit the quiz ('N'), display a thank-you message, game over graphic, and exit.
            elif choice == "N":
                print()
                print(f"{Fore.CYAN}Thank you for attempting the quiz!\n")
                game_over = figlet_format("GameOver", font='doom', width=80)
                separator()
                print(f"{Fore.RED} {game_over}")
                separator()
                time.sleep(1)
                exit()

            # If the user provides an invalid input, prompt them to choose 'Y' or 'N'.
            else:
                print(Fore.RED + "Please choose Y or N.")

        # Catch any unexpected exceptions during user input processing and display an error message.
        except Exception as e:
            print(f"An error occurred: {e}")


def main():
    """
    The main function orchestrating the execution of the quiz program.

    Steps:
    1. Displays the welcome screen to greet the user.
    2. Presents the game rules to inform the user about the quiz guidelines.
    3. Initiates the quiz for the first time.
    4. Enters a loop where, after completing the quiz, the user is prompted to try again.
       If the user chooses to continue, another round of the quiz is initiated.
       This loop continues until the user decides to exit the program.

    The function serves as the entry point for running the quiz program.
    """
    welcome_screen()
    game_rules()
    quiz()

    # Enter a loop to allow the user to play the quiz again if desired.
    while try_again():
        quiz()


# Call the main function
# Credits: https://stackoverflow.com/questions/419163/what-does-if-name-main-do


if __name__ == "__main__":
    main()
