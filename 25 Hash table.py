class Hash_table:
    def __init__(self):
        while True:
            try:
                self.length = int(input('How many items do you want to be able to store in this hash table? '))
                break
            except:
                print('That is not a valid option')
        self.table = [['',-1] for x in range (self.length)]
        #0th index is data, 1st index  is key
        print()
        
    def add(self):
        data = input('What data would you like to add? ')
        while True:
            try:
                key = int(input('Enter the key: '))
                break
            except:
                print('That is not a valid option')
        index = 0
        for x in str(key):
            index += int(x)
        index = index % self.length
        while self.table[index][1] != -1:
            if self.table[index][1] == key:
                print('That key has already been used')
                index = -1
                break
            elif index == self.length-1:
                print('This index is full')
                index = -1
                break
            else:
                index += 1
        if index != -1:
            self.table[index] = data,key
        print()
        
    def search(self):
        key = int(input('Enter the key: '))
        index = 0
        for x in str(key):
            index += int(x)
        index = index % self.length
        while True:
            if self.table[index][1] == -1:
                print('That index is empty')
                print()
                break
            elif self.table[index][1] != key:
                if index == self.length - 1:
                    print('The key cannot be found')
                    print()
                    break
                else:
                    index += 1
            else:
                print('Data: ' + self.table[index][0])
                print()
                break
            
    def view(self):
        for x in range (self.length):
            if self.table[x][1] != -1:
                print('Index:', x)
                print('Data: ' + self.table[x][0])
                print('Key:', self.table[x][1])
                print()
            
hash_table = Hash_table()
choice = 1
while choice != 0:
    try:
        choice = int(input('''Menu:

1) Add an item to the hash table
2) View the hash table
3) Search using key
0) Exit

'''))
        if choice == 1:
            print()
            hash_table.add()
        elif choice == 2:
            print()
            hash_table.view()
        elif choice == 3:
            print()
            hash_table.search()
        elif choice != 0:
            print('That is not a valid option')
            print()
    except:
        print('That is not a valid option')
        print()