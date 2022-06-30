#  identify if input is a palindrome
import re
done = False

while not(done):
    try:
        value = input("""
Enter a string
""")
        if not re.findall("[a-zA-Z]",value):
            raise ValueError
        else:
            done = True
    except ValueError:
        print("error with that value please try again and enter a string.")
    except:
        print("\n\r\n\rUknown error, exiting.")
        raise

stripped = re.findall("[a-zA-Z]",value)
    
print(stripped)

length=len(stripped)

for i in range(length):
    if stripped[i]==stripped[(length-1)-i]:
        palindrome = True
    else:
        palindrome = False

if palindrome:
    print("this is a palindrome")
else:
    print("this is not a palindrome")


