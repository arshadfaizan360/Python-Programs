### In order to flip the list, a stack has been used.
### First, the program itterates through each item in the list in order and adds them to the stack.
### This is done using a for loop as the index looping between 0 and the length of the list
### Noe first item is at the bottom of the stack and the last item is at the top if the stack.
### The program then adds each item back into the list, starting at the top of the stack first.
### The pointer top allows the program to know which item is at the top of the stack and adds it to the list and then decreases by 1 to acces the next item.
### This now means that the list is flipped.

def menu(list):
    option = 0
    while option != 2:
        option = int(input('''Please select an option:
        
1. Flip
2. Exit
        
'''))
        print()
        if option == 1:
            print('Original list:', list)
            print('Flipped list:', flip(list))
        elif option != 2:
            print('That is not a valid option')
        print()


def flip(list):
    stack = ['','','','','','','','','','']
    top = 0
    for x in range (0,len(list)):
        stack[top] = list[x]
        top += 1
    for x in range(0,len(list)):
        list[x] = stack[top-1]
        stack[top-1] = ''
        top -= 1
    return list

menu(['apple','banana','orange','pineapple','plum','strawberry','grape','pear','peach','watermelon'])