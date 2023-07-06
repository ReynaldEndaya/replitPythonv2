print('Welcome to Math Facts!')
print()

number = int(input('Name your multiples: '))
score = 0

for counter in range(1,11):
    print(counter,' x ',number,'= ',end='')
    answer = int(input())
    if answer == counter * number:
        print('Great work! That\'s correct!')
        print()
        score += 1
        continue
    else:
        print('Sorry that\'s wrong. Correct answer is',counter*number)
        print()

print('You got ',score,' out of 10')
print()
    