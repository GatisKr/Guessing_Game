
# A secret word Guessing Game

secret_word = "python"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

print("Please guess my favourite programming language. You can guess three times :)")
while guess.lower() != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter guess: ")
        guess_count += 1
    else:
        out_of_guesses = True
    guess = guess.lower()

if out_of_guesses:
    print("Out of Guesses, YOU LOSE!")
else:
    print("You win!")
    