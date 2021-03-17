import random

c_moves = ["Rock", "Paper", "Scissors"]

computer = c_moves[random.randint(0,2)]

player = False

while player == False:
    player = input("Enter Your Move: ")
    if computer == player:
        print ("It's a Tie!")

    elif player == 'Rock':
        if computer == 'Paper':
            print ("You Lose! Paper Covers Rock!")
        else:
            print ("You Win! Rock crushes Scissors!")

    elif player == 'Paper':
        if computer == 'Scissors':
            print ("You Lose! Scissors cuts Paper!")
        else:
            print ("You Win! Paper Covers Rock!")

    elif player == 'Scissors':
        if computer == 'Rock':
            print ("You Lose! Rock crushes Scissors!")
        else:
            print ("You Win! Scissors cuts Paper!")

    new_game = input("Do you want to play another round? (y/n) ")
    if new_game == 'y':
        player = False
        computer = c_moves[random.randint(0,2)]
    else:
        print("Thanks for Playing!!!")
        break