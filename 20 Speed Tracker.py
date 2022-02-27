def num_plate():
    num_plate = input('Enter the number plate without any spaces: ')
    valid = True
    if len(num_plate) == 7:
        for y in range(0,2):
            x = num_plate[y]
            if x.isalpha() == False:
                valid = False
        for y in range(2,4):
            x = num_plate[y]
            if x.isnumeric() == False:
                valid = False
        for y in range(4,7):
            x = num_plate[y]
            if x.isalpha() == False:
                valid = False
    else:
        valid = False
    if valid == True:
        print('That is a valid number plate')
    else:
        print('That is not a valid number plate')    


def speed():
    print('Enter the time the car went past the speed camera:')
    hours1 = int(input('Hours: '))
    minutes1 = int(input('Minutes: '))
    print()

    print('Enter the time the car went past the next speed camera:')
    hours2 = int(input('Hours: '))
    minutes2 = int(input('Minutes: '))

    time = (hours2 - hours1) + ((minutes2 - minutes1)/60)
    speed = 1/time

    print('The car was travelling at an average speed of', speed, 'mph')
    
choice = input('''Choose an option:
1. Find average speed
2. Check if number plate is valid
0. Quit
''')
print()
if choice == '1':
    speed()
elif choice == '2':
    num_plate()