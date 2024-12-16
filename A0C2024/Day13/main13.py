import time
import math
from itertools import combinations
start_part1 = time.time()

inp = open("A0C2024/Day13/input13.txt", "r")
#inp = open("A0C2024/Day13/test13.txt", "r")

prize = []
buttonA = []
buttonB = []

with inp as file:
    data = file.read()
blocks = data.strip().split("\n\n")

for block in blocks:
  for line in block.strip().split("\n"):
    if line[0:8]=="Button A":
        buttonA.append(line[10:].replace("X+", "").replace("Y+", "").split(","))    
    if line[0:8]=="Button B":
        buttonB.append(line[10:].replace("X+", "").replace("Y+", "").split(","))
    if line[0:5]=="Prize":
        prize.append(line[7:].replace("X=", "").replace("Y=", "").split(","))

det = 0
tokens = 0
for i in range(len(prize)):
    # use vector product
    # determinant of matrix (index 0 = x, 1 = y):
    xA = int(buttonA[i][0])
    yA = int(buttonA[i][1])
    xB = int(buttonB[i][0])
    yB = int(buttonB[i][1])
    det = xA * yB - yA * xB
    pX = int(prize[i][0])
    pY = int(prize[i][1])
    numA = math.floor((pX * yB - pY * xB)/det)
    numB = math.floor((pY * xA - pX * yA)/det)
    if numA <= 100 and numB <= 100:
       if (numA * xA + numB * xB)==pX and (numA * yA + numB * yB)==pY:
            tokens += 3*numA + numB
    # else impossible

# first answer: 38589 too high
# second answer after adding the additional check (that the product returns the pX, pY): 37128 --> correct
print(" part 1 = " + str(tokens))
print("Part 1 finished --- %s seconds ---" % (time.time() - start_part1))

#Part2
T = 10000000000000
det = 0
tokens = 0
for i in range(len(prize)):
    xA = int(buttonA[i][0])
    yA = int(buttonA[i][1])
    xB = int(buttonB[i][0])
    yB = int(buttonB[i][1])
    det = xA * yB - yA * xB
    pX = int(prize[i][0]) + T
    pY = int(prize[i][1]) + T
    numA = math.floor((pX * yB - pY * xB)/det)
    numB = math.floor((pY * xA - pX * yA)/det)
    #if numA <= 100 and numB <= 100: cannot be this low anymore
    if (numA * xA + numB * xB)==pX and (numA * yA + numB * yB)==pY:
        tokens += 3*numA + numB

# answer 74914228471331 - too easy! I just added T....no major change to algorithm
print(" part 2 = " + str(tokens))
print("Part 1 finished --- %s seconds ---" % (time.time() - start_part1))        