def palindrome(list, startnum, endnum):
    if startnum!=endnum and startnum!=endnum-1:
        if palindrome(list,startnum+1,endnum-1) == False:
            return False
    if list[startnum] == list[endnum]:
        return True
    else:
        return False

word = input('Enter a word to check if it is a palindrome: ')
list = []
for x in word:
    list.append(x)
if palindrome(list,0,len(list)-1):
    print('It is a palindrome')
else:
    print('It is not a palindrome')
