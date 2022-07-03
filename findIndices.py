#  find indices of matched objects in list, including lists of any depth
#  must take two arguments; 1. list to search, and 2. value to match
#  must have one output; 1. list of indices
indexList = []

testList = ["foo","bar","baz",["foo"]]
testValue = "foo"

def findIndices(List,Value):
    for x in range(len(List)):
        try:
            if List[x] == Value:
                print(x)
            if isinstance(List[x],list):
                findIndices(List[x],Value)
        except ValueError:
            pass

        
        
findIndices(testList,testValue)


# def findIndices(list,value):
#     try:
#         valIndex = list.index(value)
#         print(valIndex)
#         indexList.append(valIndex)
#         valIndex=list[valIndex+1:].index(value)
#         indexList.append(valIndex+1)
#         #  call findIndices again but with limited range based on last found index, pass optional index argumnet. default is 0
#         #  what about other depths in list? find dimensions with recursion?
        
#     except:
#         print('nothing')
#     return indexList

# print(findIndices(List,Value))






