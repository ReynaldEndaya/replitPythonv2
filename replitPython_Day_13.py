print('This is a grade generator!')
print()

testName = input('What is the name of the test? ')
maxScore = int(input('What is the max score for this test? '))
yourScore = int(input('What is your score? '))

percentage = float(round(yourScore/maxScore,2)) * 100

if percentage >= 90:
    print('Your grade percentage is',percentage,'and you get an A+')
elif percentage >= 80 and percentage < 90:
    print('Your grade percentage is',percentage,'and you get an A')
elif percentage >= 70 and percentage < 80:
    print('Your grade percentage is',percentage,'and you get a B')
elif percentage >= 60 and percentage < 70:
    print('Your grade percentage is',percentage,'and you get a C')
elif percentage >= 50 and percentage < 60:
    print('Your grade percentage is',percentage,'and you get a D')
else:
    print('Your grade percentage is',percentage,'and you get a U')