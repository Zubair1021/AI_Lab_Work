# ---------------------Task1 (Edit Distance)---------------------

"""
#----Simple Iterative
def edit_distance_iterative(str1, str2):
    len1, len2 = len(str1), len(str2)
    dp = [[0] * (len2 + 1) for _ in range(len1 + 1)]

    for i in range(len1 + 1):
        for j in range(len2 + 1):
            if i == 0:
                dp[i][j] = j 
            elif j == 0:
                dp[i][j] = i 
            elif str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]  
            else:
                dp[i][j] = 1 + min(dp[i-1][j],    
                                   dp[i][j-1],    
                                   dp[i-1][j-1]) 
    return dp[len1][len2]

#----Recursive
def edit_distance_recursive(str1, str2, len1, len2):
    if len1 == 0:
        return len2  
    if len2 == 0:
        return len1
    
    if str1[len1-1] == str2[len2-1]:
        return edit_distance_recursive(str1, str2, len1-1, len2-1)  

    return 1 + min(edit_distance_recursive(str1, str2, len1-1, len2),  
                   edit_distance_recursive(str1, str2, len1, len2-1),    
                   edit_distance_recursive(str1, str2, len1-1, len2-1))  


#----DP(Memoization)

def edit_distance_memoization(str1, str2):
    memo = {}

    def helper(len1, len2):
        if len1 == 0:
            return len2
        if len2 == 0:
            return len1
        
        if (len1, len2) in memo:
            return memo[(len1, len2)]
        
        if str1[len1-1] == str2[len2-1]:
            memo[(len1, len2)] = helper(len1-1, len2-1)
        else:
            memo[(len1, len2)] = 1 + min(helper(len1-1, len2),    
                                         helper(len1, len2-1),   
                                         helper(len1-1, len2-1)) 
        return memo[(len1, len2)]
    
    return helper(len(str1), len(str2))

#----DP(Tabulation)

def edit_distance_tabulation(str1, str2):
    len1, len2 = len(str1), len(str2)
    dp = [[0] * (len2 + 1) for _ in range(len1 + 1)]

    for i in range(len1 + 1):
        for j in range(len2 + 1):
            if i == 0:
                dp[i][j] = j  
            elif j == 0:
                dp[i][j] = i 
            elif str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1] 
            else:
                dp[i][j] = 1 + min(dp[i-1][j],   
                                   dp[i][j-1],  
                                   dp[i-1][j-1]) 
    return dp[len1][len2]

#--------------------------------------------
str1 = "kitten"
str2 = "sitting"

print("Iterative Result:", edit_distance_iterative(str1, str2))
print("Recursive Result:", edit_distance_recursive(str1, str2, len(str1), len(str2)))
print("Memoization Result:", edit_distance_memoization(str1, str2))
print("Tabulation Result:", edit_distance_tabulation(str1, str2))

"""



# ---------------------Task2 (Balancing an unbalanced bracket sequence)---------------------

