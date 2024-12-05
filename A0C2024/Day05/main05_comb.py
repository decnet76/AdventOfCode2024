import math 

inp = open("A0C2024/Day05/input05.txt", "r")
#inp = open("A0C2024/Day05/test05.txt", "r")

rules=[]

while inp:
  line = inp.readline().replace("\n", "")
  if line == "":
    break
  rules.append(line)

updates=[]
while inp:
  line = inp.readline().replace("\n", "")
  if line == "":
    break
  updates.append(line)

print(rules)
print(updates)


# extract all the ordered couples from the updates
couples_list=[]
for u in range(len(updates)):  
  update = updates[u].split(",")
  couples=[]
  for i in range(len(update)):
    for j in range(i+1, len(update)):
      couples.append(update[i]+"|"+update[j])
  couples_list.append(couples)

#print(updates[0])  
#print(couples_list[0])

part1 = 0
incorrect_updates=[]
incorrect_couples=[]
for t in range(len(updates)):
  isUpdateCorrect = True
  update = updates[t].split(",") 
  for x in range(len(couples_list[t])):
    print(couples_list[t][x] + " " + str(rules.count(couples_list[t][x])) )
    if rules.count(couples_list[t][x])==0:      
      isUpdateCorrect = False
      incorrect_couples.append(couples_list[t])
      incorrect_updates.append(update)
      break
  if isUpdateCorrect:    
    part1 += int(update[math.floor(len(update)/2)])
  #print(update)
  #print("update " + str(t) + " is correct = " + str(isUpdateCorrect))

print("part 1 = " + str(part1))


print(incorrect_updates)
part2 = 0
for t in range(len(incorrect_updates)):
  incorrectUpdate = incorrect_updates[t]
  isUpdateCorrect = False
  while not isUpdateCorrect:       
    numPairsInRules = 0    
    for x in range(len(incorrectUpdate)):    
      for y in range(x+1, len(incorrectUpdate)):
        if rules.count(incorrectUpdate[x]+"|"+incorrectUpdate[y])==1:
          numPairsInRules += 1
        if rules.count(incorrectUpdate[x]+"|"+incorrectUpdate[y])==0:      
          #swap then break and assess again       
          incorrectUpdate[x], incorrectUpdate[y] = incorrectUpdate[y], incorrectUpdate[x] 
          break
    if numPairsInRules == len(incorrectUpdate)*(len(incorrectUpdate)-1)/2:
      isUpdateCorrect = True

  if isUpdateCorrect:    
    part2 += int(incorrectUpdate[math.floor(len(incorrectUpdate)/2)])
  
print("part 2 = " + str(part2))