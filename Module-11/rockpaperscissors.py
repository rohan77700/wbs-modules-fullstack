import random

while True:
    user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
    choices = ['rock', 'paper', 'scissors']
    if user_choice not in choices:
        print('Invaild choice!')
        continue
    print("User choose:", user_choice)

    computer_choice = random.choice(choices)
    print("Computer choose:", computer_choice)

    if user_choice == computer_choice:
        print("It's a Tie!")
        continue
    elif(user_choice == 'rock' and computer_choice == 'scissors') or \
        (user_choice == 'paper' and computer_choice == 'rock') or \
        (user_choice == 'scissors' and computer_choice == 'paper'):
        print("You Win!")
    else:
        print("You Lost!") 

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != 'yes':
        break 