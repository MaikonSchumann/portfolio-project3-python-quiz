# Import libraries
import colorama
from colorama import Fore, Style
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