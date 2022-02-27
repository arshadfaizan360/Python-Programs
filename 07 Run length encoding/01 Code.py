text = input('Enter the text to be compressed: ')
compressed = ''
letter = text[0]
count = 0
for x in text:
    if x == letter:
        count += 1
    else:
        compressed += letter + ' ' + str(count) + ' '
        letter = x
        count = 1

compressed += letter + ' ' + str(count) + ' '
print(compressed)
