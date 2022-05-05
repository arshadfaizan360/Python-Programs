num = int(input('Please enter a decimal number to convert to binary: ')) #Prompt displayed and value input by user stored into appropriate name
binary = ''

while num != 0: #Indefinite loop used and correct condition to terminate the loop
    binary = str(num % 2) + binary #Remainder of integer division calculated and sensible method to reverse order and after each iteration remainder digit stored into string
    num = num // 2 #Result of integer division stored to variable
#Correct identification of commands inside and outside the loop

print('The binary equivalent of that number is: ' + binary) #Remainder of integer division outputed to the screen and bits output in correct order

#14/14