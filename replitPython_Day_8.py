print('Affirmation Generator!')

name = input('What is your name? ')

if name.lower() == 'reynald':
    currentDay = input('What day is it today? ')
    if currentDay.lower() == 'monday':
        faveFood = input('What is your favorite food? ')
        print('First workday of the week! Make sure you\'ve packed your',faveFood,'good luck on your day!')
    elif currentDay.lower() == 'tuesday':
        faveBook = input('What is your favorite book? ')
        print('Almost to the hump day!',name.capitalize(),'when you get home tonight find some time to read',faveBook,'it\'s a good way to unwind!')
    elif currentDay.lower() == 'wednesday':
        faveAnime = input('What anime are you currently watching? ')
        print('Happy hump day!',name.capitalize(),'tonight you must rest and watch',faveAnime,'you\'ve survived half of the week already!')
    elif currentDay.lower() =='thursday':
        faveSports = input('What sports do you usually play? ')
        print('Happy',currentDay,'the week is almost over',name.capitalize(),'so make sure you spend some time playing',faveSports,'today!')
    elif currentDay.lower() =='friday':
        faveHangoutSpot = input('Where do you usually hangout? ')
        print('You survived one week!',name.capitalize(),'It\'s now time to go out with friends at the',faveHangoutSpot,'have fun!')
    elif currentDay.lower() =='saturday':
        faveGame = input('What video game are you playing right now? ')
        print('Nothing to do!',name.capitalize(),'Make sure you level up today in',faveGame,'beat all of them!')
    elif currentDay.lower() =='sunday':
        print('Just take a rest for today!')
    else:
        print('Invalid Day')
else:
    print('Invalid User')