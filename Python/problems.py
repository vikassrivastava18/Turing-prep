import unittest

# Problem: Check whether a number is a prime.
def is_prime(n: int) -> bool:
    """
    Parameters: integer
    Returns: A string saying whether input is a prime
    Plan: Use Python modulus function to check if the input divides numbers coming before it.
    """
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1): # Trick for optimization
        if n % i == 0:
            return False
    return True


## Test 
class TestIsPrime(unittest.TestCase):
    def test_primes(self):
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(3))
        self.assertTrue(is_prime(5))
        self.assertTrue(is_prime(11))
        self.assertTrue(is_prime(29))
        self.assertTrue(is_prime(97))
        self.assertTrue(is_prime(101))
        self.assertTrue(is_prime(99991))

    def test_non_primes(self):
        self.assertFalse(is_prime(-10))
        self.assertFalse(is_prime(0))
        self.assertFalse(is_prime(1))
        self.assertFalse(is_prime(4))
        self.assertFalse(is_prime(9))
        self.assertFalse(is_prime(15))
        self.assertFalse(is_prime(25))
        self.assertFalse(is_prime(100))
        self.assertFalse(is_prime(99990))

test = TestIsPrime()
test.test_primes()
test.test_primes()


# class TestRemainder(unittest.TestCase):
#     def test_standard_cases(self):
#         self.assertEqual(remainder(10, 3), 1)
#         self.assertEqual(remainder(10, 2), 0)
#         self.assertEqual(remainder(7, 7), 0)

#     def test_zero_cases(self):
#         self.assertEqual(remainder(0, 5), 0)
#         self.assertEqual(remainder(123456, 1), 0)

#     def test_negative_cases(self):
#         self.assertEqual(remainder(-10, 3), 2)    # Python: -10 % 3 == 2
#         self.assertEqual(remainder(10, -3), -2)   # 10 % -3 == -2
#         self.assertEqual(remainder(-10, -3), -1)  # -10 % -3 == -1

#     def test_division_by_zero(self):
#         with self.assertRaises(AssertionError):
#             remainder(5, 0)

# test = TestRemainder()
# test.test_standard_cases()
# test.test_zero_cases()
# test.test_negative_cases()
# test.test_division_by_zero()


# Problem: Find and return the sum of all digits in a string
def sum_digits(s: str) -> int: # str = "10123454"
  assert len(s) != 0, "s is empty"
  total = sum([int(el) for el in s if el])
  return total

# print(sum_digits("12345"))
# print(sum_digits("abcd"))

import random
import time

# Problem: Return True if both words have the same characters
def same_chars(w1: str, w2: str) -> bool:
    """
    Parameters: Two strings
    Returns: True if the two strings have same characters, else False
    Plan: Use concept of Sets for sameness.
    """
    return set(w1) == set(w2)

print(same_chars("abc", "cab"))     # prints True
print(same_chars("abccc", "caaab")) # prints True
print(same_chars("abcd", "cabaa"))  # prints False
print(same_chars("abcabc", "cabz")) # prints False

# Problem: Return the dot product of two tuples
def dot_product(tA: tuple, tB: tuple):
    """
    tA: a tuple of numbers
    tB: a tuple of numbers of the same length as tA
    Assumes tA and tB are the same length.
    Returns a tuple where the:
    * first element is the length of one of the tuples
    * second element is the sum of the pairwise products of tA and tB
    """
    _sum = 0

    for i in range(len(tA)):
        _sum += tA[i] * tB[i]

    return (len(tA), _sum)

# Examples:
tA = (1, 2, 3)
tB = (4, 5, 6)
print(dot_product(tA, tB)) # prints (3,32)


def count_sqrts(nums_list: list[int]) -> int:
    """
    nums_list: a list
    Assumes that nums_list only contains positive numbers and that there are no duplicates.
    Returns how many elements in nums_list are exact squares of elements in the same list, including itself.
    """
    # Your code here
    count = 0

    for item in nums_list:
        if item ** 2 in nums_list:
            count +=1

    return count

# Examples:
print(count_sqrts([3,4,2,1,9,25])) # prints 3


