#  accept input string and sort words alaphabetically and return them, with case as was input
#  solution found in W3schools refernce string.split () method and list.sort() method with key=str.lower to ignore case
#  .join method to return list as string , as per spec in challenge

def sort_string():
    raw_string = input("Enter a string to have the words sorted alphabetically:\n\r")

    split_list = raw_string.split()

    split_list.sort(key = str.lower)

    joint_string = ' '.join(split_list)

    print(joint_string)

    return

sort_string()