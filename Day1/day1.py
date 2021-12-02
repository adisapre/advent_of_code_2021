#part1 - detect increases

prob1 = []

with open('day1Input.txt') as f:
    prob1 = f.readlines()

prob1 = [int(i) for i in prob1]

increases = 0
previous = prob1[0]

for n in prob1:
    if n > previous:
        increases += 1
    previous = n

print(increases)


#part2 - measurement window comparison

prevWindowSum = sum(prob1[0:3])
print(prevWindowSum)
part2increases = 0

for i in range(len(prob1)):
    if i+3 == len(prob1):
        currWindowSum = sum(prob1[i:i + 3])
        if currWindowSum > prevWindowSum:
            part2increases += 1
        break
    currWindowSum = sum(prob1[i:i+3])
    if currWindowSum > prevWindowSum:
        part2increases += 1
    prevWindowSum = currWindowSum

print(part2increases)