from collections import Counter

# Problem: Check whether two words are anagrams
def is_anagram2(w1: str, w2:str) -> bool:
    print("Count: ",Counter(w1))
    return Counter(w1) == Counter(w2)

def is_anagram3(w1, w2):
    return sorted(w1) == sorted(w2)

print(is_anagram2("aab", "abb"))
# print(is_anagram3("aab", "abb"))


def sum_str_lengths(L):
    """
    L is a non-empty list containing either:
    * string elements or
    * a non-empty sublist of string elements
    Returns the sum of the length of all strings in L and
    lengths of strings in the sublists of L. If L contains an
    element that is not a string or a list, or L's sublists
    contain an element that is not a string, raise a ValueError.
    """
    # Your code here
    result = 0

    for item in L:
        if isinstance(item, str):
            result += len(item)
        elif isinstance(item, list):
            result += sum_str_lengths(item)

        else:
            raise ValueError("Invalid input")
    return result

# Examples:
print(sum_str_lengths(["abcd", "e", "fg", ["abcd", ["e", "fg"]]]))

# Problem: Flatten a list
def flatten(L: list) -> list:
    """
    L: a list
    Returns a copy of L, which is a flattened version of L
    """
    # Your code here
    result = []

    for item in L:
        if isinstance(item, int):
            result.append(item)
        else:
            result += flatten(item)

    return result

# Examples:
L = [1,4,[2, 6],2,[[[3]],2],4,5]
print(flatten(L)) # prints the list [1,4,6,2,3,2,4,5]

import math
class Circle():
    def __init__(self, radius):
        """ Initializes self with radius """
        # your code here
        self.radius = radius

    def get_radius(self):
        """ Returns the radius of self """
        # your code here
        return self.radius

    def set_radius(self, radius):
        """ radius is a number
        Changes the radius of self to radius """
        # your code here
        self.radius = radius

    def get_area(self):
        """ Returns the area of self using pi = 3.14 """
        # your code here
        return math.pi * self.radius ** 2

    def equal(self, c):
        """ c is a Circle object
        Returns True if self and c have the same radius value """
        # your code here
        return self.radius == c.radius

    def bigger(self, c):
        """ c is a Circle object
        Returns self or c, the Circle object with the bigger radius """
        # your code here
        if self.radius > c.radius:
            return self
        return c
    
    def __str__(self):
        """ A Circle's string representation is the radius """
        return f"Circle of radius: {self.radius}"
    
    def __add__(self, c):
        """ c is a Circle object
        Returns a new Circle object whose radius is
        the sum of self and c's radius """
        c = Circle(self.radius + c.radius)
        return c

c1 = Circle(10)
c2 = Circle(5)
print("Circle sum: ", c1 + c2)


class Circle():
    def __init__(self, radius):
        """ Initializes self with radius """
        self.radius = radius

    def get_radius(self):
        """ Returns the radius of self """
        return self.radius

    
    
class Container(object):
    """
    A container object is a list and can store elements of any type
    """
    def __init__(self):
        """
        Initializes an empty list
        """
        self.myList = []

    def size(self):
        """
        Returns the length of the container list
        """
        return len(self.myList)

    def add(self, elem):
        """
        Adds the elem to one end of the container list, keeping the end
        you add to consistent. Does not return anything
        """
        self.myList.append(elem)

class Queue(Container):
    """
    A subclass of Container. Has an additional method to remove elements.
    """
    def remove(self):
        """
        The oldest element in the container list is removed
        Returns the element removed or None if the stack contains no elements
        """
        if len(self.myList) == 0:
            return None

        return self.myList.pop(0)
    
class Stack(Container):
    """
    A subclass of Container. Has an additional method to remove elements.
    """
    def remove(self):
        """
        The newest element in the container list is removed
        Returns the element removed or None if the stack contains no elements
        """
        if len(self.myList) == 0:
            return None

        return self.myList.pop()


def fibonacci(n):
    result = {0: 0, 1: 1}

    if n < 2:
        return result[n]

    for i in range(2, n+1):
        result[i] = result[i-1] + result[i-2]

    return result[n]

