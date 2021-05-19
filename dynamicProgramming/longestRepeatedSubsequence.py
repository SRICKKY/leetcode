# Function to find the length of Longest repeated Subsequence
# of substring X[0..m-1] and X[0..n-1]
def LRSLength(X, m, n):

	# return if we have reached the end of either string
	if m == 0 or n == 0:
		return 0

	# if characters at index m and n matches and index is different
	if X[m - 1] == X[n - 1] and m != n:
		return LRSLength(X, m - 1, n - 1) + 1

	# else if characters at index m and n don't match
	return max(LRSLength(X, m, n - 1), LRSLength(X, m - 1, n))


if __name__ == '__main__':

	X = "ATACTCGGA"
	m = len(X)

	print("Length of Longest Repeating Subsequence is", LRSLength(X, m, m))
