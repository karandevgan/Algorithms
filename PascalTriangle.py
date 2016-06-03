def getRow(A):
    if A==0:
        return []
    if A==1:
        return [[1]]
    if A==2:
        return [[1],[1,1]]

    pascal_triangle = [[1],[1,1]]
    prev_row = [1,1]
    next_row = []
    for i in range(3,A+1):
        next_row.append(prev_row[0])
        for j in range(len(prev_row)-1):
            next_row.append(prev_row[j]+prev_row[j+1])
        next_row.append(prev_row[len(prev_row)-1])
        pascal_triangle.append(next_row)
        prev_row = pascal_triangle[-1]
        next_row = []
    return pascal_triangle

print getRow(5)
