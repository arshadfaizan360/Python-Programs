string = input('Enter the string ')
rotations = int(input('Enter the number of rewriting steps ' ))
position = int(input('Enter the position '))


for y in range(0,rotations):
    letters = []
    for x in string:
        letters.append(x)

    string = ''
    for x in range(0,len(letters)):
        if letters[x] == 'A':
            letters[x] = 'B'
            string = string + letters[x]
        elif letters[x] == 'B':
            letters[x] = 'AB'
            string = string + letters[x]
        elif letters[x] == 'C':
            letters[x] = 'CD'
            string = string + letters[x]
        elif letters[x] == 'D':
            letters[x] = 'DC'
            string = string + letters[x]
        elif letters[x] == 'E':
            letters[x] = 'EE'
            string = string + letters[x]

letters = []
for x in string:
    letters.append(x)

nums = [0,0,0,0,0]
for x in range(0,position):
    if letters[x] == 'A':
        nums[0] += 1
    elif letters[x] == 'B':
        nums[1] += 1
    elif letters[x] == 'C':
        nums[2] += 1
    elif letters[x] == 'D':
        nums[3] += 1
    elif letters[x] == 'E':
        nums[4] += 1

for x in range(0,5):
    print(nums[x])
        
#Q3B - 256, 34
#Q3C - No because there will always be a D before and after every 2 Cs
#Q3D - A changed to A, B changed to AA
