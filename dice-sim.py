# dice outcome Monte Carlo simulation
from random import randint

def score(numFaces):
	return randint(1, numFaces)


inputFaces = list(
    map(int,
        input(
            "Enter number of faces, separated by spaces:\n").strip().split()))
numDice = len(inputFaces)
possible = [0 for x in range(numDice) for y in range(inputFaces[x])]

for i in range(int(1E6)):
    outcome = 0
    for j in range(numDice):
            outcome += score(inputFaces[j])
	
    possible[outcome - 1] += 1


for i in range(len(possible)):
    possible[i]/=1E6
    possible[i]*=100
    print(str(i+1)+" : "+str(possible[i]))
                             

