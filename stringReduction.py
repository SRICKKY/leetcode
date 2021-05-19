def stringReduction(s):
    d = [0] * 3

    for letter in s:
        if letter == 'a':
            d[0] += 1
        elif letter == 'b':
            d[1] += 1
        else:
            d[2] += 1
    print(d)

    while True:
        count = 0
        for i in d:
            if i == 0:
                count += 1
        if count >= 2:
            break

        d.sort(reverse=True)
        d[0] += -1
        d[1] += -1
        d[2] += 1

    sum = 0
    for i in d: sum += i
    
    return sum
    # print(sum)

stringReduction("cab")
stringReduction("bcab")
stringReduction("ccccc")