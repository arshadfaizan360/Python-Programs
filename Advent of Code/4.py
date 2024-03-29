with open('4.txt', "r") as file:
    cards = file.readlines()

sum = 0

for card in cards:
    index = cards.index(card)
    cards[index] = card.rstrip('\n')
    for char in card:
        if char == ":":
            cards[index] = cards[index].lstrip(": ")
            break
        else:
            cards[index] = cards[index].lstrip(char)

counter = [1 for x in range (196)]
card_number = -1

for card in cards:
    card_number += 1
    winning_numbers = []
    our_numbers = []
    adding_to = "winning_numbers"
    current_num = ""
    for char in card:
        if char.isnumeric():
            current_num += char
        elif char == " ":
            if current_num != "":
                if adding_to == "winning_numbers":
                    winning_numbers.append(current_num)
                else:
                    our_numbers.append(current_num)
                current_num = ""
        else:
            adding_to = "our_numbers"
    our_numbers.append(current_num)

    # points = 0
    # for winning_number in winning_numbers:
    #     if winning_number in our_numbers:
    #         if points == 0:
    #             points = 1
    #         else:
    #             points *= 2
    
    # sum += points

    number_of_matches = 0
    for winning_number in winning_numbers:
        if winning_number in our_numbers:
            number_of_matches += 1
    for x in range(number_of_matches):
        counter[card_number+x+1] += counter[card_number] 

for x in counter:
    sum += x

print(sum)