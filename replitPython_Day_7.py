print('Are you an attack of titan fan???')

show = input('''Which do you like more? Choose the number only:
             
(1) AoT 
(2) Wanpanman

''')

if show == '1':
    attackTitan = input('Who is the attack titan when the show started? ')
    if attackTitan == 'grisha':
        print('Wow! that\'s correct!')
    elif attackTitan == 'eren':
        print('Not quite! Eren only got the attack titan after the attack on Wall Maria')
    else:
        print('Not even close sorry!')
elif show == '2':
    personSaved = input('Who did Saitama saved that led to the founding of the Hero Association?' )
    if personSaved == 'son of founder':
        print('That\'s correct! You really are a Wanpanman fan!')
    else:
        print('Wrong he saved the founder\'s son')
else:
    print('Sorry that\'s not part of the options!')
              
    