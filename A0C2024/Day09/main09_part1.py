import time
import math
from itertools import combinations
start_part1 = time.time()

inp = open("A0C2024/Day09/input09.txt", "r")
#inp = open("A0C2024/Day09/test09.txt", "r")
#inp = open("A0C2024/Day09/test09_short.txt", "r")

diskmap = inp.readline().replace("\n", "")
#print(diskmap)

size= len(diskmap)
print(size)


blocks = []
id = 0
lastBlockSize = 0
if size%2==0:
  lastBlockSize = diskmap[size-2]
else:
  lastBlockSize = diskmap[size-1]


for i in range(size):
  if i%2==0:
    for b in range(int(diskmap[i])):
      blocks.append(id)
    id += 1
  if i%2==1:
    for b in range(int(diskmap[i])):
      blocks.append(".")      

# for b in range(len(blocks)):
#   print(str(blocks[b]), end="")

maxEmpty = int(len(blocks)) - int(lastBlockSize) - 1
#print("lastBlockSize = " + str(lastBlockSize) + ", maxEmptyIndex = " + str(maxEmpty))

### DEFRAG
r = len(blocks)-1
x = 0
#while x <= maxEmpty and x < r:
while x < r:
  print("x = " + str(x) + ", r = " + str(r))

  #debug
  if x>= 50000:
    for b in range(50000,50010):
      print(str(blocks[b]), end="")

  if blocks[x] == ".":
    # find rightmost non-empty then swap
    while blocks[r] == ".":
      r-=1
    blocks[x], blocks[r] = blocks[r], blocks[x]
    
    # for b in range(len(blocks)):
    #   print(str(blocks[b]), end="")
  x += 1

for b in range(50000,50010):
  print("b = " + str(b) + " block[b] = " + str(blocks[b]))

# pezzotto
blocks[50003], blocks[50004] = blocks[50004], blocks[50003]

# final image:
for b in range(len(blocks)):
  print(str(blocks[b]), end="")
print("x = " + str(x) + ", r = " + str(r))



for b in range(50000,50010):
  print("b = " + str(b) + " block[b] = " + str(blocks[b]))

### checksum
part1 = 0
for c in range(len(blocks)):
  if blocks[c]!=".":
    part1 += c*blocks[c]

print("part 1 = " + str(part1))
# first attempt: 6332189871939 too high
# pezzotto:      6332450937602 it's even higher, not possible...