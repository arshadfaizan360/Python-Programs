num = 0
divisible = False
while divisible == False:
    num += 20
    print(num)
    divisible = True
    for x in range (11,21):
        if num % x != 0:
            divisible = False
            break
print(num)