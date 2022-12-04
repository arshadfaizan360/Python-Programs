sum = 2
for x in range(3,2000000):
    print(x)
    prime = True
    for y in range(2,int(x**0.5+1)):
        if x % y == 0:
            prime = False
            break
    if prime == True:
        sum += x
print(sum)