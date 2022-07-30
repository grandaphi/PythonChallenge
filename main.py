prog = input("""
For Integers enter 1.
For palindrome enter 2.
For sorting strings enter 3.
For finding indices, enter 4.
For waiting game, enter 5.
For dictionary file, enter 6.
""")

if prog == "1":
    import factors
elif prog == "2":
    import palindrome
elif prog == "3":
    import sortString
elif prog == "4":
    import findIndices
elif prog == "5":
    import waitingGame
elif prog == "6":
    import dictFile
else:
    print("""
No valid option selected, exiting.
""")
