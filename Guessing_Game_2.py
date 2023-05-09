
# A secret word Guessing Game
def play_game():
    secret_word = "python"
    name = ""
    guess = ""
    another_guess = ""
    guess_count = 0
    guess_limit = 3
    out_of_guesses = False

    # Formatting example without f"" function
    print("\nPlease guess my favourite </> language :) \nYou can guess {} times".format(guess_limit)) 
    name = input("\nPlease enter your name to continue: ")
    guess = ""
    another_guess = ""
    while guess.lower() != secret_word and not(out_of_guesses):
        if guess_count < guess_limit - 1:
            # Formatting example with f"" function
            guess = input(f"\nPlease enter your {guess_count + 1} guess: ")
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

def another_try():
    while True:
        another_guess = input("Would you like to have another try? ")
        if another_guess.lower() in ["yes", "y", "sure", "ok", "go", "try"]:
            play_game()
        elif another_guess.lower() in ["no", "n", "nope"]:
            print(f"Thanks for playing!\n")
            break
        else: 
            print("Sorry, unable to handle response. Please enter correct value\n")
            continue
    
play_game()
another_try()
