from getpass import getpass as input

print('Welcome to the Rock Paper Scissor')
print()

playerOne = input('Player 1: (R)ock, (P)aper, or (S)cissor: ')
playerTwo = input('Player 1: (R)ock, (P)aper, or (S)cissor: ')

if playerOne.lower() == playerTwo.lower():
    if playerOne.lower() == 's':
        print('You both chose Scissor. It\'s a tie!')
    elif playerOne.lower() == 'r':
        print('You both chose Rock. It\'s a tie!')
    
