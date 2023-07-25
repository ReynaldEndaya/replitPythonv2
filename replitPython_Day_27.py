# Write a subroutine that generates a character: first name and character type (human, imp, wizard, elf, etc.).
# Write a subroutine that multiplies a bunch of random dice rolls together to generate the character's health stats. Use this formula:
# (6 sided roll * 12 sided roll)/2 + 10
# Write a second subroutine that multiplies a bunch of random dice rolls together to generate the character's strength stats. Use this formula:
# (6 sided roll * 12 sided roll)/2 + 12
# Present the data in a menu with time.sleep and os.system("clear") to make it appealing.
# Wrap it in a loop so the user has the option to create another character.

import random, time, os


def rollDice(sides):
  number = random.randint(1, sides)
  return number

def healthStatsCreator():
  health = (rollDice(6) * rollDice(12))/2 + 10
  return health

def strengthStatsCreator():
    strength = (rollDice(6) * rollDice(12))/2 + 12
    return strength

def characterProfile():
    characterName = input('Name your legend: ')
    characterType = input('Character Type (Human, Elf, Wizard, Orc): ')
    return characterName

while True:
    print('Character Builder')
    
    print()
    characterName = characterProfile()    
    health = healthStatsCreator()
    strength = strengthStatsCreator()
    print()
    
    print(characterName)
    time.sleep(1)
    print('Health:',health)
    time.sleep(1)
    print('Strength:',strength)
    print()
    print('May your name go down in legend!')