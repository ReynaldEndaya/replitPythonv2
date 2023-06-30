print('This is an animal sounds simulator!')
print()

exit = ''

while exit != 'yes':
    animal = input('What animal do you want? ')
    if animal.lower() == 'dog':
        print('Dog says aw aw aw!')
    elif animal.lower() == 'cat':
        print('Cat says meow meow!')
    elif animal.lower() == 'cow':
        print('Cow says moo!')
    else:
        print('That animal is not in my database yet!')
    exit = input('Do you want to exit? ')
