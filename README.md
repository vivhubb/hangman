# **THE HANGMAN GAME**
[THE HANGMAN GAME](https://dashboard.heroku.com/apps/hangman-gam3) is a Command Line Interface program built as the third Milestone Project using Python.

![display game](/readme_images/display.png)

---
## TABLE OF CONTENTS
---

<!-- TOC -->

- [**THE HANGMAN GAME**](#the-hangman-game)
    - [TABLE OF CONTENTS](#table-of-contents)
    - [USER EXPERIENCE](#user-experience)
        - [FLOWCHART](#flowchart)
    - [EXISTING FEATURES](#existing-features)
        - [Name input & Greeting](#name-input--greeting)
        - [Game rules](#game-rules)
        - [Difficulty level selection](#difficulty-level-selection)
        - [Game board](#game-board)
    - [FUTURE IMPROVEMENT IDEAS](#future-improvement-ideas)
    - [TECHNOLOGIES USED](#technologies-used)
    - [PYTHON MODULES](#python-modules)
    - [TESTING](#testing)
        - [MANUAL TESTING](#manual-testing)
        - [CODE VALIDATION](#code-validation)
    - [BUGS](#bugs)
    - [DEPLOYMENT](#deployment)
    - [CREDITS](#credits)
        - [Content](#content)
    - [RECOGNITION](#recognition)

<!-- /TOC -->

---
## USER EXPERIENCE
---

Users are able to play a game where they can try to guess the hidden word or phrase (depending on the difficulty level selected), one letter at a time. The game ends either when the user runs out of lives or when the correct answer was guessed.

### FLOWCHART
---

The flowchart for [THE HANGMAN GAME](https://dashboard.heroku.com/apps/hangman-gam3) was built using [Lucidchart](https://www.lucidchart.com/pages/).

The flowchart visualizes the separate steps of the game in sequential order. 

Once the program starts running the user is asked for a name input which is then followed by another input where the user has the option of reading the game rules and instructions before playing. The third input will require the user to select a difficulty level which will then start the main game loop with either a word or a phrase to be guessed.

The hidden word or phrase will then be visualized with a series of underline and any special characters will be given. Every guess is stored and displayed for the user and the correct guesses will uncover the hidden letters in their correct place(s). Every wrong answer will take away a life and draw a part of the hangman.

The game is over either when the correct answer was guessed or if the user runs out of lives and the hangman is complete. Once the game is over the user will be presented with an option to play again and if they do, this will take them back to difficulty level selection phase.

![flowchart](/readme_images/flowchart.png)

[JUMP to TOP](#table-of-contents)

---
## EXISTING FEATURES
---

### Name input & Greeting
---

The user is asked to input a name for the game which is the used to personalize experience with a greeting. The input is checked so that it does not contain any numbers or special characters. An empty string will also throw an 'Invalid input' feedback and the user will be asked to try again.

### Game rules
---

The user is prompted to make a choice if they want to see the game rules and instructions before playing. The input is checked so that only the given options are accepted and everything else throws a 'Invalid input' error and the user will be asked to try again.

### Difficulty level selection
---

At this stage the user is asked to select difficulty level for the game. They will have 2 options to choose from : easy and hard. Depending on their choice the game will build up for guessing either a random word from a list of approximately 2500 words or a random phrase from a list of approximately 200 idioms.

![features](/readme_images/features.png)

### Game board
---

Once the difficulty level is selected the game board is printed. We first see a banner for the game which helps to set the mood. This is followed by an empty gibbot where the hangman will be drawn and the place of the word or phrase to be guessed. For every letter in the word or phrase an underline will be displayed to represent the number of characters the correct answer has. All guesses made by the user (right or wrong) will be stored snd displayed to help keep track. Below, the user will have a life count which will show how many attempts are left until the game is over.

![easy game](/readme_images/easy.png)  ![hard game](/readme_images/hard.png)

[JUMP to TOP](#table-of-contents)

---
## FUTURE IMPROVEMENT IDEAS
---

* create a more complex design for the game board and banner
* expand the list of phrases for the game so it doesn't become repetitive
* expand the one at a time letter guess to word guesses as well
* create different options for difficulty level choice (like adding medium level or categories)
* create tracker to count wins and losses for user

[JUMP to TOP](#table-of-contents)

---
## TECHNOLOGIES USED
---

* [Python](https://www.python.org/) - programming language used to build the game
* [Heroku](https://dashboard.heroku.com/apps) - platform used to deploy the game
* [Lucidchart](https://www.lucidchart.com/pages) - used for creating the flowchart of the programme
* [Github](https://github.com/) - used for creating and storing the repository of the project
* [Gitpod](https://gitpod.io/) - used for creating and trialing the code
* [Visual Studio Code](https://code.visualstudio.com/) - code editor used to create initial version of the project
* [PowerShell](https://www.powershellgallery.com/) - task automation and configuration management program used to build and test solutions

[JUMP to TOP](#table-of-contents)

---
## PYTHON MODULES
---

* [random](https://docs.python.org/3/library/random.html) - module used to generate random actions
* [platform](https://docs.python.org/3/library/platform.html) - module used to access underlying platform's data
* [os](https://docs.python.org/3/library/os.html) - module used to interact with the underlying operating system

---
## TESTING
---

### MANUAL TESTING
---

[THE HANGMAN GAME](https://dashboard.heroku.com/apps/hangman-gam3) was tested throughout development in VS Code, PowerShell, Gitpod and Heroku. Manual testing verified and confirmed the functionality of the steps listed below:

* **Program Start**
    - program starts without any detected issues
    - name input request runs on start-up
    - invalid input calls error feedback for user

* **Name input**
    - input is validated against special characters, numbers and empty spaces
    - invalid input calls error feedback for user

* **Game Rules**
    - option to see the game rules runs after name input
    - input is validated to only accept given options
    - invalid input calls error feedback for user

* **Difficulty level selection**
    - difficulty selection runs after game rules option
    - input is validated to only accept given options
    - valid input pulls random item from the correct list based on difficulty selection
    - invalid input calls error feedback for user

* **Game board**
    - initial empty game board is printed after difficulty selection

* **Letter guess**
    - input is validated to only accept letters (A-Z)
    - correct guesses uncover the letters in their respective place(s)
    - invalid input calls error feedback for user

* **Remaining attempts**
    - remaining attempts are displayed as lives and they refresh after each guess
    - wrong guess will decrease the number of lives and draw the respective part of the stick man

* **Used letters tracker**
    - user guesses are stored and displayed for user
    - guess duplicate calls error feedback for user

* **End game**
    - the game ends once word is guessed or the man is hung
    - provides winner or looser message feedback for user

* **Play again**
    - play again option runs correctly when game is over
    - game returns to difficulty selection and restarts correctly on affirmative
    - otherwise the program stops running while providing a feedback message for user

### CODE VALIDATION
---

All python files pass validation through the [PEP8 online check](http://pep8online.com/) with no errors.

* [words.py](/readme_images/check_words.png)
* [phrases.py](/readme_images/check_phrases.png)
* [rules.py](/readme_images/check_rules.png)
* [hangman_stages.py](/readme_images/check_stages.png)
* [hangman_game.py](/readme_images/check_game.png)
* [run.py](/readme_images/check_run.png)

[JUMP to TOP](#table-of-contents)

---
## BUGS
---

While creating the game i have identified and corrected the below bugs:

* Even though every letter was guessed correctly the word builder would not be equal to the randomly choosen word/phrase as it was a list of strings. The bug solution was tested and proved using PowerShell.

```
while option in ['Y', 'YES']:
        while error_count != error_limit:
            print_board(build_word, used_letters)
            guess = get_user_input(used_letters)
            if not check_user_input(guess, random_word, build_word):
                error_count += 1
            if str(build_word) == random_word:	    # bug
                winner = True
                break
 while option in ['Y', 'YES']:
        while error_count != error_limit:
            print_board(build_word, used_letters)
            guess = get_user_input(used_letters)
            if not check_user_input(guess, random_word, build_word):
                error_count += 1
            if ''.join(build_word) == random_word:	    # correction
                winner = True
                break

```
![correction trial](/readme_images/fix_01.png)

* Letter guess input would accept consecutive letters from abc as ascii_letters is a long string with letters (a-Z). The bug solution was tested and proved using PowerShell.

![bug 2](/readme_images/bug_02.png)

![fix 2](/readme_images/fix_02.png)

[JUMP to TOP](#table-of-contents)

---
## DEPLOYMENT
---

* **Deployment**

The project was deployed to [Heroku](https://dashboard.heroku.com/apps). Deployment steps are:

1. Log in to Heroku or Set up an account

![log in](/readme_images/heroku_01.png)

2. Create a new app from the dashboard

![new app](/readme_images/heroku_02.png)

3. Enter a unique name and select region
4. Click the 'Create app' button

![create app](/readme_images/heroku_03.png)

5. Select the settings tab from navigation panel
6. Click 'Reveal config vars' button
7. In the 'Key' field input 'PORT'; in the 'Value' field input '8000'
8. Press 'Add' button
9. Scroll down and click 'Add buildpack'
10. First add 'Python'
11. Then add 'node.js'


![settings](/readme_images/heroku_04.png)

12. Scroll up and select the 'Deploy' tab from navigation menu
13. In the 'Deployment method' section select GitHub and connect your repository
14. Scroll down and select your preferred deployment type then click 'Deploy branch' 

![deploy](/readme_images/heroku_05.png)

* **Cloning the repository**

[JUMP to TOP](#table-of-contents)

---
## CREDITS
---

### Content

* List of words was found via [Stack Overflow](https://www.randomlists.com/data/words.json).
* List of phrases was built from [Topcorrect](https://www.topcorrect.com/blog/50-popular-idioms-to-sound-like-a-native-speaker/) and [Literary Devices](https://literarydevices.net/huge-list-of-idiom-examples/).
* The flowchart was built using [Lucidchart](https://www.lucidchart.com/pages/)


---
## RECOGNITION
---

[JUMP to TOP](#table-of-contents)