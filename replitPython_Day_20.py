print('This is a list generator!')
print()

startingNumber = int(input('What is your starting number? '))
maxNumber = int(input('What is your max number? '))
increment = int(input('What is the increment you want? '))
print()    
            
for i in range(startingNumber,maxNumber+increment,increment):
    print(i)