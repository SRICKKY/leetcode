# 322. Coin Change


def coinChange(coins, amount):

	dp = [0] + [amount + 1] * amount

	print(dp)

	for value in range(amount+1):
		for coin in (coins):
			if coin <= value:
				print("Coin ", coin, "<= Value ", value)
				dp[value] = min(dp[value], 1 + dp[value - coin])				

		print(dp)
		print()

	return -1 if dp[amount] > amount else dp[amount]

# coins = [1, 2, 5], amount = 11
coinChange([1, 2, 5], 11)