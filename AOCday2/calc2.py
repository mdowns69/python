import numpy
file = open('data2.txt', 'r')

#Returns 0 if doesn't pass sign test
#Returns 1 if passes sign test
def testdirection(x):
  sign = numpy.sign(x[0] - x[1])
  for y in range(0, len(x)-1):
    if numpy.sign(x[y] - x[y+1]) != sign:
      return 0
  return 1

#Returns 0 if doesn't pass value test
#Returns 1 if passes value test
def testvalues(x):
  for y in range(0, len(x)-1):
    if abs(x[y] - x[y+1]) <= 0 or abs(x[y] - x[y+1]) > 3:
      return 0
  return 1

countsafe = 0
for line in file:
  mylist = line.split()
  mylist = list(map(int, mylist))

  #currently have a single line of integers
  if testdirection(mylist) + testvalues(mylist) == 2:
    countsafe += 1
    continue
  
  for x in range(0, len(mylist)):
    newlist = mylist.copy()
    newlist.pop(x)
    if testdirection(newlist) + testvalues(newlist) == 2:
      countsafe += 1
      print(countsafe)
      break
  
print(countsafe)

