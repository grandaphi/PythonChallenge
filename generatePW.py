# input: n 
# output : random list of n words
from secrets import SystemRandom as s
r = s()
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
            diceroll+=str(r.randint(1,6))
        print(diceroll)
        words.append(diceDict[diceroll])
    return words
    
        
