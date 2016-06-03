def CountingSort(numbers, k):
    aux_list = [0 for _ in range(0,k+1)]
    final_list = [0 for _ in range(len(numbers))]

    for index in range(len(numbers)):
        aux_list[numbers[index]] += 1

    for index in range(1,len(aux_list)):
        aux_list[index] += aux_list[index-1]

    for index in range(len(final_list))[::-1]:
        final_list[aux_list[numbers[index]]-1] = numbers[index]
        aux_list[numbers[index]] -= 1

    return final_list

numbers = [6,0,2,0,1,3,4,6,1,3,2]
print CountingSort(numbers, 6)
