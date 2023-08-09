#Write a subroutine that writes text in color. All it will do is print out the text in that color and turn the color back to normal when it's finished.
#Control end and sep so there are not random symbols or spaces.
#Check out this github resource for the color codes.


def colorizer(color,word):
    if color == 'red':
        print("\033[0;31m",word,sep='',end='')
    elif color == 'yellow':
        print("\033[1;33m",word,sep='',end='')
    elif color == 'cyan':
        print("\033[0;36m",word,sep='',end='')
    elif color == 'pink':
        print("\033[1;35m",word,sep='',end='')
    else:
        print("\033[0;30m",word,sep='',end='')

print("\033[1;33m",'Super Subroutine',sep='')
print()
print("\033[1;33m",'With my',end=' ',sep='')
colorizer('pink','new program')
colorizer('yellow','I can just call red("and")')
print(end=' ')
colorizer('red','and')
print(end=' ')
colorizer('yellow','that word will appear in color I set it to.')
print()
print()
colorizer('yellow','With no')
print(end=' ')
colorizer('cyan','weird gaps')
colorizer('yellow','.')
print()
print()
colorizer('yellow','Epic.')
print()