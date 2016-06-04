def InsertionSort(elements, start=0, end=None):
    if end == None:
        end = len(elements) - 1
    for i in xrange(start+1, end+1):
        key = elements[i]
        j = i - 1
        while j >= start and elements[j] > key:
            elements[j+1] = elements[j]
            j -= 1
        elements[j+1] = key
    return elements

if __name__ == "__main__":
    print InsertionSort([1,2,4,5,3,6])
