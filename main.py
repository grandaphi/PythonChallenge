prog = input("""
For Integers enter 1.
For palindrome enter 2.
For Sorting Strings enter 3.
""")

if prog == "1":
    import factors
elif prog == "2":
    import palindrome
elif prog == "3":
    import sortString
else:
    print("""
No valid option selected, exiting.
""")


    