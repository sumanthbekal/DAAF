def knapsack_max_profit(weights, values, capacity):
    num_items = len(weights)
    dp = [0] * (capacity + 1)

    for i in range(num_items):
        for j in range(capacity, weights[i] - 1, -1):
            dp[j] = max(dp[j], dp[j - weights[i]] + values[i])

    return dp[capacity]

# Example usage
weights = [2, 3, 4, 5]
values = [10, 20, 30, 40]
capacity = 10
max_profit = knapsack_max_profit(weights, values, capacity)
print("Maximum Profit:", max_profit)
