class fruit():

    def __init__(self, colour = 'unknown', size = 'unknown', taste = 'unknown'):
        self.__colour = colour
        self.__size = size
        self.__taste = taste

    def getting(self):
        return(self.__colour, self.__size, self.__taste)

    def print_description(self):
        print('The colour of the fruit is ' + self.__colour)
        print('The size of the fruit is ' + self.__size)
        print('The taste of the fruit is ' + self.__taste)


class tropical(fruit):

    def __init__(self, colour, size):
        super().__init__(colour, size, 'sweet')


class citrus(fruit):

    def __init__(self, colour, size, bitter_level):
        super().__init__(colour, size, 'bitter')
        self.__bitter_level = bitter_level

    def setting(self):
        self.__colour, self.__size, self.__taste = fruit.getting(self)

    def print_description(self):
        print('The colour of the fruit is ' + self.__colour)
        print('The size of the fruit is ' + self.__size)
        print('The taste of the fruit is ' + self.__taste)
        print('The bitter level of the fruit is', self.__bitter_level)


mango = tropical('red','medium')
mango.print_description()

print()

lemon = citrus('yellow','small',bitter_level=8)
lemon.setting()
lemon.print_description()
