import time
import math
from itertools import combinations
start_part1 = time.time()

inp = open("A0C2024/Day11/input11.txt", "r")
#inp = open("A0C2024/Day11/test11.txt", "r")
#inp = open("A0C2024/Day11/test11 short.txt", "r")

stones=[]
stones = list(map(int, inp.readline().replace("\n", "").split(" ")))
#print(map)

size= len(stones)
print(stones)

blinks = 25
b = 0
newStones = []
while b < blinks :  
    print("b = " + str(b) + ", stones = " + str(len(stones)))
    for i in range(len(stones)):
        #print("i = " + str(i) + ", stone[i] = " + str(stones[i]))
        if stones[i] == 0:
            newStones.append(int(1))
        else:
            l = len(str(stones[i]))
            if l%2 == 0:
                left = math.trunc(stones[i]/(10**(l/2)))
                newStones.append(int(left))
                newStones.append(int(stones[i] - left*(10**(l/2))))
            else:
                newStones.append(int(2024*stones[i]))
    #print(newStones)        
    stones = newStones.copy()
    newStones = []
    b+=1
        


print(" part 1 = " + str(len(stones)))
print("Part 1 finished --- %s seconds ---" % (time.time() - start_part1))
