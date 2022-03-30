# import python modules
#from time import sleep
from colorama import init, Fore
init()

# UTLITY FUNCTIONS
def print_intro():
    print()
    print("Welcome to the Wordle Simulator!")
    print()
    print("Wordle is a game where you have 6 tries to guess a 5-letter word.")
    print("After every guess, you are given some clues to show how close you are to the word:")
    print(Fore.GREEN + "GREEN LETTER" + Fore.RESET + " - letter is in word and in correct spot")
    print(Fore.YELLOW + "YELLOW LETTER" + Fore.RESET + " - letter is in word but in wrong spot")
    print("NORMAL LETTER - letter is not in word")
    print()
    print("This program is based off of the original Wordle game by Josh Wardle. You can find it here!")
    print("https://www.nytimes.com/games/wordle/index.html")
    print()


# MAIN PROGRAM
def main():
    # print intro text
    print_intro()
    # initial prompt
    play = input("Start game? (y/n): ")
    if play.lower() == "y":
        # starts main game loop
        while True:
            # pick mystery word in word bank

            # prompt to play again
            play_again = input("Play again? (y/n): ")
            if play_again.lower() == "y":
                continue
            elif play_again.lower() == "n":
                print("Thanks for playing! Exiting program.")
                break
            else:
                print("Invalid input. Exiting program.")
                break

    elif play.lower() == "n":
        print("Exiting. Bye!")
    else:
        print("Invalid response. Exiting.")

# PROGRAM RUNNER
if __name__ == "__main__":
    main()