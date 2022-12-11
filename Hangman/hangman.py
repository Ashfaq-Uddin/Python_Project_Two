import random
import string

from words import words

def get_valid_word(words):
    word = random.choice(words)
    while "-" in words or " " in words:
        word = random.choice(words)
    return word.upper()


def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    used_letters = set()
    alphabet = set(string.ascii_uppercase)
    lives = 6

    while len(word_letters) > 0 and lives > 0:

        print("These are the words you have used so far:", " ".join(used_letters))
        word_list = [letter if letter in used_letters else "_" for letter in word]
        print("Your word so far is ", " ".join(word_list))
        user_letters = input("Please enter a character: ").upper()

        if user_letters in alphabet - used_letters:
            used_letters.add(user_letters)
            if user_letters in word_letters:
                word_letters.remove(user_letters)
            else:
                lives = lives - 1
                print("This letter is not in word")
                print("You have ", lives, "lives left!")
                print("\U0001F923")

        elif user_letters in used_letters:
            print("You have already used this letter.")
        else:
            print("This letter is not in the word!!")

    if lives == 0:
        print("You Died!! The word was ", word)
    else:
        print("You Won!!!! \U0001F970")

hangman()






    

