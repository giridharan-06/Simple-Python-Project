
import random 

options = ('rock', 'paper', 'scissor')  # fixed spelling

running = True

while running:   
    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Enter your choice (rock, paper, scissor): ").lower()

    print(f"Player: {player}") 
    print(f"Computer: {computer}")

    if player == computer:
        print("It's a Tie!")
    elif player == "rock" and computer == "scissor":
        print("You Win!")
    elif player == "paper" and computer == "rock":
        print("You Win!")
    elif player == "scissor" and computer == "paper":
        print("You Win!")
    else:
        print("You Lose!")

    play_again = input("Do you want to play again (y/n)?: ").lower()
    if play_again != 'y':
        running = False

print("Thanks For Playing!")
