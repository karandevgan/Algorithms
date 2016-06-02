def generateMatrix(A):
    return_list = [[0 for _ in range(A)] for _ in range(A)]
    limit_left = 0
    limit_down = A-1
    limit_top = 1
    limit_right = A-1
    num = 1
    i = 0
    j = 0
    total_elements = A*A
    while (num <= total_elements):
        while (j<=limit_right):
            return_list[i][j] = num
            num += 1
            j += 1
        j -= 1
        i = limit_top
        limit_right -= 1

        while (i<=limit_down):
            return_list[i][j] = num
            num += 1
            i += 1

        i -= 1
        j = limit_right
        limit_down -= 1

        while (j>=limit_left):
            return_list[i][j] = num
            num += 1
            j -= 1

        j += 1
        i = limit_down
        limit_left += 1

        while (i>=limit_top):
            return_list[i][j] = num
            num += 1
            i -= 1

        i += 1
        j = limit_left
        limit_top += 1

    return return_list

print generateMatrix(0)
