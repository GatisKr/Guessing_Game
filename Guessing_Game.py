
# A secret word Guessing Game
def play_game():
    secret_word = "python"
    name = ""
    guess = ""
    another_guess = ""
    guess_count = 0
    guess_limit = 1
    out_of_guesses = False

    print("\nPlease guess my favourite </> language :) \nYou can guess {} times".format(guess_limit)) # Formatting without f"" function
    name = input("\nPlease enter your name to continue: ")

    while guess.lower() != secret_word and not(out_of_guesses):
        if guess_count < guess_limit - 1:
            guess = input(f"\nPlease enter your {guess_count + 1} guess: ") # Formatting with f"" function
            guess_count += 1
            if guess.lower() != secret_word:
                print("No, that won't be the right one")
        elif guess_count < guess_limit:
            print("\nYou have only one guess left")
            guess = input("Please enter your best guess: ")
            guess_count += 1
        else:
            out_of_guesses = True

    if out_of_guesses:
        print(f"\nYou are out of guesses, {name}. Sorry.\n")
    else:
        print(f"\nCongratulations, {name}! You win!\n")

    while out_of_guesses:
        another_guess = input("Would you like to have another try? (yes/no) ")
        if another_guess.lower() in ["yes", "y", "ok","go"]:
            play_game()
            out_of_guesses = False
        elif another_guess.lower() in ["no", "n", "nope"]:
            print(f"Thanks for playing, {name}!\n")
            out_of_guesses = False
        elif another_guess.lower() in ["maybe"]:
            print(f"Please, give it a try! Say YES, YES, YES!!!\n")      
        else:
            print("Sorry, I don't understand. Please enter 'yes', 'no' or 'maybe'\n")

play_game()
