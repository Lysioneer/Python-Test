with open('RaceResults.txt') as f:
    results = f.read().splitlines()

resultDict = {}

for result in results:
    tempList = result.split(';')
    resultDict[tempList[0]] = tempList[1]

position = input()

def getKey(val):
    for key, value in resultDict.items():
        if val == value:
            return key
    return "Key doesn't exist"

print (getKey(position))