# Import libraries
import colorama
from colorama import Fore, Style
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