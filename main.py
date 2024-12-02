import re

#gameFile = open("test05.txt", "r")
gameFile = open("input05.txt", "r")
sum = 0

while gameFile:
  line = gameFile.readline().replace("\n", "")
  #print(line)

  if line == "":
    break

  seeds = line.split(": ")[1].split(" ")
  print(seeds)
###############

seedToSoilMatrix = []
while gameFile:
  line = gameFile.readline().replace("\n", "")
  #print(line)

  if line == "":
    break
  if line == "seed-to-soil map:":
    continue  

  seedToSoil= line.split(" ")
  print(seedToSoil)
  seedToSoilMatrix.append([int(x) for x in seedToSoil])
#############

print(seedToSoilMatrix)

#print(len(seedToSoilMatrix))
def getSoil(seed):
    for i in range(len(seedToSoilMatrix)):
        #print(i)
        #print(seedToSoilMatrix[i][1], seedToSoilMatrix[i][1]+seedToSoilMatrix[i][2]-1)
        if seed >= seedToSoilMatrix[i][1] and seed < seedToSoilMatrix[i][1]+seedToSoilMatrix[i][2]:
            return seedToSoilMatrix[i][0] + (seed - seedToSoilMatrix[i][1])
    return(seed)

#########################
###### repeat for the other maps ###########################

soilToFertilizerMatrix = []
while gameFile:
  line = gameFile.readline().replace("\n", "")
  if line == "":
    break
  if line == "soil-to-fertilizer map:":
    continue  
  soilToFertilizer= line.split(" ")
  soilToFertilizerMatrix.append([int(x) for x in soilToFertilizer])

def getFertilizer(soil):
    for i in range(len(soilToFertilizerMatrix)):
        if soil >= soilToFertilizerMatrix[i][1] and soil < soilToFertilizerMatrix[i][1]+soilToFertilizerMatrix[i][2]:
            return soilToFertilizerMatrix[i][0] + (soil - soilToFertilizerMatrix[i][1])
    return(soil)

#######################################

fertilizerToWaterMatrix = []
while gameFile:
  line = gameFile.readline().replace("\n", "")
  if line == "":
    break
  if line == "fertilizer-to-water map:":
    continue  
  fertilizerToWater= line.split(" ")
  fertilizerToWaterMatrix.append([int(x) for x in fertilizerToWater])

def getWater(fertilizer):
    for i in range(len(fertilizerToWaterMatrix)):
        if fertilizer >= fertilizerToWaterMatrix[i][1] and fertilizer < fertilizerToWaterMatrix[i][1]+fertilizerToWaterMatrix[i][2]:
            return fertilizerToWaterMatrix[i][0] + (fertilizer - fertilizerToWaterMatrix[i][1])
    return(fertilizer)

#######################################

waterToLightMatrix = []
while gameFile:
  line = gameFile.readline().replace("\n", "")
  if line == "":
    break
  if line == "water-to-light map:":
    continue  
  waterToLight= line.split(" ")
  waterToLightMatrix.append([int(x) for x in waterToLight])

def getLight(water):
    for i in range(len(waterToLightMatrix)):
        if water >= waterToLightMatrix[i][1] and water < waterToLightMatrix[i][1]+waterToLightMatrix[i][2]:
            return waterToLightMatrix[i][0] + (water - waterToLightMatrix[i][1])
    return(water)

#######################################

lightToTemperatureMatrix = []
while gameFile:
  line = gameFile.readline().replace("\n", "")
  if line == "":
    break
  if line == "light-to-temperature map:":
    continue  
  lightToTemperature= line.split(" ")
  lightToTemperatureMatrix.append([int(x) for x in lightToTemperature])

def getTemperature(light):
    for i in range(len(lightToTemperatureMatrix)):
        if light >= lightToTemperatureMatrix[i][1] and light < lightToTemperatureMatrix[i][1]+lightToTemperatureMatrix[i][2]:
            return lightToTemperatureMatrix[i][0] + (light - lightToTemperatureMatrix[i][1])
    return(light)

#######################################

temperatureToHumidityMatrix = []
while gameFile:
  line = gameFile.readline().replace("\n", "")
  if line == "":
    break
  if line == "temperature-to-humidity map:":
    continue  
  temperatureToHumidity= line.split(" ")
  temperatureToHumidityMatrix.append([int(x) for x in temperatureToHumidity])

def getHumidity(temperature):
    for i in range(len(temperatureToHumidityMatrix)):
        if temperature >= temperatureToHumidityMatrix[i][1] and temperature < temperatureToHumidityMatrix[i][1]+temperatureToHumidityMatrix[i][2]:
            return temperatureToHumidityMatrix[i][0] + (temperature - temperatureToHumidityMatrix[i][1])
    return(temperature)

#######################################

humidityToLocationMatrix = []
while gameFile:
  line = gameFile.readline().replace("\n", "")
  if line == "":
    break
  if line == "humidity-to-location map:":
    continue  
  humidityToLocation= line.split(" ")
  humidityToLocationMatrix.append([int(x) for x in humidityToLocation])

def getLocation(humidity):
    for i in range(len(humidityToLocationMatrix)):
        if humidity >= humidityToLocationMatrix[i][1] and humidity < humidityToLocationMatrix[i][1]+humidityToLocationMatrix[i][2]:
            return humidityToLocationMatrix[i][0] + (humidity - humidityToLocationMatrix[i][1])
    return(humidity)

"""
print(getSoil(14)
      , getFertilizer(getSoil(14))
      , getWater(getFertilizer(getSoil(14)))
      , getLight(getWater(getFertilizer(getSoil(14))))
      , getTemperature(getLight(getWater(getFertilizer(getSoil(14)))))
      , getHumidity(getTemperature(getLight(getWater(getFertilizer(getSoil(14))))))
      , getLocation(getHumidity(getTemperature(getLight(getWater(getFertilizer(getSoil(14)))))))
      )
"""
#print(getSoil(14))
#print(getLocation(getHumidity(getTemperature(getLight(getWater(getFertilizer(getSoil(55))))))))
#print(getLocation(getHumidity(getTemperature(getLight(getWater(getFertilizer(getSoil(13))))))))

locations = [getLocation(getHumidity(getTemperature(getLight(getWater(getFertilizer(getSoil(int(x)))))))) for x in seeds]
print(min(locations))
gameFile.close()

print("---------seconda parte-------")
#####################################################
rangeSeeds = []
print(range(len(seeds)))
x = 0
while x <= int(len(seeds)/2):
   print(x, seeds[x], seeds[x+1])
   rangeSeeds.append(list(range(int(seeds[x]), int(seeds[x])+int(seeds[x+1]))))
   x+=2
#print(rangeSeeds)
seedsList = [item for sublist in rangeSeeds for item in sublist]
print(len(seedsList))

locations = [getLocation(getHumidity(getTemperature(getLight(getWater(getFertilizer(getSoil(int(x)))))))) for x in seedsList]
print(min(locations))





