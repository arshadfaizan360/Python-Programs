class Tree:
    def __init__(self):
        self.length = int(input('How many items long do you want your tree to be? '))
        self.pointer = 0
        self.tree = [[-1,-1,-1] for x in range (self.length)]
        #Index 0 is left pointer
        #Index 1 is data
        #Index 2 is right pointer
        
    def add(self):
        if self.pointer == self.length:
            print('The tree is full')
        else:
            data=int(input('What number would you like to add to the tree? '))
            if self.pointer > 0:
                found = False
                checking = 0
                while not found:
                    if self.tree[checking][1] == data:
                        print('Already in the tree')
                        found = True
                    elif self.tree[checking][1] > data:
                        if self.tree[checking][0] == -1:
                            self.tree[checking][0] = self.pointer
                            self.tree[self.pointer][1] = data
                            self.pointer += 1
                            found = True
                        else:
                            checking = self.tree[checking][0]
                    else:
                        if self.tree[checking][2] == -1:
                            self.tree[checking][2] = self.pointer
                            self.tree[self.pointer][1] = data
                            self.pointer += 1
                            found = True
                        else:
                            checking = self.tree[checking][2]
            else:
                self.tree[self.pointer][1] = data
                self.pointer += 1
                        
    def view(self):
        for x in range(0, self.length):
            print(str(x) + ')')
            if self.tree[x][1] == -1:
                print('Data: Empty')
            else:
                print('Data: ' + str(self.tree[x][1]))
            if self.tree[x][0] == -1:
                print('Left: Empty')
            else:
                print('Left: ' + str(self.tree[x][0]))
            if self.tree[x][2] == -1:
                print('Right: Empty')
            else:
                print('Right: ' + str(self.tree[x][2]))
            print()
        
tree = Tree()
exit = False
while not exit:
            try:
                print()
                option = int(input('''Menu:
1) Add a number to the tree
2) View the tree
0) Exit

Enter your choice here: '''))
                print()
                if option == 1:
                    tree.add()
                elif option == 2:
                    tree.view()
                elif option == 0:
                    exit = True
                else:
                    print('That is not a valid option')
            except:
                print('That is not a valid option')
