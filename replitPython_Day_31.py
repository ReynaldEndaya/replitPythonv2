
def colorizer(color):
    if color == 'red':
        return "\033[0;31m"
    elif color == 'yellow':
        return "\033[1;33m"
    elif color == 'white':
        return "\033[1;37m"
    elif color == 'blue':
        return "\033[0;34m"
    else:
        return "\033[0;30m"
    
header = f"{colorizer('red')}={colorizer('white')}={colorizer('blue')}= {colorizer('else')}Music App {colorizer('red')}={colorizer('white')}={colorizer('blue')}="
headerLength = int(len(header))+20
queen = f"{colorizer('yellow')}Queen"

print(f"{header: ^{headerLength}}")
print()
print('🔥▶️',f"{'Radio Gaga': ^12}")
print(f"{queen: ^22}")
