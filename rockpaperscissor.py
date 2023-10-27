import random
def play_game():
    print("Leta play rock,paper and scissors!")
    print("enter your choice:(rock,paper,scissor)")
    player_choice=input().lower()
    computer_choice=random.choice(["rock","paper","scissor"])
    print("Computerchooses:",computer_choice)
    if player_choice==computer_choice:
        print("its a tie")
    elif player_choice=="rock":
        if computer_choice=="paper":
            print("Computer wins!")
        else:
            print("You win!")
    elif player_choice=="rock":
        if computer_choice=="scissors":
            print("Computer wins!")
        else:
            print("You win!")
    elif player_choice=="scissors":
        if computer_choice=="rock":
            print("Computer wins!")
        else:
            print("You win!")
    else:
        print("Invalid input.Please try again")
    play_again()
def play_again():
    print("Do you want to play again(yes/no)")
    choice=input().lower()
    if choice=="yes":
        play_game()
    elif play_game=="no":
        print("Thnak You for playing!Bye")
    else:
        print("Input input.Please try again")
play_game()
    
