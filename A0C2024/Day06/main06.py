inp = open("A0C2024/Day06/input06.txt", "r")
#inp = open("A0C2024/Day06/test06.txt", "r")

map=[]

currentRow=0
guardX, guardY = 0, 0
while inp:
  line = inp.readline().replace("\n", "")
  if line == "":
    break
  row = []
  for i in range(len(line)):
    if line[i] in ("^", "v", "<", ">"):
      guardY = currentRow
      guardX = i
      guardChar = line[i]
    row.append(line[i])
  map.append(row)
  currentRow+=1


# do not print map for actual input, too big - only for test input
# for i in range(len(map)):
#   print(map[i])

#print(str(guardX) + ", " + str(guardY))
#print(currentRow)
#print(len(map))

# guard walks
x = guardX
y = guardY
numGuardPos = 1

# previous conditionL x>=0 and y>=0 and x<currentRow and y<len(map):
# change condition so I am sure that it will exit from the map
while not ( 
    (x==0 and guardChar == "<")
    or (y==0 and guardChar == "^")
    or (x==len(map)-1 and guardChar == ">")
    or (y==len(map)-1 and guardChar == "v")
    ):
    try:
        match guardChar:
        # Facing north:
            case "^":
                while y>0 and map[y-1][x]!="#":
                    map[y][x]="X"
                    y -= 1
                if map[y-1][x]=="#":
                    guardChar = ">"        

        # Facing east:
            case ">":
                while x<len(map) and map[y][x+1]!="#":
                    map[y][x]="X"
                    x += 1
                if map[y][x+1]=="#":
                    guardChar = "v"      

        # Facing south:
            case "v":
                while y<len(map) and map[y+1][x]!="#":
                    map[y][x]="X"
                    y += 1
                if map[y+1][x]=="#":
                    guardChar = "<"      

        # Facing west:
            case "<":
                while x>0 and map[y][x-1]!="#":
                    map[y][x]="X"
                    x -= 1
                if map[y][x-1]=="#":
                    guardChar = "^"
    except:
       map[y][x]="X"
       break

    # debug: don't print whole map, just current status
    part1=0
    for i in range(len(map)):
        part1 += map[i].count("X")
    print("num X = " + str(part1) + ", x=" + str(x) + ", y=" + str(y) + ", direction = " + guardChar)


print(str(x) + ", " + str(y) + "\n")
part1=0
for i in range(len(map)):
    part1 += map[i].count("X")
    print(map[i])


print("part 1 = " + str(part1))
## first attempt: 4884 too high
## second attempt after adjusting the < and <= --> 4882 too low (and the code hangs)
## num X = 4882, x=95, y=0, direction = ^ --> it does not exit the while loop
## solution then is 4883 but still I have to fix the code