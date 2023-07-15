# Let's extend Day 24's project and create a health stats generator for a character in a video game.

# 1. Create a subroutine that rolls a dice of any size and returns that number.
# 2. Then, create a second subroutine that rolls one six-sided dice and one eight-sided dice.
# 3. Multiply the number from the six-sided dice and eight-sided dice together and return that subroutine as a character's health stats for a video game.
# 4. Print out the character's health stats.
# 5. Add a loop to give the user the option to generate health stats for another character.

import random

def rollDice(sides):      
    number = random.randint(1,sides)
    return number

def healthStatsCreator():
    health = rollDice(6) * rollDice(8)
    return health
    
while True:
    
    warriorName = input('Name your warrior: ')
    warriorHealth = healthStatsCreator()
    print('Their health is',warriorHealth)
    newCharacter = input('Generate another character? y|n: ')
    if newCharacter.lower() == 'y':
        continue
    else:
        break