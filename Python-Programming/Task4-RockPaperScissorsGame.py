import random

def play_rock_paper_scissors():
  """Plays a game of Rock, Paper, Scissors."""

  user_score = 0
  computer_score = 0

  while True:
    user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
    while user_choice not in ['rock', 'paper', 'scissors']:
      print("Invalid choice. Please enter rock, paper, or scissors.")
      user_choice = input("Enter your choice (rock, paper, scissors): ").lower()

    computer_choice = random.choice(['rock', 'paper', 'scissors'])

    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
      print("It's a tie!")
    elif user_choice == 'rock':
      if computer_choice == 'scissors':
        print("Rock smashes scissors! You win!")
        user_score += 1
      else:
        print("Paper covers rock! You lose.")
        computer_score += 1
    elif user_choice == 'paper':
      if computer_choice == 'rock':
        print("Paper covers rock! You win!")
        user_score += 1
      else:
        print("Scissors cuts paper! You lose.")
        computer_score += 1
    elif user_choice == 'scissors':
      if computer_choice == 'paper':
        print("Scissors cuts paper! You win!")
        user_score += 1
      else:
        print("Rock smashes scissors! You lose.")
        computer_score += 1

    print(f"Your score: {user_score}")
    print(f"Computer score: {computer_score}")

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != 'yes':
      break

if __name__ == "__main__":
  play_rock_paper_scissors()
