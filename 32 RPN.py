import sys

choice = ''
list = []

while choice != 'stop':
    choice = input(
        "Please enter the RPN statement one number / operator at a time or type stop once entire statment has been entered: "
    )
    if choice == 'stop':
        print()
    elif choice != '+' and choice != '-' and choice != '*' and choice != '/':
        try:
            choice = int(choice)
            list.append(choice)
        except:
            print('That is not a valid input')
    else:
        list.append(choice)


def DoOperation(operation, num1, num2):
    if operation == '+':
        return (num1 + num2)
    elif operation == '-':
        return (num1 - num2)
    elif operation == '*':
        return (num1 * num2)
    else:
        return (num1 / num2)


stack = [
    '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''
]
top = 0

pointer = 0
while pointer < len(list):
    stack[top] = list[pointer]
    pointer += 1
    if type(stack[top]) == str:
        try:
            operation = stack[top]
            stack[top] = ''
            top -= 1
            num2 = stack[top]
            stack[top] = ''
            top -= 1
            stack[top] = DoOperation(operation, stack[top], num2)
        except:
            print('There has been an error')
            sys.exit()

    top += 1

print('The answer is ' + str(stack[0]))
