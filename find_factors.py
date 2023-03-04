def find_factors(number):

    factor_list = []
    prime = -1

    i=2
    while i <= (int(number/2)):
        if((number % i)==0):
            factor_list.append(i)
            factor_list.append(int(number/i))
            break
        i += 1

    if len(factor_list) == 0:
        prime = 1
    else:
        prime = 0
        j = 0
        
        while j < len(factor_list):
            are_prime, p_factors  = find_factors(factor_list[j])
            if not(are_prime):
                factor_list.pop(j)
            factor_list += p_factors
            j += 1
    return prime, factor_list
