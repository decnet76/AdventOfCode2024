import time
import math
from itertools import combinations
start_part1 = time.time()

inp = open("A0C2024/Day11/input11.txt", "r")
#inp = open("A0C2024/Day11/test11.txt", "r")
#inp = open("A0C2024/Day11/test11 short.txt", "r")

stones=[]
firstStones=[]
firstStones = list(map(int, inp.readline().replace("\n", "").split(" ")))
#print(map)

size= len(firstStones)
print(firstStones)

blinks = 25
newStones = []
part2 = 0
for init in range(len(firstStones)):
    stones.append(firstStones[init])
    print(firstStones[init])
    b = 0
    while b < blinks :  
        print("b = " + str(b) + ", stones = " + str(len(stones)))
        #print("b = " + str(b) + ", stones = ", end="")
        #print(stones)
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
    part2 += len(stones)
    stones = []
        


print(" part 2 = " + str(part2))
print("Part 1 finished --- %s seconds ---" % (time.time() - start_part1))
