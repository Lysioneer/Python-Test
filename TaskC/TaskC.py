from email import charset
from pickle import FALSE
from unittest import result


stringInput = input()

charList = list(stringInput)

occurrenceDict = {}

for char in charList:
    
    occDictKeys = list(occurrenceDict.keys())

    if occDictKeys.__contains__(char) is False:
        occurrenceDict[char] = 1
    else:
        occValue = int(occurrenceDict.get(char))
        occValue = occValue + 1
        occurrenceDict[char] = occValue

resultDict = {}

def get_key(val):
    for key, value in occurrenceDict.items():
         if val == value:
             return key
 
    return "key doesn't exist"

def getMostOccurrs(input):
    occKey = ""
    occValue = 0
    for occ in input:
        if input.get(occ) > occValue:
            occKey = get_key(input.get(occ))
            occValue = input.get(occ)
    occurrenceDict.pop(occKey)
    resultDict[occKey] = str(occValue)


getMostOccurrs(occurrenceDict)
getMostOccurrs(occurrenceDict)
getMostOccurrs(occurrenceDict)

sorted(resultDict.items(), key=lambda x: (-x[1],x[0]))

for resultLetter in resultDict:
    print (resultLetter, resultDict[resultLetter])