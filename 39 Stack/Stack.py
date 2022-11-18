class stack:
    def __init__ (self):
        self._stack = [[]]
        self._top = 0

    def _push(self, item):
        self._stack[self._top] = item
        if self._top == len(self._stack) - 1:
            self._stack.append([])
        self._top += 1

    def _pop(self):
        if self._top == 0:
            return False
        else:
            self._top -= 1
            temp = self._stack[self._top]
            self._stack[self._top] = []
            return temp

    def menu(self):
        option = 1
        while option != 0:
            print('Please select an option:')
            print()
            print('1. Push to the stack')
            print('2. Pop from the stack')
            print('0. Quit')
            print()
            while True:
                try:
                    option = int(input('Please select an option: '))
                    print()
                    break
                except:
                    print('That is not a valid option')
                    print()
            if option == 1:
                city = input('Enter the name of a city: ')
                while True:
                    try:
                        population = int(input('Please enter the population: '))
                        males = float(input('Please enter the males (% of total): '))
                        print()
                        break
                    except:
                        print('That is not a valid option')
                        print()
                self._push([city, population, males])
            elif option == 2:
                city = self._pop()
                if city == False:
                    print('The stack is empty')
                else:
                    print('City: ' + city[0])
                    print('Population: ', city[1])
                    print('Males (% of total): ', city[2])
                    print()

stack = stack()
stack.menu()