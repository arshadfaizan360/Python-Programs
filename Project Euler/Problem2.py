list = [1,2]
while list[len(list)-1] <= 4000000:
    list.append(list[len(list)-1] + list[len(list)-2])
list.pop()
sum = 0
for x in list:
    if x % 2 == 0:
        sum += x
print(sum)