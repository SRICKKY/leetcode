# 274. H-Index

def hIndex(citations):
    if len(citations) < 1: return 0
    if len(citations) == 1: return 1 if citations[0] != 0 else 0 
            
    hash = dict()
    
    for val in citations:
        if val == 0: continue
        hash[val] = 0
        
        for x in citations:
            if x == 0: continue
            if x >= val:
                hash[val] += 1

    return max(hash, key=hash.get)

print(hIndex([1, 2, 3]))
print(hIndex([1]))
print(hIndex([100]))
print(hIndex([0]))
print(hIndex([11, 15]))
