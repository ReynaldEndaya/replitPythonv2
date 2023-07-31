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
print()

print(characterName_2)
time.sleep(1)
print('Health:',health_2)
time.sleep(1)
print('Strength:',strength_2)
time.sleep(1)
print()

round_counter = 0

while True:
    
    os.system('clear')
    print('⚔️ Battle Time ⚔️')
    print()
    print('The Battle Begins')
    print()
    
    round_counter += 1
    
    character_1_roll_dice = rollDice(6)
    character_2_roll_dice = rollDice(6)
    
    damage = abs(strength_1 - strength_2) + 1
    
    if character_1_roll_dice > character_2_roll_dice:
      health_2 = health_2 - damage
      print(characterName_1,'wins round',round_counter,'!')
      print(characterName_2,'takes a hit with',damage,'damage')
    else:
      health_1 = health_1 - damage
      print(characterName_2,'wins round',round_counter,'!')
      print(characterName_1,'takes a hit with',damage,'damage')
      
    time.sleep(1)
    print()
    print(characterName_1)
    print('Health:',health_1)
    time.sleep(1)
    print()
    print(characterName_2)
    print('Health:',health_2)
    
    
    if health_1 > 0 and health_2 > 0:
      time.sleep(1)
      print()
      print('And they\'re both standing for the next round!')
      time.sleep(3)
      continue
    elif health_1 > health_2:
      print()
      print('Oh no',characterName_2,'has died!')
      print(characterName_2,'wins the game in',round_counter,'rounds!')
      break
    else:
      print()
      print('Oh no',characterName_1,'has died!')
      print(characterName_1,'wins the game in',round_counter,'rounds!')
      break