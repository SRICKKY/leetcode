
arraySize = int(input())

A = [int(x) for x in input().split()]
# print(A)
largestPrimeFactor

def largestPrimeFactor(num):
    i = 2

    while i * i <= num:
        if num % i: i += 1
        else: num //= i
    
    return num


def magicValue(arraySize, A):
    output = []

    for idx, val in enumerate(A):
        if idx == 0:
            output.append(0)
        elif idx == 1:
            output.append(1)
        else:
            output.append(largestPrimeFactor(idx))

    print(max(output))

magicValue(arraySize, A)