import re
calibrationFile = open("Day01/calories.txt", "r")
sum = 0

while calibrationFile:
  line = calibrationFile.readline()
  if line == "":
    break
  """
  if (line != "\n"):
    currentElfPack = currentElfPack + int(line)
  if line == "\n":
    if currentElfPack > maxElfPack:
      maxElfPack = currentElfPack
    print(currentElfPack)
    currentElfPack = 0
  """
  firstResult = re.findall(r'[0-9]+', line)
  if firstResult:
    first = firstResult.group()

  lastResult = re.findall(r'[0-9]+', line[::-1])
  if lastResult:
    last = lastResult.group()

  print(line)
  cal = str(first) + str(last)
  print(cal)
  sum = sum + int(cal)
  
calibrationFile.close()
print("sum = " + str(sum))



print("---------seconda parte-------")
#####################################################


  