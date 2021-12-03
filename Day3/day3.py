# day 3 part 1
blanketInput = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] #deciding frequency

with open('day3input.txt') as inp:
    for line in inp:
        temp = list(line)
        for c in range(len(temp)):
            if temp[c] == "0":
                blanketInput[c] -= 1
            elif temp[c] == "1":
                blanketInput[c] += 1

gamma = []
epsilon = []

for i in blanketInput:
    if i < 0:
        gamma.append("0")
        epsilon.append("1")
    elif i >= 0:
        gamma.append("1")
        epsilon.append("0")

gamma = int("".join(gamma),2)
epsilon = int("".join(epsilon),2)

print(gamma*epsilon)

#part 2 - determine most/least common in leftover

mostCommon = 0
bitPosition = 0

fullList = []
tempString = ""
tempBlanket = [0,0,0,0,0,0,0,0,0,0,0,0]

with open('day3input.txt') as inp:
    for line in inp:
        fullList.append(line.strip())

oxyRating = fullList
co2Rating = fullList

while bitPosition < 12:
    if len(oxyRating) == 1:
        break
    for bin in oxyRating:
        if bin[bitPosition] == "1":
            mostCommon+=1
        elif bin[bitPosition] == "0":
            mostCommon-=1
    if mostCommon >= 0:
        tempString += "1"
    else:
        tempString += "0"

    oxyRating = [num for num in oxyRating if num.startswith(tempString)]
    print(bitPosition)
    print(oxyRating)
    mostCommon = 0
    bitPosition += 1

bitPosition = 0
tempString = ""

while bitPosition < 12:
    if len(co2Rating) == 1:
        break
    for bin in co2Rating:
        if bin[bitPosition] == "1":
            mostCommon+=1
        elif bin[bitPosition] == "0":
            mostCommon-=1
    if mostCommon >= 0:
        tempString += "0"
    else:
        tempString += "1"
    mostCommon = 0
    co2Rating = [num for num in co2Rating if num.startswith(tempString)]
    bitPosition += 1

print(oxyRating)
print(co2Rating)

print(int("".join(co2Rating),2)*int("".join(oxyRating),2))