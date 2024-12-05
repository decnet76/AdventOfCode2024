import re

#inp = open("A0C2024/Day04/input04.txt", "r")
#inp = open("A0C2024/Day04/test04_adhoc.txt", "r")
inp = open("A0C2024/Day05/test05.txt", "r")
#inp = open("A0C2024/Day04/test04_p2.txt", "r")

rules=[]
first=[]
second=[]

while inp:
  line = inp.readline().replace("\n", "")
  if line == "":
    break
  rules.append(line)
  first.append(line.split("|")[0])
  second.append(line.split("|")[1])

updates=[]
while inp:
  line = inp.readline().replace("\n", "")
  if line == "":
    break
  updates.append(line)

print(rules)
print(updates)

total = 0


print("part 1 = " + str(total))



############ part2:
total = 0

print("part 2 = " + str(total))