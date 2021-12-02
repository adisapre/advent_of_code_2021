#part1: parse file and determine depth and distance
depth = 0
distance = 0

with open('day2input.txt') as inp:
    for line in inp:
        temp = line.split()
        if temp[0] == 'down':
            depth += int(temp[1])
        elif temp[0] == 'up':
            depth -= int(temp[1])
        elif temp[0] == 'forward':
            distance += int(temp[1])
print(depth*distance)

#part2: aim now included!

depth = 0
distance = 0
aim = 0

with open('day2input.txt') as inp:
    for line in inp:
        temp = line.split()
        if temp[0] == 'down':
            aim += int(temp[1])
        elif temp[0] == 'up':
            aim -= int(temp[1])
        elif temp[0] == 'forward':
            distance += int(temp[1])
            depth += int(temp[1])*aim
print(depth*distance)