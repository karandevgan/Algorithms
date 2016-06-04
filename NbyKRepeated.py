def repeatedNumber(A):
    '''
        Returns any number which is repeated more than n/k times in the list,
        where n is the length of the list
    '''
    dict = {}
    divisor = 3
    for integer in A:
        if dict.get(integer) is None:
            if len(dict) != divisor-1:
                dict[integer] = 1
            else:
                isAdded = False
                for key, value in dict.iteritems():
                    if value == 0:
                        isAdded = True
                        del key
                        dict[integer] = 1
                    break
                if not isAdded:
                    for key, value in dict.iteritems():
                        value -= 1
                        dict[key] = value
        else:
            dict[integer] += 1

    for key, value in dict.iteritems():
        dict[key] = 0

    for integer in A:
        if dict.get(integer) != None:
            dict[integer] += 1
            if dict[integer] > len(A) / divisor:
                return integer

    return -1

A = []
print repeatedNumber(A)
