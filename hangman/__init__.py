"""" Hangman-game"""
import random


def __init__():
    """" Hangman initialisation"""
    dictionary = ['mother',
                  'father',
                  'permission',
                  'flight',
                  'apple',
                  'desire',
                  'bank',
                  'condition']
    j = random.randint(0, len(dictionary) - 1)
    initial_word = dictionary[j]
    game(initial_word)


def check_letter(check_word, letter):
    """" check_letter"""
    for i in check_word:
        if letter == i:
            letter_check = 1
            break
        letter_check = 0
    return letter_check


def reveal_letter(real_word, current_word, letter):
    """" reveal_letter-game"""
    k = 0
    for i in real_word:
        if i == letter:
            current_word[k] = letter
        k += 1
    return current_word


def print_result(error, real_word):
    """" print_result"""
    if error == 5:
        print("You lost!")
        print("Real word is:", real_word)
    else:
        print("You won!")


def game(word):
    """game"""
    current_word = ['*' for i in range(len(word))]
    error = 0
    while error < 5 and '*' in current_word:
        print('Guess a letter:')
        input_letter = input()
        print(' ')
        letter_check = check_letter(word, input_letter)
        if letter_check == 1:
            print('Hit!')
            current_word = reveal_letter(word, current_word, input_letter)
        if letter_check == 0:
            error += 1
            print("Missed, mistake", error, "out of 5")
        print("The word: ", end='')
        for letter in current_word:
            print(letter, end='')
        print(' ')
        print(' ')
    print_result(error, word)
