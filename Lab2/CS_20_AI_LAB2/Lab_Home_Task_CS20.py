#--------------------Task 1 Fibonacci Series / Home Task 1 

#------Simple iterative 

"""
def fibonacci(n):
    fib_sequence = [0, 1]
    for i in range(2, n):
        next_number = fib_sequence[-1] + fib_sequence[-2]
        #print(fib_sequence[-1],fib_sequence[-2])
        fib_sequence.append(next_number)
    return fib_sequence


n = 6
fib_numbers = fibonacci(n)
print(fib_numbers)

"""

#------Simple Recursive 

"""
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

for i in range(6):
    print(fibonacci(i))
    
"""   

#------Dynamic Programming(Memoization)

""" 
def fibonacci(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)
    return memo[n]

for i in range(6):
    print(fibonacci(i))
    
    
"""     
    
    
#------Dynamic Programming(Tabulation)

"""  
def fibonacci(n):
    fib_table = [0] * (n + 1)
    fib_table[0] = 0
    if n > 0:
        fib_table[1] = 1
    for i in range(2, n + 1):
        fib_table[i] = fib_table[i - 1] + fib_table[i - 2]

    return fib_table[n]

for i in range(6):
    print(fibonacci(i))
    
"""    


#--------------------Task 2 Longest Common SubString / Home Task 3

#------Simple iterative 

"""
def longest_common_substring(s1, s2):
    m = len(s1)
    n = len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    longest_length = 0

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1  
                longest_length = max(longest_length, dp[i][j])  
            else:
                dp[i][j] = 0  
    return longest_length


s1 = "abcde"
s2 = "abcfce"
result = longest_common_substring(s1, s2)
print("Length of Longest Common Substring:", result)

"""


#------Simple Recursive 


"""
def longest_common_substring(s1, s2, m, n, count):
    if m == 0 or n == 0:
        return count
    if s1[m - 1] == s2[n - 1]:
        count = longest_common_substring(s1, s2, m - 1, n - 1, count + 1)
    return max(count, longest_common_substring(s1, s2, m - 1, n, 0), longest_common_substring(s1, s2, m, n - 1, 0))

s1 = "abcde"
s2 = "abcfce"
result = longest_common_substring(s1, s2, len(s1), len(s2), 0)
print("Length of Longest Common Substring:", result)

"""

#------Dynamic Programming(Memoization)

"""
def longest_common_substring_memo(s1, s2):
    memo = {}

    def helper(i, j, count):
        if i == 0 or j == 0:
            return count
        
        if (i, j, count) in memo:
            return memo[(i, j, count)]
        
        if s1[i - 1] == s2[j - 1]:
            count = helper(i - 1, j - 1, count + 1)
        
        result = max(count, max(helper(i, j - 1, 0), helper(i - 1, j, 0)))
        memo[(i, j, count)] = result
        return result

    return helper(len(s1), len(s2), 0)


s1 = "abcde"
s2 = "abfce"
print(longest_common_substring_memo(s1,s2))


"""

#------Dynamic Programming(Tabulation)

"""
def longest_common_substring_tabulation(s1, s2):
    # Initialize the DP table with zeros
    dp = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]
    max_len = 0

    # Fill the DP table
    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                max_len = max(max_len, dp[i][j])

    return max_len


s1 = "abcde"
s2 = "abfce"
print(longest_common_substring_tabulation(s1,s2))
"""

#--------------------Task 3 Max Value of Cutting and Selling Pieces

#------Simple iterative 
"""
def rod_cutting_iterative(prices, n):
    dp = [0] * (n + 1)
    
    for length in range(1, n + 1):
        for cut in range(length):
            dp[length] = max(dp[length], prices[cut] + dp[length - cut - 1])
    
    return dp[n]

# Example usage
prices = [1, 5, 8, 9, 10, 17, 17, 20]
n = 8
result = rod_cutting_iterative(prices, n)
print("Maximum Obtainable Value (Iterative):", result)
"""

#------Simple Recursive 
"""
def rod_cutting_recursive(prices, n):
    if n <= 0:
        return 0
    max_value = float('-inf')
    for i in range(n):
        max_value = max(max_value, prices[i] + rod_cutting_recursive(prices, n - i - 1))
    return max_value

# Example usage
prices = [1, 5, 8, 9, 10, 17, 17, 20]
n = 8
result = rod_cutting_recursive(prices, n)
print("Maximum Obtainable Value (Recursive):", result)
"""

#------Dynamic Programming(Memoization)
"""
def rod_cutting_memo(prices, n, memo):
    if n <= 0:
        return 0
    if memo[n] != -1:
        return memo[n]
    
    max_value = float('-inf')
    for i in range(n):
        max_value = max(max_value, prices[i] + rod_cutting_memo(prices, n - i - 1, memo))
    
    memo[n] = max_value
    return max_value

def rod_cutting(prices, n):
    memo = [-1] * (n + 1)
    return rod_cutting_memo(prices, n, memo)

# Example usage
prices = [1, 5, 8, 9, 10, 17, 17, 20]
n = 8
result = rod_cutting(prices, n)
print("Maximum Obtainable Value (Memoization):", result)
"""
#------Dynamic Programming(Tabulation)
"""
def rod_cutting_tabulation(prices, n):
    dp = [0] * (n + 1)
    
    for i in range(1, n + 1):
        max_value = float('-inf')
        for j in range(i):
            max_value = max(max_value, prices[j] + dp[i - j - 1])
        dp[i] = max_value
    
    return dp[n]

# Example usage
prices = [1, 5, 8, 9, 10, 17, 17, 20]
n = 8
result = rod_cutting_tabulation(prices, n)
print("Maximum Obtainable Value (Tabulation):", result)
"""

