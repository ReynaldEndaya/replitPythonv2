print('Strix Login System')

def login():
    
    while True:

        username = input('Username: ')
        password = input('Password: ')
            
        if username.lower() == 'reynald' and password == 'reynald3':
            print('Welcome Reynald')
            break
        else:
            print('Invalid Credentials')
            continue
        
login()
    