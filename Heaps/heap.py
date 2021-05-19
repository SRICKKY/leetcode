# Heap Implementation

class Heap:
	def __init__(self):
		self.heap = [None]
		self.size = 0

	def __str__(self):
		out = ""
		for i in range(1, self.size + 1):
			out += str(self.heap[i]) + " "
		return out

# Heap Implementation using builtins Python module
from heapq import heappush, heappop, heapify
import heapq

h = [21, 1, 45, 78, 3, 5]
heapify(h) # inplace, its min_heapify
print(h)
heapq._heapify_max(h) # max_heapify
print(h)
