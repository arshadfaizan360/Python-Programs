def same_num(cards):
    total = 0
    for x in range (0,4):
        for y in range (x+1,5):
            if cards[x] == cards [y]:
                total += 1
    return total

def sum15(cards):
    total = 0
    for x in range (0,4):
        for y in range (x+1,5):
            if cards[x] + cards [y] == 15:
                total += 1
    for x in range (0,3):
        for y in range (x+1,4):
            for z in range (y+1,5): # x+2 changed to y+1
                if cards[x] + cards[y] + cards[z] == 15:
                    total += 1
    for x in range(0,2):
        for y in range(x+1,3):
            for z in range (y+1,4): # x+2 changed to y+1
                for a in range (z+1,5): #x+3 changed to z+1
                    if cards[x] + cards[y] + cards[z] + cards[a] == 15:
                        total += 1
    num = 0
    for x in cards:
        num += x
    if num == 15:
        total += 1
    return total



cards = []
points = 0

for x in range (0,5):
    cards.append(int(input('Enter a number between 1 and 10 ')))

points += same_num(cards)
points += sum15(cards)
print(points)

#Q1B - 1,3,6,7,10
#Q1C - 28
