testList = ["foo","bar","baz",["","foo",["foo","bar","baz",["foo"]]],["foo","bar","baz",["foo"]]]
testValue = "foo"
# correctoutput = [0,[3,1],[3,2,0],[3,2,3,0],[4,0],[4,3,0]]
indices = []
tempInds = []
temporary = []

def findInds(List,Value):
    for x in range(len(List)):
        try:
            if List[x] == Value:
                if len(tempInds) > 0:
                    tempInds.append(x)
                    indices.append(tempInds.copy())
                    tempInds.pop()
                    
                else:
                    indices.append(x)
                    
            elif isinstance(List[x],list):
                tempInds.append(x)
                findInds(List[x],Value)
                
        except ValueError:
            pass
    try:
        if len(tempInds) > 0:
            tempInds.pop()
            
    except:
        pass

findInds(testList,testValue)
print(indices)
        
                    
                    