import re
file = open('data2.txt', 'r')

total=0

for line in file:
    muls = re.findall("mul\\(\\d+,\\s*\\d+\\)", line) #used ChatGPT for the regex
    for x in muls:
        print(x)
        ints = re.findall("\\d+", x)
        print(ints[0])
        print(ints[1])
        total += int(ints[0])*int(ints[1])


print(total)
