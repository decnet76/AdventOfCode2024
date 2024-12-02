inp = open("A0C2024/Day01/input01.txt", "r")
#inp = open("A0C2024/Day01/test01.txt", "r")

list1=[]
list2=[]

while inp:
  line = inp.readline().replace("\n", "")

  if line == "":
    break
    
  list1.append(line.split("   ")[0])
  list2.append(line.split("   ")[1])
  
print(list1)
print(list2)

list1.sort()
list2.sort()

total = 0
for i in range(len(list1)):
  total += abs(int(list1[i])-int(list2[i]))

print(" part 1 = " + str(total))

total2 = 0
for i in range(len(list1)):
  total2 += int(list1[i]) * int(list2.count(list1[i]))

print(" part 2 = " + str(total2))