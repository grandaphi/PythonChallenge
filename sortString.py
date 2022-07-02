# accept input string and sort words alaphabetically and return them, with case as was input

rawString = input("Enter a string to have the words sorted alphabetically:\n\r")
rawString = rawString.split()
print(rawString)

rawString.sort()

print(rawString)