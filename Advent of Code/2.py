# # Part 1

# sum = 0

# with open("2.txt") as games:
#     for id in range(1,101):
#         current_game = games.readline()
#         current_game = current_game.rstrip('\n')
#         list = current_game.split("; ")
#         for x in list:
#             list[list.index(x)] = x.split(", ")
#         print(list)
#         possible = True
#         for x in list:
#             # print(x)
#             red, green, blue = 0,0,0
#             print('Reset')
#             for item in x:
#                 number, colour = int(item[0:len(item)-1]), item[len(item)-1]
#                 print(number, colour)
#                 if colour == "r":
#                     red += number
#                     if red > 12:
#                         possible = False
#                 elif colour == "g":
#                     green += number
#                     if green > 13:
#                         possible = False
#                 else:
#                     blue += number
#                     if blue > 14:
#                         possible = False
#         if possible:
#             print(id)
#             sum += id
#         else:
#             print()

# print(sum)        
            
# Part 2

sum = 0

with open("2.txt") as games:
    for id in range(1,101):
        current_game = games.readline()
        current_game = current_game.rstrip('\n')
        list = current_game.split("; ")
        for x in list:
            list[list.index(x)] = x.split(", ")
        print(list)
        minred, mingreen, minblue = 0,0,0
        for x in list:
            # print(x)
            red, green, blue = 0,0,0
            print('Reset')
            for item in x:
                number, colour = int(item[0:len(item)-1]), item[len(item)-1]
                print(number, colour)
                if colour == "r":
                    red += number
                elif colour == "g":
                    green += number
                else:
                    blue += number
            if minred < red:
                minred = red
            if mingreen < green:
                mingreen = green
            if minblue < blue:
                minblue = blue
        power = minred * mingreen * minblue
        sum += power

print(sum)      