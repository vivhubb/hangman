# **THE HANGMAN GAME**
[THE HANGMAN GAME](https://dashboard.heroku.com/apps/hangman-gam3) is a Command Line Interface program built using Python.

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
    - [FUTURE IMPROVEMENT IDEAS](#future-improvement-ideas)
    - [TECHNOLOGIES USED](#technologies-used)
    - [TESTING](#testing)
        - [CODE VALIDATION](#code-validation)
    - [BUGS](#bugs)
    - [DEPLOYMENT](#deployment)
    - [CREDITS](#credits)
    - [RECOGNITION](#recognition)

<!-- /TOC -->

---
## USER EXPERIENCE
---

### FLOWCHART
---

![flowchart](/readme_images/flowchart.png)

---
## EXISTING FEATURES
---

---
## FUTURE IMPROVEMENT IDEAS
---

---
## TECHNOLOGIES USED
---

* [Python](https://www.python.org/)
* [Heroku](https://dashboard.heroku.com/apps)
* [Lucidchart](https://www.lucidchart.com/pages)
* [Github](https://github.com/)
* [Gitpod](https://gitpod.io/)

---
## TESTING
---

### CODE VALIDATION
---

All python files pass validation through the [PEP8 online check](http://pep8online.com/) with no errors.

![check words](/readme_images/check_words.png)
![check phrases](/readme_images/check_phrases.png)
![check rules](/readme_images/check_rules.png)
![check stages](/readme_images/check_stages.png)
![check run](/readme_images/check_run.png)
![check game](/readme_images/check_game.png)

---
## BUGS
---

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

![bug 2](/readme_images/bug_02.png)

![fix 2](/readme_images/fix_02.png)

---
## DEPLOYMENT
---

---
## CREDITS
---

---
## RECOGNITION