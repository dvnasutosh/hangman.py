import random


def bold_text(text):
    '''Returns boldened text'''

    bold_start = '\033[1m'
    bold_end = '\033[0m'
    return bold_start + text + bold_end


class gameData:
    """
    A class to store the data for a hangman game.

    Attributes:
        missedLetters (str): The letters that the player has guessed incorrectly.
        correctLetters (str): The letters that the player has guessed correctly.
        gameIsDone (bool): Whether the game is over.
        difficultyLambda (float): A factor that determines the difficulty of the game.
        name (str): The player's name.
        secretWord (str): The secret word.

    Methods:
        initialSetup(): Resets the game data.
    """

    def initialSetup(self):
        """
            Resets the game data.

            Sets the following attributes to their initial values:
                * missedLetters: An empty string.
                * correctLetters: An empty string.
                * gameIsDone: False.
                * difficultyLambda: 1.
                * name: The player's name.
                * secretWord: An empty string.

            This method is used to manually reset the data, for example when the player wants to start a new game.
        """
        self.missedLetters = ''
        self.correctLetters = ''
        self.gameIsDone = False
        self.difficultyLambda = 1
        while True:
            self.name = input('Please enter your name: ')
            if self.name.isalpha():
                break
            print('Please Enter alphabets only')
        self.secretWord = ''


def getRandomWord(wordList):
    '''This function returns a random string from the passed list of strings.'''

    wordIndex = random.randint(0, len(wordList) - 1)
    return wordList[wordIndex]


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
