print('This is a lyrics guessing game')
print()

tries = 0
while True:
    tries += 1
    print('Save ______, fight the break of dawn!')
    print()
    missingWord = input('What is the missing word? ')
    print()
    if missingWord.lower() == 'tonight':
        print('That is correct! You only needed',tries,'guess(es)')
        break
    else: 
        print('Nope, try again!')
print()
print('Thank you for playing!')
    
    
    
    

