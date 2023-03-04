test_list = ["foo","bar","baz",["","foo",["foo","bar","baz",["foo"]]],["foo","bar","baz",["foo"]]]
test_value = "foo"
# correctoutput = [0,[3,1],[3,2,0],[3,2,3,0],[4,0],[4,3,0]]
indices = []
temp_indices = []
temporary = []

def find_indices(List,Value):
    for x in range(len(List)):
        try:
            if List[x] == Value:
                if len(temp_indices) > 0:
                    temp_indices.append(x)
                    indices.append(temp_indices.copy())
                    temp_indices.pop()
                    
                else:
                    indices.append(x)
                    
            elif isinstance(List[x],list):
                temp_indices.append(x)
                find_indices(List[x],Value)
                
        except ValueError:
            pass
    try:
        if len(temp_indices) > 0:
            temp_indices.pop()
            
    except:
        pass

find_indices(test_list,test_value)
print(indices)
        
                    
                    