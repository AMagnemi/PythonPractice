import random


secret_num = random.randrange(100)
guess = ""
guess_count = 0
guess_limit = 5
out_of_guesses = False
play_again = ""

print("You have 5 guesses to choose the number between 1 and 100, GOOD LUCK!")

while guess != secret_num and not out_of_guesses:
    if guess_count < guess_limit:
        guess = int(input("Enter guess: "))
        guess_count += 1
        if guess < secret_num:
            print("Guess too low!")
        elif guess > secret_num:
                print("Guess too high!")
    else:
        out_of_guesses = True

if out_of_guesses:
    print(" You are OUT OF GUESSES, YOU LOSE!")
    print(f"The correct number was {secret_num}")
else:
    print("You win!")

print("")

if guess_count == guess_limit:
    play_again = input("Would you like to play again? Y or N: ")
    if play_again == "Y":
        guess_count = 0
        out_of_guesses = False
    if play_again == "N":
        print("GAME OVER!")