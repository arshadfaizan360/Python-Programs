answer = 0
column = 8
while column >= 1:
    bit = int(input('Enter bit value: '))
    answer += column * bit
    column //= 2
print('Decimal value is:', answer)
