print('This program will compute how many seconds in a year!')
print()
year = int(input('What year do you want to compute for? '))

if year % 4 == 0:
    seconds = 366 * 24 * 60 * 60
    print('There are',seconds,'seconds in year',year)
else:
    seconds = 365 * 24 * 60 * 60
    print('There are',seconds,'seconds in year',year)