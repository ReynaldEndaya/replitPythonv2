
def colorizer(color):
    if color == 'red':
        return "\033[0;31m"
    elif color == 'yellow':
        return "\033[1;33m"
    elif color == 'white':
        return "\033[1;37m"
    elif color == 'blue':
        return "\033[0;34m"
    elif color == 'green':
        return "\033[0;32m"
    elif color == 'purple':
        return "\033[0;35m"
    else:
        return "\033[0;30m"
    
header = f"{colorizer('red')}={colorizer('white')}={colorizer('blue')}= {colorizer('else')}Music App {colorizer('red')}={colorizer('white')}={colorizer('blue')}="
headerLength = int(len(header))+20

print(f"{header: ^{headerLength}}")
print()
print('🔥▶️',f"{'Radio Gaga': ^12}")
print(f"{colorizer('yellow')}",f"{'Queen': ^13}")
print(colorizer('else'))
print('PREV')
print(f"{colorizer('green')}",f"{'NEXT': ^12}")
print(f"{colorizer('purple')}",f"{'PAUSE': ^23}")

# Interface 2
print()
print()
print(colorizer('else'))
print(f"{'WELCOME TO' : ^50}")
print(f"{colorizer('blue')}",f"{'--    ARMBOOK    --': ^48}")
print(colorizer('yellow'))
print(f"{'Definitely not a ripoff of': >50}")
print(f"{'a certain other social': >50}")
print(f"{'networking site': >50}")
print(colorizer('red'))
print(f"{'Honest.': ^50}")
print(colorizer('white'))
print(f"{'Username:' : ^50}")
print(f"{'Password:' : ^50}")
print()