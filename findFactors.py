def findFactors(number):

    factorlist = []
    prime = -1

    i=2
    while i <= (int(number/2)):
        if((number % i)==0):
            factorlist.append(i)
            factorlist.append(int(number/i))
            break
        i += 1

    if len(factorlist) == 0:
        prime = 1
    else:
        prime = 0
        j = 0
        
        while j < len(factorlist):
            areprime, pfactors  = findFactors(factorlist[j])
            if not(areprime):
                factorlist.pop(j)
            factorlist += pfactors
            j += 1
    return prime, factorlist
