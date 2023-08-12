import random

name = input('enter your name: ')

print(f'Good luck {name}')

names = ['ahmed', 'mohamed', 'ali', 'ibrahim', 'hady', 'yara', 'arwa', 'nour']

word = random.choice(names)

x = 12

guesses = ' '

while x > 0:
    failed = 0

    for char in word:
        if char in guesses:

            print(char)
        else:
            print('_')
            failed += 1
    if failed == 0:

        print('You win')
        print(f'The name is: {word}')

        break
    guess = input('guess a character:')

    guesses += guess
    if guess not in word:
        x -= 1
        print('wrong guess')
        print(f'You have {x} more guess')

        if x == 0:
            print("you loes")







