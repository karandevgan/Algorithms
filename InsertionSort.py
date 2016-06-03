def InsertionSort(elements):
    for i in xrange(1, len(elements)):
        key = elements[i]
        j = i - 1
        j_count = 0
        while j >= 0 and elements[j] > key:
            j_count += 1
            elements[j+1] = elements[j]
            j -= 1
        elements[j+1] = key
    return elements

if __name__ == "__main__":
    print InsertionSort([1,2,4,5,3,6])
