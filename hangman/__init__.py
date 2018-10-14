import random

dictionary = ['mother',
              'father',
              'permission',
              'flight',
              'apple',
              'desire',
              'bank',
              'condition']
i = random.randint(0, len(dictionary) - 1)
initial_word = dictionary[i]


def check_letter(check_word, letter):
    for i in check_word:
        if letter == i:
            letter_check = 1
            break
        letter_check = 0
    return letter_check


def reveal_letter(real_word, current_word, l):
    for i in range(len(real_word)):
        if real_word[i] == l:
            current_word[i] = l
    return current_word


def print_result(error, real_word):
    if error == 5:
        print("You lost!")
        print("Real word is:", real_word)
        return 0
    else:
        print("You won!")
        return 1


def game(word):
    current_word = ['*' for i in range(len(word))]
    error = 0
    while error < 5 and '*' in current_word:
        print('Guess a letter:')
        a = input()
        print(' ')
        letter_check = check_letter(word, a)
        if letter_check == 1:
            print('Hit!')
            current_word = reveal_letter(word, current_word, a)
        if letter_check == 0:
            error += 1
            print("Missed, mistake", error, "out of 5")
        print("The word: ", end='')
        for l in current_word:
            print(l, end='')
        print(' ')
        print(' ')
    print_result(error, word)


game(initial_word)
