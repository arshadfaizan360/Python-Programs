names = ['Ben','Thor','Zoe','Kate']
Max = 4
current = 0
found = False
playerName = input('What player are you looking for? ')
while found == False and current < Max:
    if names[current] == playerName:
        found = True
    else:
        current += 1
if found == True:
    print('Yes, they have a top score')
else:
    print('No, they do not have a top score')