"""

#----Simple Iterative
def balance_brackets_iterative(s):
    open_count = 0   
    close_needed = 0  
    
    for char in s:
        if char == '(':
            open_count += 1
        elif char == ')':
            if open_count > 0:
                open_count -= 1  
            else:
                close_needed += 1 
    return '(' * close_needed + s + ')' * open_count

#----Recursive
def balance_brackets_recursive(s, idx=0, open_count=0, close_needed=0):
    if idx == len(s):
        return '(' * close_needed + s + ')' * open_count
    
    if s[idx] == '(':
        return balance_brackets_recursive(s, idx + 1, open_count + 1, close_needed)
    elif s[idx] == ')':
        if open_count > 0:
            return balance_brackets_recursive(s, idx + 1, open_count - 1, close_needed)
        else:
            return balance_brackets_recursive(s, idx + 1, open_count, close_needed + 1)
    return balance_brackets_recursive(s, idx + 1, open_count, close_needed)

#----DP(Memoization)
def balance_brackets_memoization(s):
    memo = {}

    def helper(idx, open_count, close_needed):
        if idx == len(s):
            return '(' * close_needed + s + ')' * open_count
        
        if (idx, open_count, close_needed) in memo:
            return memo[(idx, open_count, close_needed)]
        
        if s[idx] == '(':
            memo[(idx, open_count, close_needed)] = helper(idx + 1, open_count + 1, close_needed)
        elif s[idx] == ')':
            if open_count > 0:
                memo[(idx, open_count, close_needed)] = helper(idx + 1, open_count - 1, close_needed)
            else:
                memo[(idx, open_count, close_needed)] = helper(idx + 1, open_count, close_needed + 1)
        else:
            memo[(idx, open_count, close_needed)] = helper(idx + 1, open_count, close_needed)
        
        return memo[(idx, open_count, close_needed)]
    
    return helper(0, 0, 0)


#----DP(Tabulation)
def balance_brackets_tabulation(s):
    open_count = 0   
    close_needed = 0  
    
    for char in s:
        if char == '(':
            open_count += 1
        elif char == ')':
            if open_count > 0:
                open_count -= 1
            else:
                close_needed += 1

    result = '(' * close_needed + s + ')' * open_count
    return result


#------------------------------------------------------

s = "(a+b(c"

print("Iterative Result:", balance_brackets_iterative(s))
print("Recursive Result:", balance_brackets_recursive(s))
print("Memoization Result:", balance_brackets_memoization(s))
print("Tabulation Result:", balance_brackets_tabulation(s))

"""


# ---------------------Task3 (Sequence Alignment of Two Biological Sequences)---------------------

# I solve this problem using Dynamic Programming.Tabulation Technique is more effeicent so i use this:


"""
def sequence_alignment(S, T, match=1, mismatch=-1, gap=-2):
    n = len(S)
    m = len(T)
    

    dp = [[0] * (m + 1) for _ in range(n + 1)]
    

    for i in range(1, n + 1):
        dp[i][0] = dp[i - 1][0] + gap
    for j in range(1, m + 1):
        dp[0][j] = dp[0][j - 1] + gap

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if S[i - 1] == T[j - 1]:
                score = match  
            else:
                score = mismatch  
            dp[i][j] = max(
                dp[i - 1][j] + gap,      
                dp[i][j - 1] + gap,      
                dp[i - 1][j - 1] + score  
            )
    

    alignment_score = dp[n][m]

    aligned_S = []
    aligned_T = []
    
    i, j = n, m
    while i > 0 or j > 0:
        if i > 0 and dp[i][j] == dp[i - 1][j] + gap:
            aligned_S.append(S[i - 1])
            aligned_T.append('-')  
            i -= 1
        elif j > 0 and dp[i][j] == dp[i][j - 1] + gap:
            aligned_S.append('-')
            aligned_T.append(T[j - 1])  
            j -= 1
        else:
            aligned_S.append(S[i - 1])
            aligned_T.append(T[j - 1])
            i -= 1
            j -= 1

    aligned_S.reverse()
    aligned_T.reverse()
    
    return alignment_score, ''.join(aligned_S), ''.join(aligned_T)

#---------------------------------------------
S = "ACG"
T = "AG"
alignment_score, aligned_S, aligned_T = sequence_alignment(S, T)
print("Alignment Score:", alignment_score)
print("Aligned S:", aligned_S)
print("Aligned T:", aligned_T)


"""


# ---------------------Task4 (Minimum Coin Change Problem)---------------------

#------Simple iterative 
def coin_change_iterative(coins, target):
    dp = [float('inf')] * (target + 1)
    dp[0] = 0
    for coin in coins:
        for i in range(coin, target + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[target] if dp[target] != float('inf') else -1

#------Recursive 
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






coins = [9, 6, 5,1]
target = 13

print("Minimum Coin Change(Iterative):", coin_change_iterative(coins, target))
print("Minimum Coin Change(Recursive):", coin_change_recursive(coins, target))
print("Minimum Coin Change(Memoization):", coin_change_memo(coins, target))
print("Minimum Coin Change(Tabulation):", coin_change_tabulation(coins, target))


