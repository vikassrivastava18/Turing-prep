# Involves splitting the input into two parts using recursion

# Merge two sorted lists
def merge(l1:list, l2: list) -> list:
    result = []
    i = 0
    j = 0
    while i < len(l1) and j < len(l2):
        if l1[i] < l2[j]:
            result.append(l1[i])
            i += 1
        elif l2[j] < l1[i]:
            result.append(l2[j])
            j += 1
        else:
            result.append(l1[i])
            result.append(l2[j])
            i += 1
            j += 1

    if i < len(l1):
        result += l1[i:]
    elif j < len(l2):
        result += l2[j:]

    return result

# Merge Sort
def merge_sort(l: list) -> list:
    """
    1) Split the list into two halves
    2) Sort each half recursively
    3) Merge the sorted lists
    """
    if len(l) == 0 or len(l) == 1:
        return l

    mid_ind = len(l) // 2
    left, right = l[:mid_ind], l[mid_ind:]
    # print(f"left: {left} right: {right}")
    sorted_left = merge_sort(left)
    sorted_right = merge_sort(right)
    # print(f"sorted_left: {sorted_left}, sorted_right: {sorted_right}")
    return merge(sorted_left, sorted_right)


print(merge([1,3,5], [2,4,6,7,8]))
print(merge([1], [2]))
print(merge_sort([1,3,2]))


# Count inversions between two sorted lists, return sorted list
def merge_and_count(l1: list, l2: list) -> list:
    i, j = 0, 0

    count = 0
    result = []

    while i < len(l1) and j < len(l2):
        if l2[j] < l1[i]: # Case for inversion
            result.append(l2[j])
            count += len(l1) - i
            j += 1
        elif l2[j] > l1[i]: # No inversion
            result.append(l1[i])
            i += 1
        else: # Both item equal
            result.append(l1[i])
            result.append(l2[j])
            i += 1
            j += 1

    result += l1[i:]
    result += l2[j:]

    return count, result


print(merge_and_count([4,5,6], [1,2,3]))
print(merge_and_count([1,2,3], [4,5,6]))
print(merge_and_count([3,4,6], [1,2,5]))
print(merge_and_count([1,2,5], [3,4,6]))


def inversions(l: list[int]) -> int:
    """
    Prameters: integer list
    Returns: total inversions ans sorted list tuple
    Plan: Count the left half and right half inversions, add the split inversions when combining them
    """

    if len(l) == 1 or len(l) == 0:
        return 0, l
    
    mid_ind = len(l) // 2
    left_count, left = inversions(l[:mid_ind])
    right_count, right = inversions(l[mid_ind:])

    split_count, combined = merge_and_count(left, right)
    total_count = split_count + left_count + right_count
    return total_count, combined

print(inversions([1,3,2,4]))
print(inversions([5,4,6,1,2,3]))


import math, random

def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


def closest_num_pairs(l: list[int]) -> tuple[list[int]]:
    """
        Parameters: l -> list of integers
        Task: return the two points closest to each other. 
        Plan: sort the list, in one iteration figure out the closest points by comparing with previous closest.
    """
    l_copy = l[:]
    l_copy.sort()

    min_dist = float('inf')

    for i in range(len(l_copy) - 1):
        d = l_copy[i+1] - l_copy[i]
        if d < min_dist:
            min_dist = d
            closest_pairs = (l_copy[i], l_copy[i+1])

    return (closest_pairs, min_dist)

l = [random.randint(1,2000) for i in range(10)]
print(closest_num_pairs(l))


def count_inversions(arr: list[int]) -> int:

    def merge_and_count(left: list[int], right: list[int]) -> tuple[int, list[int]]:
        i = j = count = 0
        merged = []
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                count += len(left) - i
                j += 1
        merged += left[i:]
        merged += right[j:]
        return count, merged

    def sort_and_count(lst: list[int]) -> int:
        if len(lst) <= 1:
            return 0, lst
        mid = len(lst) // 2
        left_count, left_sorted = sort_and_count(lst[:mid])
        right_count, right_sorted = sort_and_count(lst[mid:])
        split_count, merged = merge_and_count(left_sorted, right_sorted)
        return left_count + right_count + split_count, merged

    count, _ = sort_and_count(arr)
    return count

def inversion_large(file: str) -> int:

    r = []
    with open(file, 'r') as f:
        for i in range(100000):
            line = f.readline()
            r.append(int(line.strip()))
    print("Length of list: ", len(r))
    count = inversions(r)
    return count[0]

# print("My code inversions: ", inversion_large('integer_array.txt'))
# print("GPT code: ", count_inversions(r))


def matrix_multi(a: list, b: list) -> list:
    """
    Task: Should return the multiplication output
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
# n = random.randint(15,20)
# a = [[random.randint(0,10) for _ in range(n)] for _ in range(n)]
# b = [[random.randint(0,10) for _ in range(n)] for _ in range(n)]
# print("Dimension: ", n)
# print(a)
# print(b)
# print(matrix_multi(a, b))

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

print(f"m: {m}, n: {n}, k: {k}")
print(f"a: {a}, b: {b}")
print(matrix_mul_general(a, b))

