arr = [10, 20, 20, 10, 10, 30, 50, 10, 20]


sock = dict()

for x in arr:
    if x not in sock.keys():
        sock[x] = 1
    else:
        sock[x] += 1

count = 0
for v in sock.values():
    count += v // 2

print(count)
