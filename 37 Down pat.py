words = input('')
list = []
for x in words:
    list.append(x)

word1 = ''
word2 = ''
found = False
for x in list:
    if x == ' ':
        found = True
    elif found == False:
        word1 += x
    else:
        word2 += x

part1 = ''
part2 = word1

def check(part1, part2):
    part1 = part2[0]
    part2 = part2[1:]
    if part2 != '':
        list1 = []
        list2 = []
        for x in part1:
            list1.append(x)
        for x in part2:
            list2.append(x)
        correct = True
        for x in part1:
            for y in part2:
                if x < y:
                    correct = False
                    if len(part1) != 1:
                        check(part1, part2)
                    else:
                        print('No')
        if correct == True:
            print('Yes')

    if len(part1) == 1 and len(part2) == 0:
        print('Yes')

check(part1, part2)
check('', word2)
check('', word1+word2)
