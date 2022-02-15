import findFactors as f
done = False

while not(done):
    try:
        val=int(input("Enter an integer to determine prime factors:"))
        done = 1
    except ValueError:
        print("error with that value please try again and enter an integer.")
    except:
        print("\n\r\n\rUknown error, exiting.")
        raise

print("you have entered: ",val)

isprime,factors = f.findFactors(val)

if isprime == 1:
    print(val,"is a prime number i.e. the only factors are itself and 1.")
else:
    print(val,"isn't a prime number. Factors are:",factors)

     

