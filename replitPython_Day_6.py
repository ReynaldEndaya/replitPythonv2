print('This is a secure zone! Only people with registered username and password are allowed!')

username = input('Enter your username: ')
password = input('Enter your password: ')

if username == 'reynald' and password == 'reynaldpass':
    print('Welcome Reynald!')
elif username == 'agatha' and password == 'agathapass':
    print('Welcome Agatha!')
elif username == 'meowy' and password == 'meowypass':
    print('Welcome meowy!')
else:
    print('You are not authorized to access this system!')