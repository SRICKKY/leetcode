import partitionAlgo

def quick_sort(array, start, end):
    if start >= end:
        return

    p = partitionAlgo.partition(array, start, end)
    quick_sort(array, start, p-1)
    quick_sort(array, p+1, end)

array = [29, 99, 27, 41, 66, 28, 44, 78, 87, 19, 31, 76, 58, 88, 83, 97, 12, 21, 44]

quick_sort(array, 0, len(array) - 1)

# print(array)

