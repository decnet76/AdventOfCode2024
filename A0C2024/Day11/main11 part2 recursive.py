import time
import math
from itertools import combinations
start_part2 = time.time()

inp = open("A0C2024/Day11/input11.txt", "r")
#inp = open("A0C2024/Day11/test11.txt", "r")
#inp = open("A0C2024/Day11/test11 short.txt", "r")

stones=[]
firstStones=[]
firstStones = list(map(int, inp.readline().replace("\n", "").split(" ")))
#print(map)

size= len(firstStones)
print(firstStones)

maxBlinks = 75
cache=set()
def findInCache(cache, key):
    for item in cache:
        if item[:2] == key:
            return item[2]
    return None

'''
def countStones(s: int, blink: int) -> int:
    #print("countStones(s: " + str(s) + ", blink: " + str(blink) + ")")
    if blink == maxBlinks:        
        return 1
    if s == 0:
        return countStones(1, blink + 1)
    l = len(str(s))
    if l%2 == 0:
        left = math.trunc(s/(10**(l/2)))
        return countStones(left, blink + 1) + countStones(s - int(left*(10**(l/2))), blink + 1)
    else:
        r = findInCache(cache, (2024*s, blink + 1))
        if r is None:
            r = countStones(2024*s, blink + 1)
            cache.add((2024*s, blink + 1, r))
        #return countStones(2024*s, blink + 1)
        # else:
        #     print("cache hit: " + "countStones(s: " + str(s) + ", blink: " + str(blink) + ") = " + str(r))
        return r
'''

# improvement: cache only n=0..9 for all the iterations
# PS: maybe SET is not the most efficient structure for this
def countStones(s: int, blink: int) -> int:
    #print("countStones(s: " + str(s) + ", blink: " + str(blink) + ")")
    r = findInCache(cache, (s, blink))
    if r is not None:
        #print("cache hit: " + "countStones(s: " + str(s) + ", blink: " + str(blink) + ") = " + str(r))        
        return r
    else:     
        if blink == maxBlinks:
            if s < 10 :        
                cache.add((s, blink, 1))
            return 1
        if s == 0:
            r = countStones(1, blink + 1)
            cache.add((1, blink + 1, r))
            return r
        l = len(str(s))
        if l%2 == 0:
            left = math.trunc(s/(10**(l/2)))
            rleft = countStones(left, blink + 1)
            if left < 10 :        
                cache.add((left, blink + 1, rleft))            
            rright = countStones(s - int(left*(10**(l/2))), blink + 1)
            if s - int(left*(10**(l/2))) < 10 :
                cache.add((s - int(left*(10**(l/2))), blink + 1, rright))            
            return rleft + rright
        else:
            r = countStones(2024*s, blink + 1)
            # if s < 10 :    
            #     cache.add((2024*s, blink + 1, r))
            return r


# preload cache
for i in range(10):
    cache.add((i, 0, countStones(i, 0)))


# print(countStones(125,0))
# print(countStones(17,0))

newStones = []
part2 = 0
for init in range(len(firstStones)):
    print(firstStones[init])
    part2 += countStones(firstStones[init], 0)
    print(str(part2))


        



print(" part 2 = " + str(part2))
print("Part 2 finished --- %s seconds ---" % (time.time() - start_part2))

print(cache)
