import random


print('This is a numbers guessing game!')
print()

number = random.randint(1,1000000)
attempts = 0

while True:
    numberGuess = int(input('What is your guess? '))
    attempts += 1
    if numberGuess > number:
        print('Your guess is too high. Guess again')
    elif numberGuess < number and numberGuess >=0:
        print('Your guess is too low. Guess again')
    elif numberGuess == number:
        print('That is correct! You only took',attempts,'guesses')
        break
    else:
        print('Invalid number')
        
    
