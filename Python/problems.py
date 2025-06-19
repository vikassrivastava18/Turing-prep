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
encoded_string("13[a]10[bc]")

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


