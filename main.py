prog = input("""
For Integers enter 1.
For palindrome enter 2.
For sorting strings enter 3.
For finding indices, enter 4.
""")

if prog == "1":
    import factors
elif prog == "2":
    import palindrome
elif prog == "3":
    import sortString
elif prog== "4":
    import findIndices
else:
    print("""
No valid option selected, exiting.
""")


    