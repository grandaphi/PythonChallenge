#  function 1:
#  create dictionary & save to a file
#  inputs : dictionary and filename
#  outputs: file path

#  function 2:
#  read dictionary from file
#  inputs: file path
#  outputs: dictionary data


def dictFile():
    numPairs = int(input("How many key value pairs do you wish to enter?"))

    dictionary = dict(
        input(
            str("Input key value pair (separated by space) #: " + str(_ + 1) +
                "/" + str(numPairs))).split() for _ in range(numPairs))
    f = open("dictionary_file.txt", "w")
    f.write(str(dictionary))
    f.close()

    f = open("dictionary_file.txt")
    print(f.read())
    

dictFile()
