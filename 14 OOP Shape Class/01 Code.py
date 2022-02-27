import math

shapes = []
shape_names = []

class shape: #Class
    def __init__(self,length=0,name='',shape_type=''): #Constructor
        if name == '':
            self.name = input('What would you like to name this shape? ')
            shape_names.append(self.name)
        else:
            self.name = name
        self.shape_type = shape_type
        self.length = length #Attribute
    def view_shapes(self): #Inherited method
        print('Shapes:')
        print(shape_names)
        print()

class square(shape): #Subclass
    def __init__(self,length=0,name=''):
        length = int(input('Enter the square side length: '))
        super().__init__(length,shape_type='square',name=name) #Inheritance
        self.__area = self.length**2 #Private attribute
        print()
    def dimensions(self): #Method
        print()
        print(self.name + ' dimensensions:')
        print()
        print('Length =', self.length)
        print('Area =', self.__area) #Encapsulation
        print()

class circle(shape):
    def __init__(self,radius=0,name=''): #Overwriting
        radius = int(input('Enter the radius: '))
        super().__init__(shape_type='circle',name=name)
        self.__radius = radius
        self.__area = math.pi*(self.__radius**2)
        print()
    def dimensions(self): #Getter
        print()
        print(self.name + ' dimensensions:')
        print()
        print('Radius =', self.__radius)
        print('Area =', self.__area)
        print()

class triangle(shape):
    def __init__(self,length=0,height=0,name=''): #Setter
        length = int(input('Enter the base length: '))
        height = int(input('Enter the height: '))
        super().__init__(length,shape_type='triangle',name=name)
        self.__height = height
        self.__area = 0.5 * self.length * self.__height
        print()
    def dimensions(self): #Polymorphism
        print()
        print(self.name + ' dimensensions:')
        print()
        print('Base length =', self.length)
        print('Height =', self.__height)
        print('Area =', self.__area)
        print()

def menu():
    menu = int(input('''Choose an option:

1. Create a square
2. Create a circle
3. Create a triangle
0. Exit

'''))
    if menu == 1:
        create('square')
    elif menu == 2:
        create('circle')
    elif menu == 3:
        create('traingle')

def create(shape_type):
    print()
    if shape_type == 'square':
        shape = square()
        shapes.append(shape) #Initialisation of object
    elif shape_type == 'circle':
        shape = circle()
        shapes.append(shape)
    else:
        shape = triangle()
        shapes.append(shape)
    print()
    stop = False
    while stop == False:
        print('Current shape: '+shape.name)
        print()
        choice = int(input('''Choose an option:

1. View dimensions
2. Edit dimensions
3. Create a new shape
4. Switch to a different shape
0. Exit

'''))
        if choice == 1:
            shape.dimensions() #Getting public/private attributes
        elif choice == 2:
            print()
            shape.__init__(name=shape.name) #Overwriting the object
        elif choice == 3:
            print()
            menu()
            stop = True
        elif choice == 4:
            print()
            for x in range(0,len(shapes)):
                print(x,': ',shapes[x].name)
            print()
            selection = int(input('Choose a shape: '))
            shape = shapes[selection]
            shape_type = shape.shape_type
            print()
        else:
            stop = True

menu()






    
