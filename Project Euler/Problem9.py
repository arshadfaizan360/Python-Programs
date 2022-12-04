found = False
for a in range(1,1000):
    for b in range(1,1000):
        c = 1000 - a - b
        if a**2 + b**2 == c**2:
            found = True
            abc = a * b * c
            break
    if found == True:
        break
print(abc)