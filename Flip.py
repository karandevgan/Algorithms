def Flip(A):
    zero_count = 0
    max_zero_count = 0
    start_index = None
    last_index = None
    for index in range(0, len(A)):
        if A[index] == '0':
            if start_index is None:
                start_index = index
                temp_start_index = index
            if zero_count < 0:
                temp_start_index = index
                zero_count = 0
            zero_count += 1
            if zero_count > max_zero_count:
                start_index = temp_start_index
                last_index = index
                max_zero_count = zero_count
        elif start_index != None:
            zero_count -= 1
    if start_index != None and last_index != None:
        return [start_index+1, last_index+1]
    else:
        return []

#print Flip('1101010001')
print Flip('0111000100010')
