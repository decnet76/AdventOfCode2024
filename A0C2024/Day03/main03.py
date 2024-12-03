import re

inp = open("A0C2024/Day03/input03.txt", "r")
#inp = open("A0C2024/Day03/test03.txt", "r")

#single line input for this problem
line = inp.readline().replace("\n", "")
#print(line)

#mults = re.search("mul\(+[0-9]{,}+[0-9]\)", line)
mults = re.findall("mul\([0-9]+\,[0-9]+\)", line)
#print(mults)

total = 0
for j in range(len(mults)):
  first, second = map(int, mults[j].replace("mul(", "").replace(")", "").split(","))
#  print(mults[j], first, second)  
  total += first * second

print(" part 1 = " + str(total))

################# Part 2
#inp = open("A0C2024/Day03/test03_part2.txt", "r")
#line = inp.readline().replace("\n", "")

mults2 = re.findall("mul\([0-9]+\,[0-9]+\)|do\(\)|don't\(\)", line)
print(mults2)

total2 = 0
isEnabled = True
for j in range(len(mults2)):
  if mults2[j]=="do()":
    isEnabled = True
  if mults2[j]=="don't()":
    isEnabled = False  
  if isEnabled and mults2[j] != "do()" and mults2[j] != "don't()":
    first, second = map(int, mults2[j].replace("mul(", "").replace(")", "").split(","))
    total2 += first * second

print(" part 2 = " + str(total2))
