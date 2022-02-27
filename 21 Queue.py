queue = ["","","","",""]
front = 0
back = 0

def full(queue):
    for x in queue:
        if x == "":
            return False
    print('The queue is full')
    return True

def insert(queue, back):
    if full(queue) == False:
        item = input('What would you like to insert into the queue? ')
        if back == len(queue):
            back = 0
        queue[back] = item
        back += 1
        return back      
        
def view(queue, front, back):
    print(queue)
    print('Front:', front)
    print('Back:', back)
    
def delete(queue, front, back):
    if front == back:
            print('The queue is empty')
        else:
            print(queue[front] + ' was deleted')
            queue[front] = ""
            front += 1
            return front
        
def menu(queue, front, back):
    while True:
        option = int(input('''Choose an option:

1. Insert an item to the back of the queue
2. Delete an item from the front of the queue
3. View the queue
0. Quit
'''))
        print()
        if option == 1:
            back = insert(queue, back)
        elif option == 2:
            front = delete(queue, front, back)
        elif option == 3:
            view(queue, front, back)
        else:
            break
        
menu(queue, front, back)