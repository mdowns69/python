file = open('data2.txt', 'r')

countsafe = 0
for line in file:
  mylist = line.split()
  mylist = list(map(int, mylist))
  increase = 1
  if mylist[0] - mylist[1] >= 0:
    increase = 0

  countsafe += 1
  for x in range(0, len(mylist)-1):
    a = mylist[x] - mylist[x+1]
    #print(a)
    if increase == 0:
      if a <= 0 or a >= 4:
        countsafe -= 1
        #print ("a is " + str(a))
        #print(countsafe)
        break
    else:
      if a <= -4 or a >= 0:
        countsafe -= 1
        #print ("a is " + str(a))
        #print(countsafe)
        break
  print("countsafe is " + str(countsafe))