count = 1
num = 2
while count < 10001:
    num += 1
    prime = True
    for x in range (2,num//2+1):
        if num % x == 0:
            prime = False
            break
    if prime == True:
        count += 1
        print(count)
print(num)