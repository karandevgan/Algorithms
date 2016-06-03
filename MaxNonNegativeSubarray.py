def maxset(A):
    start_index = -1
    end_index = -1
    temp_sum = 0
    max_sum = 0
    temp_start_index = -1
    temp_end_index = -1

    for i in range(len(A)):
        if A[i] >= 0:
            temp_sum += A[i]
            if temp_start_index == -1:
                temp_start_index = i
            temp_end_index = i

            if temp_sum > max_sum:
                max_sum = temp_sum
                start_index = temp_start_index
                end_index = temp_end_index
        else:
            temp_sum = 0
            temp_start_index = -1
            temp_end_index = -1

        if temp_sum == max_sum and start_index != temp_start_index:
            if (end_index - start_index) < (temp_end_index - temp_start_index):
                start_index, end_index = temp_start_index, temp_end_index
            elif (end_index - start_index) == (temp_end_index - temp_start_index):
                if start_index > temp_start_index:
                    start_index = temp_start_index
                    end_index = temp_end_index
    if start_index == -1:
        return []
    return A[start_index:end_index+1]

print maxset([-1,-2])
