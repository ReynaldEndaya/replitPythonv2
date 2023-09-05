listName = []

def printList():
    print()
    print(listName)
    print()


while True:
    item = input('What\'s in the agenda? ')
    listName.append(item)
    for item in listName:
        print(item)
    print()