#--------------------Home Task 2 Minimum Coin Change
 
#------Simple iterative 
"""
def coin_change_iterative(coins, target):
    dp = [float('inf')] * (target + 1)
    dp[0] = 0
    for coin in coins:
        for i in range(coin, target + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[target] if dp[target] != float('inf') else -1

#------Simple Recursive 
def coin_change_recursive(coins, target):
    if target == 0:
        return 0
    if target < 0:
        return float('inf')

    min_coins = float('inf')
    for coin in coins:
        result = coin_change_recursive(coins, target - coin)
        if result != float('inf'):
            min_coins = min(min_coins, result + 1)

    return min_coins if min_coins != float('inf') else -1

#------Dynamic Programming(Memoization)
def coin_change_memo(coins, target):
    memo = {}

    def dp(amount):
        if amount in memo:
            return memo[amount]
        if amount == 0:
            return 0
        if amount < 0:
            return float('inf')

        min_coins = float('inf')
        for coin in coins:
            result = dp(amount - coin)
            if result != float('inf'):
                min_coins = min(min_coins, result + 1)

        memo[amount] = min_coins
        return min_coins

    result = dp(target)
    return result if result != float('inf') else -1

#------Dynamic Programming(Tabulation)
def coin_change_tabulation(coins, target):
    dp = [float('inf')] * (target + 1)
    dp[0] = 0  # Base case

    for i in range(1, target + 1):
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[target] if dp[target] != float('inf') else -1






coins = [1, 2, 5]
target = 11

print("Minimum Coin Change(Iterative):", coin_change_iterative(coins, target))
print("Minimum Coin Change(Recursive):", coin_change_recursive(coins, target))
print("Minimum Coin Change(Memoization):", coin_change_memo(coins, target))
print("Minimum Coin Change(Tabulation):", coin_change_tabulation(coins, target))


"""

#--------------------Home Task 4 Climbing Stairs

"""
#------Simple iterative 
def staircase_iterative(n):
    if n == 0 or n == 1:
        return 1

    prev2, prev1 = 1, 1

    for i in range(2, n + 1):
        current = prev1 + prev2
        prev2 = prev1
        prev1 = current

    return prev1

#------Simple Recursive 
def staircase_recursive(n):
    if n == 0 or n == 1:
        return 1
    return staircase_recursive(n - 1) + staircase_recursive(n - 2)

#------Dynamic Programming(Memoization)
def staircase_memo(n, memo={}):
    if n == 0 or n == 1:
        return 1
    if n in memo:
        return memo[n]
    memo[n] = staircase_memo(n - 1, memo) + staircase_memo(n - 2, memo)
    return memo[n]

#------Dynamic Programming(Tabulation)
def staircase_tabulation(n):
    if n == 0 or n == 1:
        return 1

    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]

n=5
print("Climbing Stairs(Iterative):", staircase_iterative(n))
print("Climbing Stairs(Recursive):", staircase_recursive(n))
print("Climbing Stairs(Memoization):", staircase_memo(n))
print("Climbing Stairs(Tabulation):", staircase_tabulation(n))
"""

#--------------------Home Task 5 Knapsack Problem (0/1)
#------Simple iterative 
def knapsack_iterative(values, weights, W):
    n = len(values)
    dp = [0] * (W + 1)

    for i in range(n):
        for w in range(W, weights[i] - 1, -1):
            dp[w] = max(dp[w], dp[w - weights[i]] + values[i])

    return dp[W]

values = [60, 100, 120]
weights = [10, 20, 30]
W = 50

print("Result(Iterative):",knapsack_iterative(values, weights, W)) 

#------Simple Recursive 
def knapsack_recursive(values, weights, W, n):
    if n == 0 or W == 0:
        return 0

    if weights[n-1] > W:
        return knapsack_recursive(values, weights, W, n-1)
    else:
        return max(
            knapsack_recursive(values, weights, W, n-1), 
            values[n-1] + knapsack_recursive(values, weights, W - weights[n-1], n-1)
        )


values = [60, 100, 120]
weights = [10, 20, 30]
W = 50
n = len(values)

print("Result(Recursive):",knapsack_recursive(values, weights, W, n)) 

#------Dynamic Programming(Memoization)

def knapsack_memo(values, weights, W, n, memo):
    if n == 0 or W == 0:
        return 0

    if (n, W) in memo:
        return memo[(n, W)]

    if weights[n-1] > W:
        memo[(n, W)] = knapsack_memo(values, weights, W, n-1, memo)
    else:
        memo[(n, W)] = max(
            knapsack_memo(values, weights, W, n-1, memo),
            values[n-1] + knapsack_memo(values, weights, W - weights[n-1], n-1, memo)
        )

    return memo[(n, W)]


values = [60, 100, 120]
weights = [10, 20, 30]
W = 50
n = len(values)
memo = {}

print("Result(Memoization):",knapsack_memo(values, weights, W, n, memo))  

#------Dynamic Programming(Tabulation)

def knapsack_tabulation(values, weights, W):
    n = len(values)
    dp = [[0 for x in range(W + 1)] for y in range(n + 1)]

    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                dp[i][w] = 0
            elif weights[i-1] <= w:
                dp[i][w] = max(values[i-1] + dp[i-1][w - weights[i-1]], dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]

    return dp[n][W]

values = [60, 100, 120]
weights = [10, 20, 30]
W = 50

print("Result(Tabulation):",knapsack_tabulation(values, weights, W))


  
    


   