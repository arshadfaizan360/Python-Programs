#Initialising global variables

class queue:
    def __init__(self):
        self.length = int(input('How items long do you want the queue to be: '))
        self.queue = [['','','',0] for x in range(self.length)]
        self.front = 0
        self.back = 0
        print()
# 
#     #Adds items to the queue
#     def enqueue(self):
#         #Checks if queue is full
#         if self.front == self.back and self.queue[0] != ['','','',0]:
#             print('The queue is full')
#             print()
#         else:
#             self.queue[self.back][0] = input('What is the name of the game: ')
#             #Does not add item to queue if name is left blank
#             if self.queue[self.back][0] == '':
#                 print('Not added')
#                 print()
#             else:
#                 self.queue[self.back][1] = input('Who is the developer of the game: ')
#                 self.queue[self.back][2] = input('What is the genre of the game: ')
#                 print('Added')
#                 print()
#                 #Increments back of the queue
#                 if self.back == (self.length - 1):
#                     self.back = 0
#                 else:
#                     self.back += 1
                    
    def enqueue(self):
        if self.front == self.back and self.queue[0] != ['','','',0]:
            print('The queue is full')
            print()
        else:
            self.queue[self.back][0] = input('What is the name of the game: ')
            if self.queue[self.back][0] == '':
                print('Not added')
                print()
            else:
                self.queue[self.back][1] = input('Who is the developer of the game: ')
                self.queue[self.back][2] = input('What is the genre of the game: ')
                while True:
                    try:
                        self.queue[self.back][3] = int(input('Enter 1 for AAA or 2 for F2P: '))
                        if self.queue[self.back][3] != 1 and self.queue[self.back][3] != 2:
                            print('That is not a valid option.')
                        else:
                            break
                    except:
                        print('That is not a valid option.')
            if self.queue[self.back][3] == 1:
                current = self.back
                if current == 0:
                    nextItem = self.length-1
                else:
                    nextItem = current - 1
                while self.queue[nextItem][3] == 2 and current != self.front:
                    temp = self.queue[nextItem]
                    self.queue[nextItem] = self.queue[current]
                    self.queue[current] = temp
                    current = nextItem
                    if current == 0:
                        nextItem = self.length-1
                    else:
                        nextItem = current - 1
            print('Added')
            print()
            if self.back == (self.length - 1):
                self.back = 0
            else:
                self.back += 1
    
    #Removes items from the queue        
    def dequeue(self):
        #Checks if queue is empty
        if self.front == self.back and self.queue[0] == ['','','',0]:
            print('The queue is empty')
            print()
        else:
            #Outputs item being removed
            self.show(self.front)
            self.queue[self.front] = ['','','',0]
            #Increments front by 1
            if self.front == (self.length - 1):
                self.front = 0
            else:
                self.front += 1

    #Displays the queue
    def display(self):
        print()
        print('Front')
        print()
        #x is temp var used to indicate item being outputted
        x = self.front
        #Stops if back of the queue is reached
        stop = False
        #Increments from front of queue to end of array
        while x != self.length and not stop:
            stop = self.show(x)
            x += 1
        x = 0
        #Increments from start of array to front of queue
        while x != self.front and not stop:
            stop = self.show(x)
            x += 1
        print('Back')
        print()
        print()
            
    #Ouputs item in queue (indicated by ordinal parameter x)
    def show(self, x):
        empty = 0
        original = x
        #If back of the queue is reached, program will count and output number of empty spaces remaining
        while self.queue[x][0] == '':
            empty += 1
            if x == (self.length - 1):
                x = 0
            else:
                x += 1
            if x == original:
                break
        if empty != 0:
            print('Empty x' + str(empty))
            print()
            return True
        #Outputs item
        else:
            print('Game: ' + self.queue[x][0])
            print('Developer: ' + self.queue[x][1])
            print('Genre: ' + self.queue[x][2])
            if self.queue[x][3] == 1:
                print('Priority: AAA')
            else:
                print('Priority: F2P')
            print()
            return False

    #Menu - self explanatory :-)
    def menu(self):
        choice = 1
        while choice != 0:
            choice = int(input('''Menu
1. Add an item to the queue
2. Remove an item from the queue
3. View the queue
0. Quit

Please choose an option: '''))
            print()
            if choice == 1:
                self.enqueue()
            elif choice == 2:
                self.dequeue()
            elif choice == 3:
                self.display()

queue = queue()
queue.menu()