for i in range(0,10):
    print(fibonacci(i))

def fibonacci_optimal(n):
    # Optimizes memory space
    if n == 0:
        return 0
    a, b = 0, 1

    for i in range(2, n+1):
        a, b = b, a + b

    return b

for i in range(0,10):
    print(fibonacci_optimal(i))

from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

fibonacci(10)

def fibonacci(n, memo={0:0, 1:1}):
    if n in memo:
        return memo[n]
    memo[n] =  fibonacci(n-1, memo) + fibonacci(n-2, memo)

    return memo[n]

def group_anagram(words):
    result = {}

    for word in words:
        w1_sorted = ''.join(sorted(word))
        if w1_sorted not in result:
            result[w1_sorted] = [word]
        else:
            result[w1_sorted].append(word)

    return list(result.values())

group_anagram(["eat", "tea", "ate", "pan", "nap"])

print(sorted("word"))

def encoded_string(string: str) -> str:
    # "3[a]2[bc]5[a]","13[a]2[bc]5[a]", 2[abc3[de]]
    """
    Solve using index of open and closed ([]) brackets
    TODO - Solve for nested problems
    """
    result = ""
    i = 0
    # Iterate over the characters
    while i < len(string):
        try:
            digit = int(string[i])
            open_b = string.find("[", i)
            closed_b = string.find("]", open_b)
            digit = int(string[i: open_b])

            result += string[open_b+1: closed_b] * digit
            i = closed_b + 1
        except ValueError:
            result += string[i]
            i += 1

    return result
print("Encoded string: ", encoded_string("13[a]10[bc]5[a]"))
print(encoded_string("2[abc3[de]]"))

# Backtractracking
def generate_subsets(nums):
    result = []

    def backtrack(index, path):
        # Add the current subset to the result
        result.append(path[:])  # Copy to avoid mutation

        # Try including each element one by one
        for i in range(index, len(nums)):
            path.append(nums[i])             # Choose
            print("Path: ", path)
            backtrack(i + 1, path)           # Explore
            path.pop()                       # Un-choose (backtrack)

    backtrack(0, [])
    return result

l = [1,2]
generate_subsets(l)

path =[1,2,3]
path.pop()
path


# Valid anagram
def valid_anagram(a: str, b: str):
    return sorted(a) == sorted(b)

print(valid_anagram("aab", "baa"))
print(valid_anagram("papa", "appa"))
print(valid_anagram("aab", "bba"))

def sorted_students():
    students = []
    # With 'with' the file is closed automatically.
    with open("names.csv") as file:
        for line in file:
            name, house = line.rstrip().split(",")
            students.append({"name": name, "house": house})
            
    students = sorted(students, key=lambda student: (student["name"], student["house"]))


def remove_and_sort(Lin: list[int], k: int) -> None:
    """ 
    Task:
        Mutates input list to remove the first k elements in input and
        then sorts the remaining elements in ascending order.
        If you run out of items to remove, Lin is mutated to an empty list.
    Output: None
    """
    # Your code here
    global L
    L = Lin[k:]
    L.sort()

# Examples:
L = [1,6,3,5,7, 0]
k = 2
remove_and_sort(L, k)
print(L)   # prints the list [3, 6]


def check_sorted(ls: list) -> bool:
    """
    Returns True if the list is sorted
    Approach: loop from index 0 to second last element's index.
              Compare consecutive elements, returns Flase if any
              succeeding element is smaller than the preceding one
    """

    for i in range(len(ls)-1):
        if ls[i+1] < ls[i]:
            return False
    
    return True

print(check_sorted([1,2,3,4,5,6]))
print(check_sorted([1,2,3,0,5,6]))


def second_largest(ls: list[int]) -> bool:
    """
    Returns the second largest element of the list
    """
    assert len(ls) > 1, "List must contain at least two elements"

    first, second = -math.inf, -math.inf

    for i in range(len(ls)):
        if ls[i] > first:
            second = first
            first = ls[i]
        elif ls[i] > second:
            second = ls[i]
        
    return second

