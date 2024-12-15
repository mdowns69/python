file = open('../AOCday1/distance2.txt', 'r')
leftlist = []
rightlist = []

for line in file:
  a = line.split()
  leftlist.append(a[0])
  rightlist.append(a[1])

print(leftlist)
sumnsquared = 0

for x in leftlist:
  for y in rightlist:
    if x == y:
      sumnsquared += int(x)
      print(sumnsquared)

print(sumnsquared)