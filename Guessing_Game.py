
# A secret word Guessing Game

def play_game():

    secret_word = "python"
    name = ""
    guess = ""
    another_guess = ""
    guess_count = 0
    guess_limit = 3
    out_of_guesses = False

    print("\nPlease guess my favourite </> language :) \nYou can guess " + "{}".format(guess_limit) + " times")
    name = input("\nPlease enter your name to continue: ")

    while guess.lower() != secret_word and not(out_of_guesses):

        if guess_count < guess_limit - 1:
            guess = input("\nPlease enter your " + "{}".format(guess_count + 1) + " guess: ")
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
        print("\nYou are out of guesses, " + name + ". Sorry.\n")

    else:
        print("\nCongratulations, " + name + "! You win!\n")

    if out_of_guesses:
        another_guess = input("Would you like to have another try? (yes/no) ")

        if another_guess.lower() == "yes":
            play_game()
        else:
            print("Thanks for playing!\n")

play_game()
