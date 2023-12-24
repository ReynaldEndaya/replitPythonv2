# Build a really cool to do list manager. (I know we did this before...hold on!)

# We are going to upgrade the last to do list manager we created:

# Create a menu where the user can view, add, or remove an item.
# The user should be able to edit the text of an item on the list too.
# Don't allow the user to add duplicates.
# Double check with the user they want to remove an item from the list before it is actually removed. (Is this the item they really want to remove?)
# Give the user the option to completely erase the to do list. (You should be able to do this in one line of code!)

import os, time

listName = ['a','b','c']
addNewTask = ''

def printList():
    os.system('clear')
    counter = 0
    print('Here is your to do list:')
    print()
    for item in listName:
        counter += 1
        print(f'{counter}. ',end='')
        print(item)
    print()

# function to create list
def createList(): 
    os.system('clear')
    addNewTask=''
    item = input('What\'s in the agenda? ')
    listName.append(item)
    print()
    print('Here\'s your new to do list: ')
    print()
    for item in listName:
        print(item)
    print()
        
def editList():
    print()
    print('Current task list:')
    printList()
    taskToEdit = input('Which task do you want to edit? ')
    if taskToEdit in listName:
        index = listName.index(taskToEdit)
        listName[index] = input('Enter new task: ')
    else:
        print('Task not in List')

def removeItem():
    print()
    print('Current task list:')
    printList()
    taskToDelete = input('Which task do you want to delete? Type "ALL" to delete all tasks:  ')
    if taskToDelete == 'ALL':
        confirmation = input('Are you sure you want to delete ALL tasks? (y|n): ')
        if confirmation == 'y':
            listName = []
        else:
            
            index = listName.index(taskToDelete)
            confirmation == input(f'Are you sure you want to remove {taskToDelete}? ')
                if confirmation == 'y':
                    listName[index].remove()
                else:
                    
            
        
# main code
print('To do List Manager')
print()
while True:
    option = input('(V)iew, (A)dd, (E)dit, or (R)emove an item from your to do list? ')
    if option.lower() == 'v':
        printList()
    elif option.lower() == 'a':
        while True:
            createList()
            addNewTask = input('Add more task? (y) or (n): ')
            print()
            if addNewTask.lower() == 'y':
                continue
            else: 
                break
    elif option.lower() == 'e':
        editList()
    elif option.lower() == 'r':
        
        listName = []
    else:
        print('No action selected! Exiting now...')
        break
    