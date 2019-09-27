# --- Define your functions below! ---
from random import randint
global quit
quit = False
def intro():
    print("Hi! My name is Chatty! Type quit at anytime to end the game or type Let's play a game! if you want to play.")
def game():
#list
    list = ["Rock", "Paper", "Scissors"]
    computer = list[randint(0,2)]
    player = False

    while player == False:

        player = input("Rock, Paper, Scissors?")
        if player == computer:
            print("Tie!")
        elif player == "Rock":
            if computer == "Paper":
                print("You lose!", computer, "covers", player)
            else:
                print("You win!", player, "smashes", computer)
        elif player == "Paper":
            if computer == "Scissors":
                print("You lose!", computer, "cut", player)
            else:
                print("You win!", player, "covers", computer)
        elif player == "Scissors":
                if computer == "Rock":
                    print("You lose...", computer, "smashes", player)
                else:
                    print("You win!", player, "cut", computer)
        else:
            print("That's not a valid play. Check your spelling!")
    player = False
    computer = list[randint(0,2)]

def process_input(user):
    if user == "hi":
        print("Hello! How are you")
    elif user == "quit":
        print("Bye!")
        global quit
        quit = True
    elif user == "Let's play a game!":
        print("Great!")
        game()
    else:
        print("Cool")


# --- Put your main program below! ---

def main():
    intro()

    while True:
        answer = input("(What will you say?) ")
        process_input(answer)
        global quit
        if(quit == True):
            break





# DON'T TOUCH! Setup code that runs your main() function.
if __name__ == "__main__":
    main()
