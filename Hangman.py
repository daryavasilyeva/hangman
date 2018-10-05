import random

dictionary = ['mother', 'father', 'permission', 'flight']
i = random.randint(0, len(dictionary) - 1)
word = dictionary[i]

current_word = ['0' for i in range(len(word))]

error = 0
success_flg = 0

while error < 5 and success_flg == 0:
    print('Guess a letter:')
    success = 0
    a = input()
    print(' ')
    for i in range(len(word)):
        if a == word[i] and current_word[i] == a:
            print('You have already tried this letter!')
            break
        if a == word[i] and current_word[i] == '0':
            current_word[i] = a
            success = 1
        if i == len(word) - 1 and word[i] != a and success == 0:
            error += 1
            print("Missed, mistake", error, "out of 5")
    if success == 1:
        print("Hit!")
    print("The word: ", end = '')
    for x in current_word:
        if x == '0':
            print('*', end = '')
        else:
            print (x, end = '')
    print(' ')
    print(' ')
    if '0' not in current_word:
        success_flg = 1

if error == 5:
    print("You lost!")
    print("Real word is:", word)

else:
    print("You won!")