from texttable import Texttable

from constants import HANGMAN_PICS
from helper import bold_text

def displayLeaderBoard(dbResult: list):
    """ print UI for leader board

    Args:
        dbResult (list): list of rows to be displayed in leaderboard
    """
    leaderboardUI=Texttable()

    # configuration of LeaderBoardUI
    leaderboardUI.set_cols_align(['c'])
    leaderboardUI.set_chars(['','','',''])
    

    # Handling content UI
    contentUI= Texttable()
    contentUI.set_chars(['_', '|', '|', '_'])
    contentUI.set_cols_align(['l','l','l'])
    contentUI.set_cols_dtype(['t','t','i'])
    contentUI.set_cols_width([18,18,18])
    
    # Setting header
    contentUI.header(['Level','Winner name','Remaining lives'])
    
    for i in dbResult:
        contentUI.add_row(i[1:])
        
    # Mergin titleUI and contentUI on to leaderBoardUI
    leaderboardUI.add_row([ 'Leaderboard' ])
    leaderboardUI.add_row([contentUI.draw()])
    
    print(leaderboardUI.draw())
    
def displayMenu(name: str):  
    '''Display The main Menu'''
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
    print(MenuUI.draw())


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

    # Adding about section content as row
    about.add_row([aboutContent.draw()])
    # !SECTION about UI

    print(about.draw())


def displaySetSelector():
    '''Display the secret word sets to select from.'''

    SetSelector = Texttable()

    SetSelector.set_chars(['_', '|', '|', '_'])
    SetSelector.set_cols_align(['c'])
    SetSelector.set_cols_dtype(['t'])

    SetSelector.header(["SELECT FROM THE FOLLOWING SETS Of SECRET WORDS"])

    Sets = Texttable()
    Sets.set_chars(['', '', '', ''])

    Sets.add_row(['1. Animal', '2. Shapes', '3. Places'])

    SetSelector.add_row([Sets.draw()])

    print(SetSelector.draw())


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
    print()

    for letter in blanks:  # Show the secret word with spaces in between each letter.

        print(letter, end=' ')
    print()
