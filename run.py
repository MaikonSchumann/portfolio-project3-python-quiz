# Import libraries
import colorama
from colorama import Fore, Style
import pyfiglet
from pyfiglet import figlet_format
import time
import gspread
from google.oauth2.service_account import Credentials

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
    
    Credits: https://stackoverflow.com/questions/29887629/how-to-clear-terminal-mac-osx-scrollback/29887659#29887659
    """
    print('\033c')
    
def game_rules():
    """
    Displays the game rules to the user.

    Explains the quiz format: friendly multiple-choice questions.
    Instructs users to answer by typing 'a', 'b', 'c', or 'd' and pressing 'Enter'.
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
    
user_history('maikon', 6, 4)