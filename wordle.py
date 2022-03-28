from time import sleep
from colorama import init
from colorama import Fore, Back, Style
# print(Fore.RED + 'some red text')
# print(Back.GREEN + 'and with a green background')
# print(Style.RESET_ALL)
# print('back to normal now')
init() # initializes colorama

def coloramaDemo():
    print(Fore.GREEN + "C" + "R" +
            Fore.YELLOW + "A" + "N" +
            Fore.RESET + "E")

coloramaDemo()

print("Welcome to the Wordle Simulator!")
print()
print("Wordle is a game where you have 6 tries to guess a 5-letter word.")
print("After every guess, you are given some clues to show how close you are to the word:")
print(Fore.GREEN + "GREEN LETTER" + Fore.RESET + " - letter is in word and in correct spot")
print(Fore.YELLOW + "YELLOW LETTER" + Fore.RESET + " - letter is in word but in wrong spot")
print("NORMAL LETTER - letter is not in word")
print()
print("This program is based off of the original Wordle game, by Josh Wardle. You can find it here!")
print("https://www.nytimes.com/games/wordle/index.html")
print()
input("Start game? (y/n): ")

# may be used
def main():
    print("whale")

if __name__ == "__main__":
    main()