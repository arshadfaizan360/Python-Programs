sum = 0

with open("1.txt") as words:
    for word in words:
        num = ""
        for pos in range(0, len(word)):
            if word[pos].isdigit():
                num += word[pos]
                break
            else:
                if word[pos:].startswith("one"):
                    num += "1"
                    break
                elif word[pos:].startswith("two"):
                    num += "2"
                    break
                elif word[pos:].startswith("three"):
                    num += "3"
                    break
                elif word[pos:].startswith("four"):
                    num += "4"
                    break
                elif word[pos:].startswith("five"):
                    num += "5"
                    break
                elif word[pos:].startswith("six"):
                    num += "6"
                    break
                elif word[pos:].startswith("seven"):
                    num += "7"
                    break
                elif word[pos:].startswith("eight"):
                    num += "8"
                    break
                elif word[pos:].startswith("nine"):
                    num += "9"
                    break
                
        for pos in range (len(word)-1, -1, -1):
            if word[pos].isdigit():
                num += word[pos]
                break
            else:
                if word[pos:].startswith("one"):
                    num += "1"
                    break
                elif word[pos:].startswith("two"):
                    num += "2"
                    break
                elif word[pos:].startswith("three"):
                    num += "3"
                    break
                elif word[pos:].startswith("four"):
                    num += "4"
                    break
                elif word[pos:].startswith("five"):
                    num += "5"
                    break
                elif word[pos:].startswith("six"):
                    num += "6"
                    break
                elif word[pos:].startswith("seven"):
                    num += "7"
                    break
                elif word[pos:].startswith("eight"):
                    num += "8"
                    break
                elif word[pos:].startswith("nine"):
                    num += "9"
                    break
        sum += int(num)

print(sum)
