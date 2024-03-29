# Part 1

# sum = 0

# list = []
# with open("3.txt") as file:
#     for x in range(140):
#         list.append(file.readline().rstrip('\n'))

# # identify the numbers and symbols and their positions
# numlist = []
# symbolpositions = []
# row = -1
# for x in list:
#     row += 1
#     number_started = False
#     column = -1
#     currentnum = ""
#     num_positions = []
#     for char in x:
#         column += 1
#         if char == ".":
#             if number_started:
#                 numlist.append([int(currentnum), num_positions])
#                 currentnum = ""
#                 num_positions = []
#                 number_started = False
#         elif char.isdigit():
#             currentnum += char
#             num_positions.append([row, column])
#             number_started = True
#         else:
#             symbolpositions.append([row, column])
#             if number_started:
#                numlist.append([int(currentnum), num_positions])
#                currentnum = ""
#                num_positions = []
#                number_started = False 
#     if number_started:
#         numlist.append([int(currentnum), num_positions])

# for list in numlist:
#     num = list[0]
#     num_positions = list[1]
#     next_to_a_symbol = False

#     for position in num_positions:
#         row = position[0]
#         column = position[1]
#         adjacent_positions = [[row-1, column-1], [row-1, column], [row-1, column+1], [row, column-1], [row, column+1], [row+1, column-1], [row+1, column], [row+1, column+1]]
#         for x in adjacent_positions:
#             if x in symbolpositions:
#                 next_to_a_symbol = True
    
#     if next_to_a_symbol:
#         print(num)
#         sum += num

# print(sum)

# Part 2

sum = 0

list = []
with open("3.txt") as file:
    for x in range(140):
        list.append(file.readline().rstrip('\n'))

# identify the numbers and symbols and their positions
numlist = []
gearpositions = []
row = -1
for x in list:
    row += 1
    number_started = False
    column = -1
    currentnum = ""
    num_positions = []
    for char in x:
        column += 1
        if char == ".":
            if number_started:
                numlist.append([int(currentnum), num_positions])
                currentnum = ""
                num_positions = []
                number_started = False
        elif char.isdigit():
            currentnum += char
            num_positions.append([row, column])
            number_started = True
        else:
            if char == "*":
                gearpositions.append([row, column])
            if number_started:
               numlist.append([int(currentnum), num_positions])
               currentnum = ""
               num_positions = []
               number_started = False 
    if number_started:
        numlist.append([int(currentnum), num_positions])

for gear in gearpositions:
    adjacentnumbers = []
    row = gear[0]
    column = gear[1]
    adjacent_positions = [[row-1, column-1], [row-1, column], [row-1, column+1], [row, column-1], [row, column+1], [row+1, column-1], [row+1, column], [row+1, column+1]]
    for x in numlist:
        num = x[0]
        positions = x[1]
        for position in positions:
            if position in adjacent_positions:
                adjacentnumbers.append(num)
                break
    if len(adjacentnumbers) == 2:
        sum += adjacentnumbers[0] * adjacentnumbers[1]

print(sum)