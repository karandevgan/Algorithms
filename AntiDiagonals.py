def diagonal(a):
    number_of_rows = (2 * len(a)) - 1
    return_list = [[] for _ in xrange(number_of_rows)]
    for i in xrange(len(a)):
        for j in xrange(len(a)):
            return_list[i+j].append(a[i][j])
    return return_list

print diagonal([[1,2,3],[4,5,6],[7,8,9]])
