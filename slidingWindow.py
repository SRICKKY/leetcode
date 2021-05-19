# Sliding Window Technique
import sys

def maxSumSubArray(arr, k):

	currentSum = 0
	maxValue = - sys.maxsize - 1


	for i, v in enumerate(arr):
		currentSum += v

		if i >= k-1:
			maxValue = max(maxValue, currentSum)
			print("window: ", arr[i - (k - 1):i+1], maxValue)
			currentSum -= arr[i - (k - 1)]

	return maxValue

# print(maxSumSubArray([1, 4, 2, 7, 9, 3, 5], 3))
# print(maxSumSubArray([1, 4, 2, -1, 9, 3, 5], 4))
print(maxSumSubArray([1, 4, 2, -1, 9, 3, 5], 2))
print(maxSumSubArray([1, 4, 2, -1, 9, 3, 5], 5))



# lastIndex = i - (k - 1)
	