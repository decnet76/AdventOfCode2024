import re

inp = open("A0C2024/Day04/input04.txt", "r")
#inp = open("A0C2024/Day04/test04.txt", "r")

rows=[]

while inp:
  line = inp.readline().replace("\n", "")
  if line == "":
    break
  rows.append(line)



total = 0
# search in rows
cntInRows = 0
for i in range(len(rows)):
  cntInRows += len(re.findall("XMAS" , rows[i]))
  cntInRows += len(re.findall("SAMX" , rows[i]))


# define columns
cols=[]
for i in range(len(rows)):
  col=""
  for j in range(len(rows[i])):
    #print(i, j)
    #print(rows[i][j])
    col+=rows[j][i]
  #print(col)
  cols.append(col)


# search in columns
cntInCols = 0
for i in range(len(cols)):
  cntInCols += len(re.findall("XMAS" , cols[i]))
  cntInCols += len(re.findall("SAMX" , cols[i]))



# create diagonals NW-SE
diagNW=[]
# main diag
diag=""
for d in range(len(rows)):
  diag+=rows[d][d]
diagNW.append(diag)
#print(diagNW)

# above the main one: (0,1), (1, 2), (2, 3)  
# then (0, 2), (1, 3), (2, 4) etc
for d in range(1, len(rows)-3):
  #print("d=" + str(d))
  diag=""
  i=0
  j=d
  while j<len(rows):
    #print(i, j)
    diag+=rows[i][j]
    i+=1
    j+=1
    #print(diag)  
  diagNW.append(diag)
#print(diagNW)

# lower diagonal below the main one: (1,0), (2,1), (3,2)  
# then (2,0), (3,1), (4,2) etc
for d in range(1, len(rows)-3):
  #print("d=" + str(d))
  diag=""
  i=d
  j=0
  while i<len(rows):
    #print(i, j)
    diag+=rows[i][j]
    i+=1
    j+=1
    #print(diag)  
  diagNW.append(diag)
#print(diagNW)


#####################################################
# create diagonals SW-NE (9,0), (8,1) etc
diagSW=[]
# main diag
diag=""
for d in range(len(rows)):
  diag+=rows[len(rows)-1-d][d]
diagSW.append(diag)
#print(diagSW)

# above the main one: (8,0), (7,1), (6,2)  
# then (7,0), (6,1), (5,2) etc
for d in range(len(rows)-1, 3, -1):
  #print("d=" + str(d))
  diag=""
  i=d
  j=0
  while i>0:
    #print(i, j)
    diag+=rows[i][j]
    i-=1
    j+=1
    #print(diag)  
  diagSW.append(diag)
#print(diagSW)


# lower diagonal below the main one: (9,1), (8,2), (7,3)  
# then (9,2), (8,3), (7,4) etc up to (9,6)...(6,9)
for d in range(1, len(rows)-3):
  #print("d=" + str(d))
  diag=""
  i=len(rows)-1
  j=d
  while i>0 and j<len(rows):
    #print(i, j)
    diag+=rows[i][j]
    i-=1
    j+=1
    #print(diag)  
  diagSW.append(diag)
#print(diagSW)

#search in diagonals
cntInDiagNW = 0
for i in range(len(diagNW)):
  cntInDiagNW += len(re.findall("XMAS" , diagNW[i]))
  cntInDiagNW += len(re.findall("SAMX" , diagNW[i]))


cntInDiagSW = 0
for i in range(len(diagSW)):
  cntInDiagSW += len(re.findall("XMAS" , diagSW[i]))
  cntInDiagSW += len(re.findall("SAMX" , diagSW[i]))


print(rows)
print(cntInRows)
print(cols)
print(cntInCols)
print(diagNW)
print(cntInDiagNW)
print(diagSW)
print(cntInDiagSW)

print(len(rows))
print(len(cols))
print(len(diagNW))
print(len(diagSW))

total = cntInCols + cntInRows + cntInDiagSW + cntInDiagNW
print("part 1 = " + str(total))