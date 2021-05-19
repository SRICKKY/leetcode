# 347. Top K Frequent Elements

from collections import Counter
import heapq
from typing import List

def topKFrequent(nums: List[int], k: int) -> List[int]:
    count = Counter(nums)
    return heapq.nlargest(k, count.keys(), key=count.get)

topKFrequent([1,1,1,2,2,3,3,4,4,4,4,4], 2)
topKFrequent([1,1,1,2,2,3,3,4,4,4,4,4,8,5,5,5,5,5,5,5,2,], 2)
topKFrequent([1,1,1,2,2,3,3,4,3,8,9,5,6], 2)