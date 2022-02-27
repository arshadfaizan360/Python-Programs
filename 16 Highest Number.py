def highest_number(num1,num2,num3):
    if num1 >= num2 and num1 >= num3:
        print(num1, 'is the highest number.')
    elif num2 >= num3:
        print(num2, 'is the highest number.')
    else:
        print(num3, 'is the highest number.')

num1 = int(input('Enter a number '))
num2 = int(input('Enter another number '))
num3 = int(input('Enter a third number ')) 
highest_number(num1,num2,num3)