print(second_largest([1, 3, 2])) # 2
print(second_largest([1, 3, 2, 4, 10, 9, 8, 0])) # 9
print(second_largest([1, 3, 2, 4, 6, 0, 5])) # 5


def wave_array(ls: list) -> list:
    """
    Implement a waveform such that first is greater than second, second 
    is smaller than third and so on.
    """
    for i in range(len(ls) - 1):
        if i % 2 == 0: 
            if ls[i] < ls[i + 1]:
                ls[i], ls[i + 1] = ls[i + 1], ls[i]
        else:
            if ls[i] > ls[i + 1]:
                ls[i], ls[i + 1] = ls[i + 1], ls[i]
    return ls


print(wave_array([1, 2, 3, 4, 5]))
print(wave_array([2, 4, 7, 8, 9, 10]))


def merge_sorted_arrays(l1: list, l2: list) -> list:
    """
        l1, l2 - Lists of numbers
        Should return a sorted list combining the two input 
    """
    result = []

    # Start with the initial position for both the lists
    i, j = 0, 0 
    while i < len(l1) and j < len(l2):
        if l1[i] < l2[j]:
            result.append(l1[i])
            i += 1  
        elif l1[i] > l2[j]:
            result.append(l2[j])
            j += 1
        else:
            result.append(l1[i])
            result.append(l2[j])
            i += 1
            j += 1

    if i < len(l1):
        result.extend(l1[i:])
    if j < len(l2):
        result.extend(l2[j:])

    return result


print(merge_sorted_arrays([1,3,5], [2,4,6]))
print(merge_sorted_arrays([1,3,5], [2,4]))

assert merge_sorted_arrays([1,3,5], [2,4,6]) == [1,2,3,4,5,6], "Merge tests failed"
assert merge_sorted_arrays([], [1,2]) == [1,2], "Merge tests failed"
assert merge_sorted_arrays([1,2], []) == [1,2], "Merge tests failed"

def pairs_with_diff(ls: list, k: int) -> list:
    """
    Returns a list of all pairs
    with difference equal to k
    """

    result = []
    for item in ls:
        check_pair_gr = item + k
        check_pair_sm = item - k
        if check_pair_gr in ls:
            result.append((item, check_pair_gr))
        if check_pair_sm in ls:
            result.append((item, check_pair_sm))

    return result

print(pairs_with_diff([8, 16, 12, 16, 4, 0], 4))
print(pairs_with_diff([1, 4, 1, 4, 5], 3))

# Remove minimum number of elements from lists to make them different
def remove_common_counts(l1: list, l2: list) -> int:
    """
        Remove minimum number of elements from two lists
        To make them completely differnt
    """
    l1_unique = set(l1)
    l2_unique = set(l2)

    common_elements = l1_unique.intersection(l2_unique)

    count = 0
    for common in common_elements:
        if l1.count(common) < l2.count(common):
            count += l1.count(common)
        elif l1.count(common) > l2.count(common):
            count += l2.count(common)
        else:
            count += l1.count(common)

    return count

l1 = [2, 3, 4, 5, 8]
l2 = [1, 2, 3, 4]

print(remove_common_counts(l1, l2))
print(remove_common_counts([1,1,1,2,3,4,5], [1,1,2,6,7]))

def max_distance_between_elem(l: list) -> int:
    """
    The task is to find the maximum distance between two occurrences of an element. 
    If no element has two occurrences, then return 0.
    """
    # Step 1: Find the indexes of all elements
    indexes = {}

    for i, item in enumerate(l):
        indexes[item] = indexes.get(item, []) + [i]

    _max = 0

    for item in indexes:
        if indexes[item][-1] - indexes[item][0] > _max:
            _max = indexes[item][-1] - indexes[item][0]

    return _max

print(max_distance_between_elem([1, 1, 2, 2, 2, 1]))
print(max_distance_between_elem([3, 2, 1, 2, 1, 4, 5, 8, 6, 7, 4, 2]))


