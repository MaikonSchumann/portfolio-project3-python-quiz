# Python Quiz

Prepare for the Python Quiz, a lively 10-question multiple-choice test designed for Python newcomers! Although we have 30 questions in the database, each quiz session randomly selects 10. If you're teaching Python courses, think about incorporating this quiz to captivate your students and identify areas where they might benefit from some extra assistance. The results are conveniently stored in an external file, allowing for easy visualization through user-friendly spreadsheet functionality. Let's simplify the journey of mastering Python!

- - -

![Python Quiz](documentation/welcomescreen.png)

## Demo

You can explore a live demonstration [here](https://project3-python-quiz-5f0c6fd0bce1.herokuapp.com/).
The application has been deployed using Heroku.

- - -

# Technologies Used
## Language
* Python3

## Libraries
* colorama
* pyfiglet
* time
* gspread
* google.oauth2.service_account
* random

## Frameworks & Tools
* Heroku Platform: Deployment of the application in a live environment.
* Visual Studio Code: Creation of the website.
* GitHub: Repository storage and deployment of the website.
* Google Sheets API: Handling data automation.
* [Lucidchart](https://www.lucidchart.com/) - to draw a flowchart.

- - -

For this project, I utilized a [Code Institute template](https://github.com/Code-Institute-Org/python-essentials-template), which supplied all the necessary files to enable the mock terminal functionality in the browser.

The questions and options are extracted from the "questions" worksheet, which stores 30 general questions. User history is updated in the "history" worksheet.

* Question Worksheet:
* ![Spreadsheet](documentation/questionsworksheet.png)

* History Worksheet:
* ![Spreadsheet](documentation/historyworksheet.png)

- - - 

# User Experience (UX)

## The ideal users for this website is:
* Users learning Python who wish to assess their knowledge.

## User stories:

* As a new user, I expect to quickly comprehend the program's purpose.


* I wish for clear instructions on how to participate in the quiz.
* I expect precise feedback based on my inputs.
* I would like the choice to either replay the quiz or exit the program.
* I expect the ability to restart the quiz.

## How to play:

- Initially, the user is required to input a valid name to commence the game.
- Subsequently, the user can review the instructions.
- Following that, the quiz initiates, and the user must select a, b, c, or d as their choice.
- The score increases by one for each correct choice or incorrect one.
- After finishing the 10 random questions, the user's score will be shown in the terminal and stored in the history worksheet.
- Finally, the user will be given the choice to either play again or exit the program.

- - -