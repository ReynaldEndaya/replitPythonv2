import random

print('Roll a Dice')

def rollDice(sides):
    
    while True:
        
        number = random.randint(1,sides)
        print('You rolled ',number)
        repeat = input('Roll again? (y|n): ')
        if repeat.lower() == 'n':
            break
        else:
            continue


sides = int(input('How many sides? '))
rollDice(sides)