def generate_bits(n: int, memo={1:["0", "1"]}) -> list:
    if n in memo:
        return memo[n]
    
    get_one_less = generate_bits(n-1, memo)
    zeoros = ["0" + bit for bit in get_one_less]
    ones = ["1" + bit for bit in get_one_less]
    memo[n] = zeoros + ones
    return zeoros + ones

print(generate_bits(2))
# print(generate_bits(8))

def vaild_brackets(brackets) -> bool:
    open, closed = "(", ")"
    stack = []

    for bracket in brackets:
        if bracket == open:
            stack.append(bracket)
        else:
            if len(stack) == 0:
                return False            
            stack.pop()

    return len(stack) == 0


def generate_brackets(n, memo={1:["(", ")"]}):
    if n in memo:
        return memo[n]
    
    get_one_less = generate_brackets(n-1)
    open = ["(" + bracket for bracket in get_one_less]
    closed = [")" + bracket for bracket in get_one_less]

    memo[n] = open + closed
    return memo[n]

# brackets_8 = generate_brackets(8)
# for bracket in brackets_8:
#     if vaild_brackets(bracket):
#         print(bracket)


def matrix_multi(a: list, b: list) -> list:
    """
    Task: Should return the multiplication output of two matrices a and b.
    Plan: 1) Initialize a n * n Matrix
          2) Loop over both matrices and another nested one.
          3) Use Matrix multiplication formula for assigning result: C(i,j) = Sum(A[i,k] * B[k,j]
    """
    n = len(a)
    result = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += a[i][k] * b[k][j]

    return result

import random

def matrix_mul_general(a: list, b: list) -> list:
    """
    Task: Create a general solution for Matrix multiplication
    Plan: 1) First validate the dimensions of the matrices
          2) Modify the loop ranges
          3) Use the modified formula for calculation: C(i,j) = Sum(A[i,k] * B[k,j]) 
    """
    assert len(b) == len(a[0]), "Invalid dimensions"

    m = len(a)
    k = len(b[0])
    n = len(b)

    result = [[0 for _ in range(k)] for _ in range(m)]

    for i in range(m):
        for j in range(k):
            for l in range(n):
                result[i][j] += a[i][l] * b[l][j]

    return result

m = random.randint(10,15)
n = random.randint(10,12)
k = random.randint(10,25)


a = [[random.randint(0,10) for _ in range(n)] for _ in range(m)]
b = [[random.randint(0,10) for _ in range(k)] for _ in range(n)]

# print(f"m: {m}, n: {n}, k: {k}")
# print(f"a: {a}, b: {b}")
# print(matrix_mul_general(a, b))


def fibonacci(n, memo={1: 1, 2: 1}):
    
    if n in memo:
        return memo[n]
    
    for i in range(3, n+1):
        memo[i] = fibonacci(i-1, memo) + fibonacci(i-2, memo)

    return memo[n]

# t2 = time.time()
# print(fibonacci(1000))
# t1 = time.time()
# print(f"Time taken: {t2-t1}")


def fibonacci_recursive(n, memo={1: 1, 2: 1}):
    if n in memo:
        return memo[n]
    
    fib_l = fibonacci_recursive(n-1, memo)
    fib_r = fibonacci_recursive(n-2, memo)
    memo[n] = fib_l + fib_r
    return memo[n]


# t2 = time.time()
# print(fibonacci_recursive(1000))
# t1 = time.time()
# print(f"Time taken: {t2-t1}")

def tribonacci_recursive(n, memo={0: 0, 1: 1, 2: 1}):
    if n in memo:
        return memo[n]
    
    trib_p = tribonacci_recursive(n-1, memo)
    trib_pp = tribonacci_recursive(n-2, memo)
    trib_ppp = tribonacci_recursive(n-3, memo)

    memo[n] = trib_p + trib_pp + trib_ppp

    return memo[n]

# t2 = time.time()
# print(tribonacci_recursive(1000))
# t1 = time.time()
# print(f"Time taken: {t2-t1}")

