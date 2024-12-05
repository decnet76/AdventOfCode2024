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

# I'm going to use loops (bad), updates are shorter than the rules list so I should iterate on those first
def isUpdateCorrect(update, f, s, rules):  
  #check the all the rules in which this number is the first element
  for i in range(len(update)):    
    succRules = [x for x in rules if update[i] in x.split("|")[0]]
    print(succRules) # ok up to this point

  #check the all the rules in which this number is the second element
  for i in range(len(update)):    
    precRules = [x for x in rules if update[i] in x.split("|")[1]]
    print(precRules) # ok up to this point

  #for each element of the update, check if it violates any rules
  for i in range(len(update)):
    # check predecessors
    if i>0:
      pass

    # check successors
    if i<len(update):
      pass
      
  return True

# def findMiddle(update):
#   return 0

part1 = 0
update = []
for u in range(len(updates)):
  #update = updates[u].split(",")  
  update = updates[3].split(",")  
  if isUpdateCorrect(update, first, second, rules):
    break
    part1 += update[len(update)/2]

print("part 1 = ", str(part1))



############ part2:
total = 0

print("part 2 = " + str(total))