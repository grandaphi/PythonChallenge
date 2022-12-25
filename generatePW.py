# input: n 
# output : random list of n words
from random import randint as r
diceDict = {}
diceroll = ""

with open("dicelist.txt", 'r') as file:
    for line in file:
        key, value = line.strip().split()
        diceDict[key] = value

for i in range(5):
    diceroll+=str(r(1,6))
print(diceroll)

print(diceDict[diceroll])                  
#  TODO: generate 5 digit random number for each of n words and return them from the dictionary