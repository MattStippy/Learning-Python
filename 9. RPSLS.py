import random

c_moves = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]

computer = c_moves[random.randint(0,4)]

player = False


while player == False:
    print ("------Welcome to Rock-Paper-Scissors-Lizard-Spock!------")
    player = input("                  Enter your Move: ")
    if computer == player:
        print ("It's a Tie!")

    elif player == "Rock":
        if computer == 'Paper':
            print ("You Lost! Paper covers Rock!")
        if computer == 'Spock':
            print ("You Lost! Spock vaporises Rock!")
        if computer == 'Scissors':
            print ("You Win! Rock crushes Paper!")
        if computer == 'Lizard':
            print ("You Win! Rock crushes Lizard!")

    elif player == "Paper":
        if computer == 'Lizard':
            print ("You Lost! Lizard eats Paper!")
        if computer == 'Scissors':
            print ("You Lost! Scissors cuts Paper!")
        if computer == 'Rock':
            print ("You Win! Paper covers Rock!")
        if computer == 'Spock':
            print ("You Win! Paper disproves Spock!")

    elif player == "Scissors":
        if computer == 'Rock':
            print ("You Lost! Rock crushes Scissors!")
        if computer == 'Spock':
            print ("You Lost! Spock smashes Scissors!")
        if computer == 'Paper':
            print ("You Win! Scissors cuts Paper!")
        if computer == 'Lizard':
            print ("You Win! Scissors decapitates Lizard!")

    elif player == "Lizard":
        if computer == 'Rock':
            print ("You Lost! Rock crushes Lizard!")
        if computer == 'Scissors':
            print ("You Lost! Scissors decapitates Lizard!")
        if computer == 'Paper':
            print ("You Win! Lizard eats Paper!")
        if computer == 'Spock':
            print ("You Win! Lizard poisons Spock!")

    elif player == "Spock":
        if computer == 'Lizard':
            print ("You Lost! Lizard poisons Spock!")
        if computer == 'Paper':
            print ("You Lost! Paper disproves Spock!")
        if computer == 'Scissors':
            print ("You Win! Spock smashes Scissors!")
        if computer == 'Rock':
            print ("You Win! Spock vaporises Rock!")

    new_game = input("Do you want to play another round? (y/n): ")
    if new_game == 'y':
        player = False
        computer = c_moves[random.randint(0,4)]
    else:
        print ("Thanks for Playing!!!")
        break