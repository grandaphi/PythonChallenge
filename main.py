prog = input("""
For Prime Factors enter 1.
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
    import sort_string
elif prog == "4":
    import find_indices
elif prog == "5":
    import waiting_game
elif prog == "6":
    import dict_file
else:
    print("""
No valid option selected, exiting.
""")
