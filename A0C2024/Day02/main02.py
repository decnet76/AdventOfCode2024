inp = open("A0C2024/Day02/input02.txt", "r")
#inp = open("A0C2024/Day02/test02.txt", "r")

levels=[]
total = 0

###### Function
def isSafe(levels):  
  diff = []
  for i in range(len(levels)-1):
    diff.append(int(levels[i]) - int(levels[i+1]))    

  sign = 0
  for j in range(len(diff)):
    if diff[j]==0 or abs(diff[j])>3:
      return False

    sign += diff[j]/abs(diff[j])

  return abs(sign) == len(diff)


####### Main
safe = 0
unsafe = 0
while inp:
  line = inp.readline().replace("\n", "")

  if line == "":
    break

  levels = line.split(" ")
  
  print(levels)

  ### Part 2
  total2 = 0
  # If unsafe, try to pass a reduced list to the function
  if isSafe(levels):
    safe += 1
    print("safe without changes")
  else:
    for j in range(len(levels)):
      lvl = levels.copy()
      del lvl[j]   
      print(lvl)
      if isSafe(lvl):
        print("safe when removing element at place " + str(j))
        safe += 1
        break
    unsafe += 1
  
  print(" safe = " + str(safe))
  print(" unsafe = " + str(unsafe))







