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
    os.system('clear')
    print('⚔️ Battle Time ⚔️')
    
    print()
    characterName_1 = characterProfile()
    health_1 = healthStatsCreator()
    strength_1 = strengthStatsCreator()
    print()
    
    print(characterName_1)
    time.sleep(1)
    print('Health:',health_1)
    time.sleep(1)
    print('Strength:',strength_1)
    time.sleep(1)
    print()
    print()
    time.sleep(1)
    
    print('Who are they battling?')
    
    print()
    characterName_2 = characterProfile()
    health_2 = healthStatsCreator()
    strength_2 = strengthStatsCreator()
    
    print(characterName_2)
    time.sleep(1)
    print('Health:',health_2)
    time.sleep(1)
    print('Strength:',strength_2)
    time.sleep(1)
    print()
    
    os.system('clear')
    print('⚔️ Battle Time ⚔️')
    print()
    print('The Battle Begins')
    print()
    
    if 
    
    
    