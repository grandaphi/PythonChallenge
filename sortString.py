#  accept input string and sort words alaphabetically and return them, with case as was input
#  solution found in W3schools refernce string.split () method and list.sort() method with key=str.lower to ignore case
#  .join method to return list as string , as per spec in challenge

def SortString():
    rawString = input("Enter a string to have the words sorted alphabetically:\n\r")

    splitList = rawString.split()

    splitList.sort(key = str.lower)

    jointString = ' '.join(splitList)

    print(jointString)

    return

SortString()