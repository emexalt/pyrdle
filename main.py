import random

words = open("sgb-words.txt", "r")
word_list = list(words)
print(word_list)
#target_word = random.choices(word_list)
target_word = "spore"
guess_limit = 6
guess_counter = 0
guess = ""

def check_guess_matches(guess, target_word):
    matches = ""
    for i in range(len(guess)):
        if guess[i] = target_word[i]:
            matches = matches + guess[i]
        else:
            matches = matches + "X"
    return matches

def check_guess_contains(guess, target_word):
    contained_letters = []
    for i in range(len(guess)):
        if guess[i] in target_word:
            contained_letters = contained_letters + guess[i]
        else:
            contained_letters = contained_letters
    return contained_letters




while guess != target_word and guess_counter <= guess_limit:
    guess_counter = guess_counter + 1
    guess = input("Guess a word: ")
    if guess == target_word:
        print("Guessed correctly!")
    else:
        print("Guessed incorrectly")

