list = [600851475143]
changed = True
while changed == True:
    changed = False
    for x in list:
        for y in range (2, x):
            if x % y == 0:
                list.remove(x)
                list.append(y)
                list.append(x//y)
                changed = True
                break
print(list)