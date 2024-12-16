import time
import math
from itertools import combinations
start_part1 = time.time()

inp = open("A0C2024/Day14/input14.txt", "r")
#inp = open("A0C2024/Day14/test14.txt", "r")

pos = []
speed = []

while inp:
  line = inp.readline().replace("\n", "")
  if line == "":
    break
  pos.append(list(map(int, line.split(" ")[0].replace("p=", "").split(","))))
  speed.append(list(map(int, line.split(" ")[1].replace("v=", "").split(","))))

#print(pos)
#print(speed)

K = 100 # iterations
M = 101# map X size
N = 103# map Y size
endPos = []
for i in range(len(pos)):
    endPos.append(
    [
        (pos[i][0] +  K*speed[i][0]) % M,
        (pos[i][1] +  K*speed[i][1]) % N
    ]
    )
# print(endPos)



part1 = 0
# count on each quarter
q1 = 0
for x in range(int((M-1)/2)):
   for y in range(int((N-1)/2)):
      q1 += endPos.count([x,y])
#print(q1)

q2 = 0
for x in range(int((M+1)/2), M):
   for y in range(int((N-1)/2)):
      q2 += endPos.count([x,y])
#print(q2)

q3 = 0
for x in range(int((M-1)/2)):
   for y in range(int((N+1)/2), N):
      q3 += endPos.count([x,y])
    #   if endPos.count([x,y]) > 0 :
    #     print(x, y, endPos.count([x,y]))
#print(q3)

q4 = 0
for x in range(int((M+1)/2), M):
   for y in range(int((N+1)/2), N):
      q4 += endPos.count([x,y])
#print(q4)

part1 = q1*q2*q3*q4
# first answer: 
print(" part 1 = " + str(part1))
print("Part 1 finished --- %s seconds ---" % (time.time() - start_part1))

#Part2
part2 = 0

# 
print(" part 2 = " + str(part2))
print("Part 1 finished --- %s seconds ---" % (time.time() - start_part1))        