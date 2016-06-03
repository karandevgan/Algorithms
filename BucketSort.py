from InsertionSort import InsertionSort

def BucketSort(elements, max_element):
    number_of_buckets = len(elements)
    size_of_bucket = max_element/number_of_buckets + 1
    buckets = [[] for _ in xrange(number_of_buckets)]

    for i in xrange(len(elements)):
        bucket_index = elements[i]/size_of_bucket
        buckets[bucket_index].append(elements[i])

    elements = [0] * len(elements)

    element_index = 0
    for bucket in buckets:
        if len(bucket) > 0:
            for j in xrange(len(bucket)):
                elements[element_index] = bucket[j]
                element_index += 1

    return InsertionSort(elements)

print BucketSort([29,25,3,49,9,37,21,43], 49)
