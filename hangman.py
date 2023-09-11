from enum import Enum
import random
import textwrap

from texttable import Texttable

HANGMAN_PICS = ['''
  +---+
      |
      |
      |
     ===''', '''
  +---+
  O   |
      |
      |
     ===''', '''
  +---+
  O   |
  |   |
      |
     ===''', '''
  +---+
  O   |
 /|   |
      |
     ===''', '''
  +---+
  O   |
 /|\  |
      |
     ===''', '''
  +---+
  O   |
 /|\  |
 /    |
     ===''', '''
  +---+
  O   |
 /|\  |
 / \  |
     ===''', '''
  +---+
 [O   |
 /|\  |
 / \  |
     ===''', '''
  +---+
 [O]  |
 /|\  |
 / \  |
     ===''']


# Animals based secret words pool to extract secret words from
words = 'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra'.split()


# shapes based secret words
shapes = 'square triangle rectangle circle ellipse rhombus trapezoid'
Places = 'Cairo London Paris Baghdad Istanbul Riyadh'   # places based secret words


class Levels(Enum):
    """
    Represents the levels in a game.

    Args:
        Enum: A class that represents a set of named values.

    Returns:
        None

    Example:
        ```python
        level = Levels.Easy
        print(level)
        ```
"""

    Easy = 1
    Moderate = 2
    Hard = 3


def displayMenu(name: str):  # sourcery skip: extract-duplicate-method
    # SECTION Preparing Intro part of the Menu
    Intro = Texttable()

    Intro.set_cols_dtype(["t"])
    Intro.set_cols_align(['c'])
    Intro.set_chars(['', '', '', ''])
    # Adding Rows for Intro Table
    Intro.add_row([f'Hi, "{name}"'])
    Intro.add_row(['Welcome to HANGMAN'])
    #!SECTION

    # SECTION play game UI row with level selection Hints

    playGame = Texttable()
    playGame.set_cols_dtype(["t"])
    playGame.set_cols_align(['l'])
    playGame.set_chars(['', '', '', ''])
    # Adding rows to the play game Section
    playGame.add_row(["PLAY THE GAME"])

    # SECTION defining Levels that will be a part of play game row
    levelUI = Texttable()

    levelUI.set_cols_dtype(["t", "t", "t"])
    levelUI.set_cols_align(['c', 'c', 'c'])
    levelUI.set_chars(['', '', '', ''])

    levelUI.add_row(["1. EASY LEVEL", "2. MODERATE LEVEL", "3. HARD LEVEL"])
    #!SECTION levelUI

    # Adjoinging it to the playGame table
    playGame.add_row([levelUI.draw()])

    #!SECTION playGameUI

    # SECTION MenuUI: Creating The Master Menu UI to be displayed.
    MenuUI = Texttable(200)
    MenuUI.set_cols_dtype(["t"])
    MenuUI.set_cols_align(['c'])
    MenuUI.set_chars(['_', '|', '|', ''])

    # Adding rows to Menu UI
    MenuUI.add_row([Intro.draw()])
    MenuUI.add_row([playGame.draw()])
    MenuUI.add_row(['4. Hall Of  Fame'])
    MenuUI.add_row(['5. About The Game'])
    # !SECTION MenuUI
    return MenuUI.draw()


def displayAboutGame() -> None:
    '''return `about the game` section

    '''
    # SECTION About the Game UI Section

    about = Texttable()
    about.set_chars(['_', '|', '|', '_'])
    about.set_cols_align(['l'])
    about.set_cols_dtype(['t'])
    about.header(["ABOUT THE GAME"])

    # SECTION content of `About the game` UI
    aboutContent = Texttable()
    aboutContent.set_chars(['', '', '', ''])
    aboutContent.set_cols_align(['l', 'l'])
    aboutContent.set_cols_dtype(['t', 't'])

    aboutContent.add_row(["• Easy:", "The user will be given the chance to select the list from which the random word will be selected (Animal, Shap, Place). This will make it easier to guess the secret word. Also the number of trails will be increased from 6 to 8."])
    aboutContent.add_row(["• Medium:", "Similar to Easy, the user will be given the chance to select the set from which the random word will be selected (Animal, Plant, Place) but the number of trail will be reduced to 6. The last two graphics will not be used or displayed"])
    aboutContent.add_row(["• Hard:", "The code will randomly select a set of words. From this set the code will randomly select a word. The uses will have no clue on the secret word. Also, the number of trails will remain at 6."])
    # !SECTION aboutContent

    about.add_row([aboutContent.draw()])
    # !SECTION about UI

    print(about.draw())


def displaySetSelector():
    pass


def getRandomWord(wordList):
    '''This function returns a random string from the passed list of strings.'''

    wordIndex = random.randint(0, len(wordList) - 1)
    return wordList[wordIndex]


def displayBoard(missedLetters, correctLetters, secretWord):
    print(HANGMAN_PICS[len(missedLetters)])
    print()

    print('Missed letters:', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print()

    blanks = '_' * len(secretWord)

    # Replace blanks with correctly guessed letters.
    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

    for letter in blanks:  # Show the secret word with spaces in between each letter.
        print(letter, end=' ')
    print()


def getGuess(alreadyGuessed):
    # Returns the letter the player entered. This function makes sure the player entered a single letter and not something else.
    while True:
        print('Guess a letter.')
        guess = input()
        guess = guess.lower()

        if len(guess) != 1:
            print('Please enter a single letter.')
        elif guess in alreadyGuessed:
            print('You have already guessed that letter. Choose again.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter a LETTER.')
        else:
            return guess


def playAgain():
    # This function returns True if the player wants to play again; otherwise, it returns False.
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')


print('H A N G M A N')
missedLetters = ''
correctLetters = ''
secretWord = getRandomWord(words)
gameIsDone = False


while True:
    displayBoard(missedLetters, correctLetters, secretWord)

    # Let the player enter a letter.
    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess

        foundAllLetters = all(
            secretWord[i] in correctLetters for i in range(len(secretWord))
        )
        if foundAllLetters:
            print(f'Yes! The secret word is "{secretWord}"! You have won!')
            gameIsDone = True
    else:
        missedLetters = missedLetters + guess

        # Check if player has guessed too many times and lost.
        # TODO: `-1` is what we need to make variable to implement difficulty
        if len(missedLetters) == len(HANGMAN_PICS) - 1:
            displayBoard(missedLetters, correctLetters, secretWord)
            print('You have run out of guesses!\nAfter ' + str(len(missedLetters)) + ' missed guesses and ' +
                  str(len(correctLetters)) + ' correct guesses, the word was "' + secretWord + '"')
            gameIsDone = True

    if gameIsDone:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
            secretWord = getRandomWord(words)
        else:
            break
