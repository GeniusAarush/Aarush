import random
print("Welcome to the game of Rock, Paper, Scissors! |made by Aarush|")

def get_user_choice():
    user_choice = input("Enter Your Choice (rock , paper, or scissors)").lower()
    if user_choice in ('rock','paper','scissors'):
        return user_choice



def get_computer_choice():
    while True:
         return random.choice(['rock','paper','scissors'])
      
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return 'its a tie!'
    elif(user_choice == 'rock'and computer_choice == "scissors"):
        print("You Wins")
    elif(user_choice == 'scissors'and computer_choice == "paper"):
        print("You wins")
    elif(user_choice == 'paper'and computer_choice == "rock"):
        print("You wins")
    else:
        print("Computer wins")

def play_game():
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"\n Your Choice: {user_choice}")
        print(f" Computer Choice: {computer_choice}")

        result = determine_winner(user_choice ,computer_choice)
        print(result)

        
if __name__ == "__main__":
    play_game()


