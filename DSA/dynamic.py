memo = {1: 1, 2: 1}
def fibonacci(n):
    global memo
    # Base case
    if n in memo:
        return n
    
    feb_left = fibonacci(n-1)
    print(n-1, feb_left)
    if n-1 not in memo:
        memo[n-1] = feb_left
    feb_right = fibonacci(n-2)
    print(n-1, feb_right)
    if n-2 not in memo:
        memo[n-2] = feb_right

    return feb_left + feb_right 

memo = {1: 1, 2: 1}
def fibonacci_updated(n):
    global memo
    # Base case
    if n in memo:
        return memo[n]
    
    feb_left = fibonacci_updated(n-1)
    if n-1 not in memo:
        memo[n-1] = feb_left
    feb_right = fibonacci_updated(n-2)

    return feb_left + feb_right 


print(fibonacci_updated(3))
print(fibonacci_updated(4))
print(fibonacci_updated(5))
print(fibonacci_updated(6))
print(fibonacci_updated(1000))


class Fibonacci:
    def __init__(self):
        # Initialize memoization dictionary
        self.memo = {1: 1, 2: 1}

    def compute(self, n):
        # Base case
        if n in self.memo:
            return self.memo[n]

        # Recursive calls
        left = self.compute(n - 1)
        self.memo[n - 1] = left  # Ensure left is memoized

        right = self.compute(n - 2)
        self.memo[n - 2] = right  # Ensure right is memoized

        self.memo[n] = left + right
        return self.memo[n]

# f = Fibonacci().compute(1000)

# Minimum coins
# Given an endless amount of denominations, find the minimum set of coins whose sum matches the required value.
# Test: Coins = {1,4,5}, sum = 13, output = 3 ([4,4,5])


def minimum_coins(coins: list, sum:int) -> int:
    """
    Use Dynamic programming to find the minimum coins required
    Use bottom-up approach to find the minimum coins for sum starting from 1.
    """
    memo = {i: float('inf') for i in range(sum+1)}
    memo[0] = 0

    for i in range(1, sum+1):
        for denomination in coins:
            if i - denomination >= 0:
                memo[i] = min(memo[i], memo[i - denomination] + 1)

    if memo[sum] == float('inf'):
        return -1
    
    return memo[sum]

print(minimum_coins([1,4,5], 13))
print(minimum_coins([1,4,5], 6))
print(minimum_coins([1,4,5], 1))
print(minimum_coins([1,4,5], 4))
print(minimum_coins([1,4,5], 5))


def min_coins_recur(coins: list, sum: int) -> int:
    memo = {i: float('inf') for i in range(sum+1)}
    memo[0] = 0

    if sum == 0:
        return 0

    for coin in coins:
        diff = sum - coin
        if diff >= 0:            
            memo[sum] = min(memo[sum], min_coins_recur(coins, diff) + 1)
    
    return memo[sum]
        
print("Recursive: _________________")
print(min_coins_recur([1,4,5], 13))
print(min_coins_recur([1,4,5], 6))
print(min_coins_recur([1,4,5], 1))
print(min_coins_recur([1,4,5], 4))
print(min_coins_recur([1,4,5], 5))


def min_coins_recur2(coins: list, target: int, memo=None) -> int:
    if memo is None:
        memo = {}

    if target == 0:
        return 0
    if target < 0:
        return float('inf')
    if target in memo:
        return memo[target]

    min_count = float('inf')
    for coin in coins:
        res = min_coins_recur2(coins, target - coin, memo)
        if res != float('inf'):
            min_count = min(min_count, res + 1)

    memo[target] = min_count
    return memo[target]

print("Recursive: _________________")
print(min_coins_recur2([1,4,5], 13))
print(min_coins_recur2([1,4,5], 6))
print(min_coins_recur2([1,4,5], 1))
print(min_coins_recur2([1,4,5], 4))
print(min_coins_recur2([1,4,5], 5))

# Create a class based code
class MinCoins:
    """
    Solve using recursion and memoization
    """
    def __init__(self):
        self.memo = {0: 1}

    def compute(self, coins: list, target: int) -> int:
        if target == 0:
            return 0
        if target < 0:
            return float('inf')
        if target in self.memo:
            return self.memo[target]
        
        min_count = float('inf')
        for coin in coins:
            res = self.compute(coins=coins, target=target-coin)
            if res != float('inf'):
                min_count = min(min_count, res + 1)

        self.memo[target] = min_count
        return min_count
    

