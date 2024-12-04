import re

inp = open("A0C2024/Day04/input04.txt", "r")
#inp = open("A0C2024/Day04/test04_adhoc.txt", "r")
#inp = open("A0C2024/Day04/test04.txt", "r")
#inp = open("A0C2024/Day04/test04_p2.txt", "r")

rows=[]

while inp:
  line = inp.readline().replace("\n", "")
  if line == "":
    break
  rows.append(line)



total = 0

for i in range(len(rows)):
  for j in range(len(rows)):
    if rows[i][j]=="X":
      try:
        # check diagonally:
        #NW:                
        if i>2 and j>2 and rows[i-1][j-1]=="M" and rows[i-2][j-2]=="A" and rows[i-3][j-3]=="S":         
          total+=1
          print(i,j, "NW")
        #NE
        if i>2 and j<len(rows)-3 and rows[i-1][j+1]=="M" and rows[i-2][j+2]=="A" and rows[i-3][j+3]=="S":
          total+=1
          print(i,j, "NE")
        #SW
        if j>2 and i<len(rows)-3 and rows[i+1][j-1]=="M" and rows[i+2][j-2]=="A" and rows[i+3][j-3]=="S":
          total+=1
          print(i,j, "SW")
        #SE
        if i<len(rows)-3 and j<len(rows)-3 and rows[i+1][j+1]=="M" and rows[i+2][j+2]=="A" and rows[i+3][j+3]=="S":
          total+=1
          print(i,j, "SE")

        #vertical:
        if i<len(rows)-3 and rows[i+1][j]=="M" and rows[i+2][j]=="A" and rows[i+3][j]=="S":
          total+=1
          print(i,j, "S")
        if i>2 and rows[i-1][j]=="M" and rows[i-2][j]=="A" and rows[i-3][j]=="S":
          total+=1
          print(i,j, "N")
        #horizontal:
        if j<len(rows)-3 and rows[i][j+1]=="M" and rows[i][j+2]=="A" and rows[i][j+3]=="S":
          total+=1
          print(i,j, "E")
        if j>2 and rows[i][j-1]=="M" and rows[i][j-2]=="A" and rows[i][j-3]=="S":
          total+=1
          print(i,j, "W")
      except:
        pass #nothing to see here...

print("part 1 = " + str(total))



############ part2:
total = 0

for i in range(len(rows)):
  for j in range(len(rows)):
    if rows[i][j]=="A" and i>0 and j>0 and i<len(rows)-1 and j<len(rows)-1:
      try:
        if rows[i-1][j-1]=="M" and rows[i-1][j+1]=="M" and rows[i+1][j-1]=="S" and rows[i+1][j+1]=="S":         
          total+=1
        if rows[i-1][j-1]=="M" and rows[i-1][j+1]=="S" and rows[i+1][j-1]=="M" and rows[i+1][j+1]=="S":         
          total+=1
        if rows[i-1][j-1]=="S" and rows[i-1][j+1]=="M" and rows[i+1][j-1]=="S" and rows[i+1][j+1]=="M":         
          total+=1
        if rows[i-1][j-1]=="S" and rows[i-1][j+1]=="S" and rows[i+1][j-1]=="M" and rows[i+1][j+1]=="M":         
          total+=1
      except:
        pass

print("part 2 = " + str(total))