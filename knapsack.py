def knapsack(capacity, weights, values):
    """
    Solve the 0/1 Knapsack problem using dynamic programming.
    
    :param capacity: int - The maximum capacity of the knapsack.
    :param weights: List[int] - The weights of the items.
    :param values: List[int] - The values of the items.
    :return: Tuple[int, List[int]] - Maximum achievable profit and list of selected items.
    """
    if not weights or not values or len(weights) != len(values) or capacity < 0:
        raise ValueError("Invalid input")

    n = len(weights)

    # Create a DP table
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    # Fill the DP table
    for i in range(1, n + 1):
        weight = weights[i - 1]
        value = values[i - 1]
        for w in range(1, capacity + 1):
            # Do not take the current item
            dp[i][w] = dp[i - 1][w]
            # Take the current item (if it fits)
            if w >= weight:
                dp[i][w] = max(dp[i][w], dp[i - 1][w - weight] + value)

    # Backtrack to find the selected items
    selected_items = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:  # If the value came from taking the item
            selected_items.append(i - 1)  # Add the item's index
            w -= weights[i - 1]  # Decrease the remaining capacity

    # The maximum profit is stored in dp[n][capacity]
    return dp[n][capacity], selected_items


# Example usage
if __name__ == "__main__":
    # Example 1
    capacity = 10
    values = [1, 4, 8, 5]
    weights = [3, 3, 5, 6]
    max_profit, items = knapsack(capacity, weights, values)
    print(f"Maximum Profit: {max_profit}, Selected Items: {items}")

    # Example 2
    capacity = 7
    values = [2, 2, 4, 5, 3]
    weights = [3, 1, 3, 4, 2]
    max_profit, items = knapsack(capacity, weights, values)
    print(f"Maximum Profit: {max_profit}, Selected Items: {items}")

