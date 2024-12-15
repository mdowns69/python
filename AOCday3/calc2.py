import re
file = open('data2.txt', 'r')

mystring=""
for line in file:
   mystring = mystring + line


total=0

dos = re.split("do\\(\\)", mystring)


for subline in dos:
  subdos = re.split("don't\\(\\)", subline)
  muls = re.findall("mul\\(\\d+,\\s*\\d+\\)", subdos[0])
  for x in muls:
    ints = re.findall("\\d+", x)
    total += int(ints[0])*int(ints[1])


print(total)