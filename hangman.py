from random_word import RandomWords

words = RandomWords()
guess_word = words.get_random_word()


# A function that swap the correctly guess letters
def swap(user_guess: str, word: str, unknown: str):
    index = 0
    index_list = []
    for i in word:
        if user_guess == word[index]:
            index_list.append(index)
            index += 1
        else:
            index += 1

    for i in index_list:
        unknown = unknown[:i] + user_guess + unknown[i+1:]

    return unknown

def hangman(guess_word: str):
    """Returns the hangman game result"""
    print("---------------------------------------------\nWelcome to the oasix hangman")
    trys = 5  
    word_count = 0
    unknown = ""
    for i in guess_word:
        word_count+=1
        unknown +="_"  

    while True: 
 
        print(f"Find the missing letters. Letter count = {word_count}\nYou have {trys} trys left.\n'{" ".join(unknown)}'\n---------------------------------------------")

        user_guess = input("enter guess: ")

        if len(user_guess) != 1 or user_guess.isalpha() == False or user_guess == "":  
            print("--------------------------------------------\nInvalid input: letter must be a single letter\n-------------------------------------------------")
        else:
            if user_guess in guess_word and user_guess not in unknown:
                unknown = swap(user_guess, guess_word, unknown)
                print(f"Guess correct!\n {" ".join(unknown)}\n-----------------------------------------------")  
                if unknown == guess_word:
                    print(f"Congratulations, you won! Five gbosa for you\n----------------------------------------")
                    break

            elif user_guess in unknown:
                print(f"You've already guessed '{user_guess}' correctly.\n-------------------------------------------------")

            else:
                trys -= 1                
                print(f"Invalid guess!.\n-------------------------------------------------")
                if trys == 0:
                    print(f"You lost! The word was '{guess_word.capitalize()}'.\n-----------------------------------------------")
                    break


hangman(guess_word)
