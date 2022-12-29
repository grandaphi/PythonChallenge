# input: n 
# output : random list of n words
from random import randint as r
diceDict = {}

with open("dicelist.txt", 'r') as file:
    for line in file:
        key, value = line.strip().split()
        diceDict[key] = value

def genWords(numWords):
    words = []
    for n in range(numWords):
        diceroll = ""
        for i in range(5):
            diceroll+=str(r(1,6))
        print(diceroll)
        words.append(diceDict[diceroll])
    print(words)
    return words
    
        
