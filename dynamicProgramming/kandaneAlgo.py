import unittest


# kadane Algorithms
# Max sum of subArray

def maxSubArraySum(arr):
	'''
	Time Complexity: O(n)
	Space Complexity: O(n)
	'''

	maxSumSoFar = 0
	maxSumEndingHere = 0

	for i in range(len(arr)):
		maxSumEndingHere += arr[i]

		if maxSumEndingHere < 0: maxSumEndingHere = 0
		if maxSumSoFar < maxSumEndingHere: maxSumSoFar = maxSumEndingHere

	return maxSumSoFar


# print(maxSubArraySum([-2, -3, 4, -1, -2, 1, 5, -3]))
# print(maxSubArraySum([-2, 3, 4, -1, -2, 1, 5, -3]))
# print(maxSubArraySum([-2, -3, 4, -1, 2, -1, 5, -3]))

assert maxSubArraySum([-2, -3, 4, -1, -2, 1, 5, -3]) == 7
assert maxSubArraySum([-2, 3, 4, -1, -2, 1, 5, -3]) == 10
assert maxSubArraySum([-2, -3, 4, -1, 2, -1, 5, -3]) == 9



def maxSubArraySum(arr):
	'''
	Brute-Force

	Time Complexity: O(n^2)
	Space Complexity: O(n^2)
	'''

	maxSum = 0
	tempSum = 0

	for i in range(len(arr)):
		tempSum = arr[i]

		for j in range(i+1, len(arr)):
			# tempSum hold  sum of all elements from
			# i to j index (both including)
			tempSum += arr[j]
			if tempSum > maxSum: maxSum = tempSum

	return maxSum

