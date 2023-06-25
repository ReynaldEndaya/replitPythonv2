print('WanPanMan Character Generator')
print('Remember, answer with yes or no only!')

character = input('Can you defeat your enemies with one punch? ')

if character == 'yes':
    print('Hello Saitama!')
elif character == 'no':
    character = input('Are you an overpowered cyborg but is always turned into scrap? ')
    if character == 'yes':
        print('Hello Genos!')
    elif character == 'no':
        character = input('Are you known for your "engine"? ')
        if character == 'yes':
            print('Hello King!')
        elif character == 'no':
            print('I don\'t know what you are but I sure hope I get to know you!')
        else:
            print('Wrong Input friend!')
    else:
        print('Wrong Input friend!')
else:
    print('Wrong Input friend!')