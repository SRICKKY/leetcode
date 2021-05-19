def change(amount, coins):

    dp = [0] * (amount + 1)
    dp[0] = 1

    for coin in coins:
        # print("-------------------------------------")
        for index in range(amount+1):
            if index >= coin:
                dp[index] += dp[index - coin]
        print(dp)
        print("=====================================")
    
    return dp[-1]
    

# print(change(6, [2, 3, 4]))
print(change(5, [1, 2, 5]))
