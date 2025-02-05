import random

# List of words to choose from
words = ["python", "javascript", "hangman", "programming", "developer", "computer", "keyboard", "guitar"]

# Select a random word from the list
word = random.choice(words)
guesses = "_" * len(word)
guessed_letters = []
attempts = 6  # Number of attempts before game over

print("Welcome to Hangman!")
print("Guess the word:")
print(" ".join(guesses))

# Game loop
while attempts > 0 and "_" in guesses:
    guess = input(f"\nYou have {attempts} attempts left. Guess a letter: ").lower()

    # Check if the guess is valid
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a valid letter.")
        continue

    # Check if the letter has already been guessed
    if guess in guessed_letters:
        print("You've already guessed that letter.")
        continue

    guessed_letters.append(guess)

    # Check if the guessed letter is in the word
    if guess in word:
        print(f"Good guess! The letter '{guess}' is in the word.")
        # Update the word display
        guesses = "".join([guess if word[i] == guess else guesses[i] for i in range(len(word))])
    else:
        print(f"Oops! The letter '{guess}' is not in the word.")
        attempts -= 1

    print("Word: " + " ".join(guesses))

# Check if the player has won or lost
if "_" not in guesses:
    print("\nCongratulations! You've guessed the word correctly.")
else:
    print("\nGame over! The word was:", word)
