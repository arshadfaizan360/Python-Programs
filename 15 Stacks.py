class stack():
    def __init__(self, stack = ['','','','',''], top = 0):
        self.__stack = stack
        self.__top = top

    def menu(self):
        option = 1
        while option == 1 or option == 2 or option == 3:
            while True:
                try:
                    option = int(input('''Choose an option:

1. Push an item to the stack
2. Pop an item from the stack
3. View the stack
Any other number to quit
'''))
                except:
                    print('That is not an option')
                    continue
                break
            if option == 1:
                if self.__top < 5:
                    self.push()
                else:
                    print('The stack is full. You must pop an item first in order to push another')
            elif option == 2:
                if self.__top > 0:
                    self.pop()
                else:
                    print('The stack is empty. You must push an item first in order to pop it')
            elif option == 3:
                print(self.__stack)
            print()

    def push(self):
        self.__stack[self.__top] = input('What is the item you would like to push onto the stack ')
        self.__top += 1

    def pop(self):
        self.__top -= 1
        self.__stack[self.__top] = ''

stack1 = stack()
stack1.menu()