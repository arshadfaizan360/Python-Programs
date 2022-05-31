word = input('Please enter your word: ')
compressed = ''
current = word[0]
count = 0
for x in word:
  if x == current:
    count += 1
  else:
    compressed = compressed + ' ' + current + ' ' + str(count)
    current = x
    count = 1

compressed = compressed + ' ' + current + ' ' + str(count)

print(compressed)