def possible_coins_set(coins: list[int], sum: int) -> int:
    memo={0: 1}

    for i in range(1, sum+1):
        count = 0
        left = math.inf
        while left > 0:
            for coin in coins:
                left -= coin

        for coin in coins:
            left = i - coin
            
            while left > 0:
                left -= coin

            if left == 0:
                count += 1
            if left < 0:
                continue
        memo[i] = count
    
    return memo


def possible_coins_set_rec(coins, sum, memo={0: 1}):
    if sum in memo:
        return memo[sum]
    
    memo[sum] = 0
    for coin in coins:
        left = sum - coin
        while left > 0:
            memo[sum] += possible_coins_set_rec(coins, left, memo)
            # left = sum - coin
        
    return memo[sum]





# Find all possible combinations to make the sum
def possible_coins_set_rec(coins=[1, 4, 5], sum=2, memo={1: 1}) -> int:
    pass



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

    return memo[sum]
    
print("Possible count:: ",possible_coins_set([1,4,5], 3))
print("Possible count:: ",possible_coins_set([1,4,5], 4))
print("Possible count:: ",possible_coins_set([1,4,5], 5))


def min_path_sum(graph=[[1,2,8], [5,1,3]], position=(0,0), memo=None) -> int:
    """
        Returns the minimum cost of reaching from the starting position
        Parameters: 
                graph - Weights of cost
                position - Starting postion
                Destiny - (len(graph)-1, len(graph[0])-1)
        Plan: Take the base case as destination, memoize the cost
              Recursively find the cost of preceding connented nodes
    """
    import math
    memo = memo if memo else {(len(graph)-1, len(graph[0])-1): graph[-1][-1]}

    if position in memo:
        return memo[position]
    
    # Find the right and down min distance
    if position[0] < len(graph) - 1:
        down_distance = graph[position[0]][position[1]] + min_path_sum(graph, (position[0]+1, position[1]), memo)
    else:
        down_distance = math.inf

    if position[1] < len(graph[0]) - 1:
        right_distance = graph[position[0]][position[1]] + min_path_sum(graph, (position[0], position[1]+1), memo)
    else:
        right_distance = math.inf

    memo[position] = min(down_distance, right_distance)

    return memo[position]


print(min_path_sum(position=(0,0)))
print(min_path_sum(position=(0,1)))
print(min_path_sum(position=(1,1)))


def min_summing_squares(n=5, sum=25, memo={0: 1}) -> int:
    # find the minimimum set of squares from 1 to n that on adding is equal to sum.
    if sum in memo:
        return memo[sum]
    
    for i in range(1, n+1):
        if sum == i ** 2:
            memo[sum] = 1
        if sum > i ** 2:
            local_min = 1 + min_summing_squares(n, sum - i**2, memo)
            memo[sum] = local_min

    return memo[sum]

print("min",min_summing_squares(n=5, sum=25))
print("min",min_summing_squares(n=5, sum=5))
print("min",min_summing_squares(n=5, sum=4))
print("min",min_summing_squares(n=5, sum=3))
print("min",min_summing_squares(n=5, sum=7))



# Find the smallest COMBINATION of coins to make up the sum
def minimum_coins_set_rec(coins=[1, 4, 5], sum=2, memo={1: 1}):
    if sum in memo:
        return memo[sum]
    
    for coin in coins[::-1]:
        if sum == coin:
            memo[sum] = 1
        elif sum > coin:
            local_min = 1 + minimum_coins_set_rec(coins, sum=sum-coin, memo=memo)
            if sum in memo:
                print("Idea works!!")
                memo[sum] = min(local_min, memo[sum])
            else:
                memo[sum] = local_min
    return memo[sum]
        
print(minimum_coins_set_rec(sum=3))   
print(minimum_coins_set_rec(sum=5))   
print(minimum_coins_set_rec(sum=7))  
print(minimum_coins_set_rec(sum=10))  
print(minimum_coins_set_rec(sum=9))  
print(minimum_coins_set_rec(sum=8))
print(minimum_coins_set_rec(sum=12))
print(minimum_coins_set_rec(sum=13))
print(minimum_coins_set_rec(sum=50))
print(minimum_coins_set_rec(sum=52))
print(minimum_coins_set_rec(sum=53))