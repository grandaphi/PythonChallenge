#  find unique words in file and list top ten most common words
test = "one two three one"
with open("pg100.txt",'r') as file:
    lines = [line.strip().strip('.').strip(';').strip(':').split() for line in file]
#  append if no match
#  increment count if match
# print(lines)

#  TODO:  work better with alphanumerics and also ignore case
wordict ={}

for i in range(len(lines)):
    for j in range(len(lines[i])):
        if not(lines[i][j] in wordict):
            wordict[lines[i][j]]=1
        else:
            wordict[lines[i][j]]+=1

print(wordict)

#    for j in test.split():
#        if test.split()[i] == test.split()[i+j]:
#            print("match")

