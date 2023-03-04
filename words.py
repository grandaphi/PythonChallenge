#  find unique words in file and list top ten most common words
import re, heapq

nMaximaWords = 20
max = 0
topword=[]
wordict ={}
totalWords = 0

filestr = input("Enter filename for word analysis")
with open(filestr,'r') as file:
    lines = [line.split() for line in file]

for i in range(len(lines)):
    for j in range(len(lines[i])):
        word = (re.sub("[^0-9a-zA-Z-']",'',lines[i][j])).lower()
        if not(word in wordict):
            wordict[word]=1
        else:
            wordict[word]+=1
        totalWords+=len(lines[i])

topN = heapq.nlargest(nMaximaWords , wordict, key=wordict.get)


for i, j in wordict.items():
    if i in topN:
        topword.append([i,j])
        max = j

print(topword)
print("Total words: ", totalWords)
