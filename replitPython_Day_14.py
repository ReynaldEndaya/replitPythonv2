from getpass import getpass as input

print('Welcome to the Rock Paper Scissor')
print()

playerOne = input('Player 1: (R)ock, (P)aper, or (S)cissor: ')
playerTwo = input('Player 2: (R)ock, (P)aper, or (S)cissor: ')

if playerOne.lower() == playerTwo.lower():
    if playerOne.lower() == 's':
        print('You both chose Scissor. It\'s a tie!')
    elif playerOne.lower() == 'r':
        print('You both chose Rock. It\'s a tie!')
    else:
        print('You both chose Paper. It\'s a tie!')
elif playerOne.lower() == 'r' and playerTwo.lower() == 's':
    print('Player 1 chose Rock and Player 2 chose scissor. Player 1 Wins!')
elif playerOne.lower() == 's' and playerTwo.lower() == 'p':
    print('Player 1 chose Scissor and Player 2 chose Paper. Player 1 Wins!')
elif playerOne.lower() == 'p' and playerTwo.lower() == 'r':
    print('Player 1 chose Paper and Player 2 chose Rock. Player 1 Wins!')
elif playerTwo.lower() == 'r' and playerOne.lower() == 's':
    print('Player 1 chose Scissor and Player 2 chose Rock. Player 2 Wins!')
elif playerTwo.lower() == 's' and playerOne.lower() == 'p':
    print('Player 1 chose Paper and Player 2 chose Scissor. Player 2 Wins!')
elif playerTwo.lower() == 'p' and playerOne.lower() == 'r':
    print('Player 1 chose Rock and Player 2 chose Paper. Player 2 Wins!')
else:
    print('Invalid Choice')