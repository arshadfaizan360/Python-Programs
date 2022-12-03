largest = 0

for x in range (100,1000):
    for y in range (100,1000):
        num = x*y
        if num > largest:
            list = []
            for z in str(num):
                list.append(int(z))
            palindrome = True
            while list != [] and palindrome == True:
                if list[0] == list[len(list)-1]:
                    list.remove(list[0])
                    if list != []:
                        list.pop()
                else:
                    palindrome = False
            if palindrome == True:
                largest = num

print(largest)