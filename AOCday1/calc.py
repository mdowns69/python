file = open('distance2.txt', 'r')
leftlist = []
rightlist = []

for line in file:
  a = line.split()
  leftlist.append(a[0])
  rightlist.append(a[1])

print(leftlist)
print(rightlist)

mylen = len(leftlist)
leftlist = sorted(leftlist)
rightlist = sorted(rightlist)
print(leftlist)
print(rightlist)

total = 0

for x in range(0, mylen):
  print(abs(int(leftlist[x]) - int(rightlist[x])))
  total += abs(int(leftlist[x]) - int(rightlist[x]))

print(total)