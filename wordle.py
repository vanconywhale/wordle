# colorama library by Jonathan Tartley and other contributors:
# https://github.com/tartley/colorama
from colorama import init, Fore, Style
# random is a python built-in module
import random
init()



# prints intro text and asks user to play
## I created this function!
def print_intro():
    print()
    print("Welcome to the Wordle Simulator!")
    print()
    print(f"Wordle is a game where you have 6 tries to guess the {colorful_wordle()}, a random 5-letter word.")
    print("After every guess, you are given some clues that show how close you are to the word:")
    print(Fore.GREEN + "GREEN LETTER" + Fore.RESET + " - letter is in word and in correct spot")
    print(Fore.YELLOW + "YELLOW LETTER" + Fore.RESET + " - letter is in word but in wrong spot")
    print("NORMAL LETTER - letter is not in word")
    print()
    print("This program is based off the original Wordle game by Josh Wardle. You can find it here!")
    print("https://www.nytimes.com/games/wordle/index.html")
    print()
    play = input("Start game? (y/n): ")
    if play.lower() == "y":
        return True
    elif play.lower() == "n":
        print("Exiting. Bye!")
        return False
    else:
        print("Invalid response. Exiting.")
        return False



# returns a colorful WORDLE!
## I created this function!
def colorful_wordle():
    return f"{Fore.GREEN}W{Fore.YELLOW}O{Fore.RESET}R{Fore.GREEN}D{Fore.YELLOW}L{Fore.RESET}E"


# prints out color hint of the guess, wordle-style
# INPUT: 5-letter uppercase guess, 5-letter uppercase wordle
# OUTPUT: 5-letter uppercase color hint
## I initially created this function, but there were some bugs that my teammates fixed for me!
def color_compare(guess, wordle):
    color_list = ["#","#","#","#","#"]
    color_word = ""
    guess = list(guess)
    wordle = list(wordle)
    # check for letter in exact spot
    for i in range(5):
        if guess[i] == wordle[i]:
            color_list[i] = (Fore.GREEN + guess[i] + Fore.RESET)
            wordle[i] = "#"
            guess[i] = "*"
    # check for letter in wordle but not exact spot
    for i in range(5):
        if guess[i] in wordle:
            color_list[i] = (Fore.YELLOW + guess[i] + Fore.RESET)
            wordle[wordle.index(guess[i])] = "#"
    # fill remaining letters
    for i in range(5):
        if color_list[i] == "#":
            color_list[i] = (Fore.RESET + guess[i] + Fore.RESET)

    # bulid the color_hint
    for i in range(5):
        color_word += color_list[i]
    return color_word

## I created the general outline of the main function!
def main():
    # welcome user
    game_loop = print_intro()

    # main game loop
    while game_loop:
        num_tries = 6
        ## my teammates created the code for accessing word-bank and valid-words!
        # get random wordle from word bank list
        # the Word Bank and Valid Word List are credits to Sean Patlan, which can be found on their github: https://github.com/seanpatlan/wordle-words%22
        with open("word-bank.csv") as f:
            wordlist = [row.split()[0] for row in f]
            wordle = str(random.choice(wordlist)).upper()
        # get list of valid guesses
        with open("valid-words.csv") as f:
            guesslist = [row.split()[0] for row in f]

        # defining the alphabet
        letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        lettercolours = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        
        ## my teammates created the general game logic! (ask user input, win condition, lose condition)
        # loop for each attempt
        while True:
            temp = ""
            # make sure input is a valid guess
            while True:
                print()
                print("Letter Bank: " + letters)
                print(f"Guess the WORDLE! ({str(num_tries)} tries left): ")
                guess = input().upper()
                temp = guess
                if len(guess) != 5:
                    print("Invalid guess. Please type a 5-letter word.")
                    continue
                elif guess.lower() not in guesslist:
                    print("Invalid guess. Word is not in valid word bank. ")
                    continue
                else:
                    # valid word, exit loop
                    break
            
            # print out color comparison
            print(color_compare(guess, wordle))
            
            num_tries -= 1
            
            # if guess matches wordle, congrats!
            if guess.upper() == wordle:
                print()
                print(f"Congrats you found the {colorful_wordle()}!")
                print(f"It took you {str(6 - num_tries)} attempt(s) to find the {colorful_wordle()}!")
                break
            
            # if run out of guesses, game over :(
            if num_tries <= 0:
                print()
                print("You ran out of guesses!")
                print(f"The {colorful_wordle()} was: {wordle}")
                break
            
            ## my teammates created the code for making the letter bank!
            # printing out what letters have not been guessed
            for i in range(len(temp)):
                if temp[i] == wordle[i]:
                    letters = letters.replace(temp[i], Fore.GREEN + temp[i] +
            Fore.RESET)
                    lettercolours = lettercolours.replace(temp[i],"#")
                elif temp[i] in wordle:
                    if temp[i] in lettercolours:
                        letters = letters.replace(temp[i], Fore.YELLOW + temp[i] +
            Fore.RESET)
                else:
                    letters = letters.replace(temp[i], Fore.LIGHTBLACK_EX + temp[i] +
            Fore.RESET)

        # play again logic
        print()
        play = input("Play again? (y/n): ")
        if play.lower() == "y":
            continue
        elif play.lower() == "n":
            print("Exiting. Thank you for playing, Bye!")
            game_loop = False
        else:
            print("Invalid response. Exiting.")
            game_loop = False



# run main program
if __name__ == "__main__":
    main()