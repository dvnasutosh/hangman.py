

from UI import displayAboutGame, displayBoard, displayLeaderBoard, displayMenu, displaySetSelector
from database import SqlLite

from helper import gameData, getGuess, getRandomWord, playAgain
from constants import HANGMAN_PICS, animals, places, shapes, setOptions

def getMenu(data: gameData,db: SqlLite):
    # Display the menu
    while True:
        displayMenu(data.name)

        print()
        
        choice = int(input("Enter Choice: "))
        if choice not in range(1,6):
            print('Wrong Choice!')
            continue
        # Handling about game section first
        if choice == 5:
            displayAboutGame()
            input("Press any key to return to menu: ")
            continue
        # Handling aboutleaderboard Section
        if choice ==4:
            displayLeaderBoard(db.getLeaderBoard())
            db.conn.close()
            input("Press any key to return to menu: ")
            continue
            
        data.difficultyLambda = 3 if choice != 1 else 1

        if choice != 3:
            displaySetSelector()
            print()
            setChoice = int(input("Enter the set of your choice: "))
            
            while True:
                try:
                    data.secretWord = getRandomWord(setOptions[setChoice])
                except KeyError:
                    print('Please enter a valid option.')
                    continue
                break

        else:
            data.secretWord = getRandomWord(animals+shapes+places)
        return choice


if __name__=='__main__':
    # ANCHOR Game Flow

    data = gameData()
    db=SqlLite()
    data.initialSetup()
    difficultyLevel = getMenu(data,db)


    while True:

        displayBoard(data.missedLetters, data.correctLetters, data.secretWord)

        # Let the player enter a letter.
        guess = getGuess(data.missedLetters + data.correctLetters)

        if guess in data.secretWord:
            data.correctLetters += guess

            foundAllLetters = all(
                data.secretWord[i] in data.correctLetters for i in range(len(data.secretWord))
            )
            if foundAllLetters:
                
                db.add(
                    name       = data.name,
                    livesleft  = (len(HANGMAN_PICS) - data.difficultyLambda) - len(data.missedLetters),
                    difficulty = difficultyLevel
                    )
                
                
                print(
                    f'Yes! The secret word is "{data.secretWord}"! You have won!')
                data.gameIsDone = True
        else:
            data.missedLetters += guess

            # Check if player has guessed too many times and lost.
            # TODO: `-1` is what we need to make variable to implement difficulty
            if len(data.missedLetters) >= (len(HANGMAN_PICS) - data.difficultyLambda):
                displayBoard(
                    data.missedLetters,
                    data.correctLetters, data.secretWord)
                print('You have run out of guesses!\nAfter ' + str(len(data.missedLetters)) + ' missed guesses and ' +
                    str(len(data.correctLetters)) + ' correct guesses, the word was "' + data.secretWord + '"')
                data.gameIsDone = True

        if data.gameIsDone:
            if playAgain():
                data.initialSetup()
                difficultyLevel=getMenu(data,db)
            else:
                break
