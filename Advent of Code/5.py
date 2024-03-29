with open('5.txt') as file:
    lines = file.readlines()

for line in lines:
    index = lines.index(line)
    lines[index] = line.rstrip('\n')

lines.reverse()

seed_string = lines.pop()
seed_string = seed_string.lstrip('seeds: ')

seeds = []
current_seed = ''
for char in seed_string:
    if char.isnumeric():
        current_seed += char
    else:
        seeds.append(int(current_seed))
        current_seed = ''
seeds.append(int(current_seed))

print(seeds)

# new_seeds = []

# for index in range (0, len(seeds), 2):
#     for x in range (seeds[index+1]):
#         if not (seeds[index] + x) in new_seeds:
#             new_seeds.append(seeds[index] + x)
#             print(seeds[index]+x)

# seeds = new_seeds

seed_to_soil_map = []
soil_to_fertilizer_map = []
fertilizer_to_water_map = []
water_to_light_map = []
light_to_temperature_map = []
temperature_to_humidity_map = []
humidity_to_location_map = []

lines.pop()
lines.pop()
current_line = lines.pop()

while current_line != '':
    numbers = []
    current_number = ''
    for char in current_line:
        if char.isnumeric():
            current_number += char
        else:
            numbers.append(int(current_number))
            current_number = ''
    numbers.append(int(current_number))
    seed_to_soil_map.append(numbers)
    current_line = lines.pop()

lines.pop()
current_line = lines.pop()
while current_line != '':
    numbers = []
    current_number = ''
    for char in current_line:
        if char.isnumeric():
            current_number += char
        else:
            numbers.append(int(current_number))
            current_number = ''
    numbers.append(int(current_number))
    soil_to_fertilizer_map.append(numbers)
    current_line = lines.pop()

lines.pop()
current_line = lines.pop()
while current_line != '':
    numbers = []
    current_number = ''
    for char in current_line:
        if char.isnumeric():
            current_number += char
        else:
            numbers.append(int(current_number))
            current_number = ''
    numbers.append(int(current_number))
    fertilizer_to_water_map.append(numbers)
    current_line = lines.pop()

lines.pop()
current_line = lines.pop()
while current_line != '':
    numbers = []
    current_number = ''
    for char in current_line:
        if char.isnumeric():
            current_number += char
        else:
            numbers.append(int(current_number))
            current_number = ''
    numbers.append(int(current_number))
    water_to_light_map.append(numbers)
    current_line = lines.pop()

lines.pop()
current_line = lines.pop()
while current_line != '':
    numbers = []
    current_number = ''
    for char in current_line:
        if char.isnumeric():
            current_number += char
        else:
            numbers.append(int(current_number))
            current_number = ''
    numbers.append(int(current_number))
    light_to_temperature_map.append(numbers)
    current_line = lines.pop()

lines.pop()
current_line = lines.pop()
while current_line != '':
    numbers = []
    current_number = ''
    for char in current_line:
        if char.isnumeric():
            current_number += char
        else:
            numbers.append(int(current_number))
            current_number = ''
    numbers.append(int(current_number))
    temperature_to_humidity_map.append(numbers)
    current_line = lines.pop()

lines.pop()
while lines != []:
    current_line = lines.pop()
    numbers = []
    current_number = ''
    for char in current_line:
        if char.isnumeric():
            current_number += char
        else:
            numbers.append(int(current_number))
            current_number = ''
    numbers.append(int(current_number))
    humidity_to_location_map.append(numbers)

def applymap(source, map_list):
    for map in map_list:
            if source >= map[1] and source < map[1]+map[2]:
                difference = source - map[1]
                return map[0] + difference
    return source

closest_location = 9999999999999999999999999999999999999999999999999999999999999999999
for seed in seeds:
    soil = applymap(seed, seed_to_soil_map)
    fertilizer = applymap(soil, soil_to_fertilizer_map)
    water = applymap(fertilizer, fertilizer_to_water_map)
    light = applymap(water, water_to_light_map)
    temp = applymap(light, light_to_temperature_map)
    humidity = applymap(temp, temperature_to_humidity_map)
    location = applymap(humidity, humidity_to_location_map)

    if location < closest_location:
        closest_location = location

print(closest_location)