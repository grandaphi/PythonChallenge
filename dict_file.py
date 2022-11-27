#  function 1:
#  create dictionary & save to a file
#  inputs : dictionary and filename
#  outputs: file path

#  function 2:
#  read dictionary from file
#  inputs: file path
#  outputs: dictionary data


def dict_file():
    file_path = "dictionary_file.txt"
    numPairs = int(input("How many key value pairs do you wish to enter?"))

    dictionary = dict(
        input(
            str("Input key value pair (separated by space) #: " + str(_ + 1) +
                "/" + str(numPairs))).split() for _ in range(numPairs))
    f = open(file_path, "w")
    f.write(str(dictionary))
    f.close()

    f = open(file_path)
    print(f.read())
    return(file_path)
    

path = dict_file()

def open_file(file_path):
    fp = input("Enter your file path")
    if fp:
        file_path = fp
    else: 
        pass

    f = open(file_path)
    print(f.read())

open_file(path)

        

    
    
    