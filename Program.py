import random

number = random.randint(1,10)
guess = int(input('Guess any number from 1-10 :'))

while guess != number:
    if guess < number:
        print('Try guesssing higher')
        guess = int(input('Guess any number from 1-10 :'))
    else:
        print('try guessing lower ')
        guess = int(input('Guess any number from 1-10 :'))


if guess == number:
    print('Congrats! You guessed the correct number')
 