print("Class Based -----------")
print(MinCoins().compute([1,4,5], 13))
print(MinCoins().compute([1,4,5], 6))
print(MinCoins().compute([1,4,5], 1))
print(MinCoins().compute([1,4,5], 4))
print(MinCoins().compute([1,4,5], 5))


def possible_coins_set(coins: list[int], sum: int, memo=None) -> int:
    # Initialize memo
    if not memo:
        memo = {0: 1}
    # Base Case
    if sum in memo:
        return memo[sum]

    count = 0

    for coin in coins:
        remaining = sum - coin
        if remaining >=0:
            count += possible_coins_set(coins, remaining, memo)

    memo[sum] = count

    return count
    
print("Possible count: ",possible_coins_set([1,4,5], 7))
    

def maze_count(mz: tuple, start: tuple,  memo=None) -> int:
    """
    mz: tuple (height and width of maze)
    stat: tuple (x, y coordinate)
    """
    mz_height, mz_width = mz[0], mz[1]
    # Initialize with base case
    if memo == None:
        memo = {(mz_height-1, mz_width-1): 1}
    # Return possible count from memo if found
    if start in memo:
        return memo[start]
    
    count = 0
    if start[0] < mz_height-1:
        new_down = (start[0] + 1, start[1])
        count += maze_count(mz, new_down, memo)
    if start[1] < mz_width-1:
        new_right = (start[0], start[1] + 1)
        count += maze_count(mz, new_right, memo)

    memo[start] = count
    return count

import random

print(maze_count((3,3), (0,0)))
assert maze_count((1, 1), (0, 0)) == 1
# Only one cell, already at the destination.

assert maze_count((2, 2), (0, 0)) == 2
# Paths: right→down, down→right

assert maze_count((3, 3), (0, 0)) == 6
# Standard example with 2 steps down and 2 right in any order: C(4,2) = 6

assert maze_count((3, 2), (0, 0)) == 3
# Paths: DDR, DRD, RDD

assert maze_count((2, 3), (0, 0)) == 3
# Paths: RRD, RDR, DRR

assert maze_count((1, 5), (0, 0)) == 1
# Only right moves

assert maze_count((5, 1), (0, 0)) == 1
# Only down moves

# assert maze_count((0, 0), (0, 0)) == 1
# Edge case: already at destination (0x0), still 1 valid path
print(maze_count((15, 5), (0, 0)))

memo = {0: 0, 1: 1, 2: 1}
def tribonacci(n: int) -> int:
    if n in memo:
        return memo[n]
    r = tribonacci(n-1) + tribonacci(n-2) + tribonacci(n-3)
    memo[n] = r
    return r

print(f"Tribonacci of 3: ", tribonacci(3))
print(f"Tribonacci of 4: ", tribonacci(4))
print(f"Tribonacci of 5: ", tribonacci(5))


def max_path_sum(graph, position: int, memo=None) -> int:
    """
    Graph: Contains the position (implicit) with weights.
    Plan: Recursively find the max path sum for subproblems
    Base case: last square position with weight as it's max path cost
    """
    # Initialize memo
    memo = memo if memo else {(len(graph)-1, len(graph[0])-1): graph[-1][-1]}
    # Return max if already in memo
    if position in memo:
        return memo[position]
    
    current_weight = graph[position[0]][position[1]]
    if position[0]+1 < len(graph):
        down_max = max_path_sum(graph, (position[0]+1, position[1]), memo)
    else:
        down_max = 0
    
    if position[1] +1 < len(graph[0]):
        right_max = max_path_sum(graph, (position[0], position[1]+1), memo)
    else:
        right_max = 0
        
    total_wight = current_weight + max(down_max,right_max)
    memo[position] = total_wight
    print("Memo: ", memo)

    return total_wight
    

g = [[1,2,8], [5,1,3]]
print(max_path_sum(g, (0,0)))

def non_adjacent_max_sum(ls: list) -> int:
    pass

def min_summing_squares(n, sum) -> int:
    # find the minimimum set of squares from 1 to n that on adding is equal to sum.
    pass