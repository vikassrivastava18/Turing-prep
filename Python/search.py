import random
import time
# Problem: Binary "search"
def guess_with_binary(n: int) -> tuple[int, int]:
    """
    Params:  A number to guess
    Returns: The guessed number, number of attempts
    """
    start_time = time.time()

    num = random.randint(0, n)
    print("Number to guess: ", num)

    start, end = 0, n
    guess = (start + end) // 2
    count = 0
    print(f"Guess: {guess}, Count: {count}")

    while not guess == num:
        if num > guess:
            start = guess
        else:
            end = guess
        guess = (start + end) // 2
        count += 1
        print(f"Guess: {guess}, Count: {count}")

    end_time = time.time()
    print("Total time: ", end_time - start_time)
    return num, count

print(guess_with_binary(100000000000000))


def check_brackets(chars: str) -> bool:
    """
    Parameters: A string of characters
    Returns: True if all the brackets are closed in expected order
    Plan: Create a bucket for open brackets.
          When a new closed bracket is encountered match with last bracket in bucket.
    """
    bucket = []
    open_brackets = ["{", "[", "("]
    closed_brackets = ["}", "]", ")"]

    for char in chars:
        if char in open_brackets:
            bucket.append(char)
        elif char in closed_brackets:
            if len(bucket) == 0:
                return False

            last_open = bucket[-1]
            index = open_brackets.index(last_open)

            if not closed_brackets.index(char) == index:
                return False
            else:
                bucket = bucket[:-1]

    return len(bucket) == 0

print(check_brackets("{hello[])}"))
print(check_brackets("{hello[]}"))
print(check_brackets("{(hello[])}]"))
print(check_brackets("{[({[()]})]}"))

def max_sum_subarray(l: list[int|float], k: int) -> int:
    """
    Parameters: l -> list of numbers
                k -> size of subarray
    Returns:    maximum possible sum for subarray of size k
    """
    # Initialization
    max_sum = sum(l[:k])

    for i in range(1, len(l)-k+1):
        new_sum = sum(l[i:i+k])
        max_sum = max(new_sum, max_sum)
    return max_sum

rand_list = [random.randint(1,1000) for i in range(100000000)]

import time, random

start_time = time.time()

# rand_list = [random.randint(1,1000) for i in range(100000000)]
max_sum_subarray(rand_list, 5)

end_time = time.time()

print("Total time: ", end_time - start_time)

def max_subarray_optimal(l: list, k: int) -> int:
    """
    Parameters: l -> list of numbers
                k -> size of subarray
    Returns the maximum possible sum for subarray of size k
    """

    if len(l) < k:
        return None  # or raise an error if desired
    # Initialization
    curr_sum = sum(l[:k])
    max_sum = curr_sum

    for i in range(k, len(l)):
        curr_sum += l[i] - l[i - k]  # slide window forward
        max_sum = max(max_sum, curr_sum)

    return max_sum

import time, random
start_time = time.time()

# rand_list = [random.randint(1,1000) for i in range(100000000)]
max_subarray_optimal(rand_list, 5)

end_time = time.time()

print("Total time: ", end_time - start_time)

def longest_unique_substring_length(s):
    seen = set()
    left = 0

    max_length = 0

    for right in range(len(s)):
        # If character is already in the current window, shrink from the left
        while s[right] in seen:
            seen.remove(s[left])
            left += 1

        seen.add(s[right])
        max_length = max(max_length, right - left + 1)

    return max_length

print(longest_unique_substring_length("abcadcbb"))


def two_sum(l, s):
    """
        Return a pair of indexes of elements in list l that sum to s
        Sliding windows concept used,
        list is sorted
    """
    left = 0
    right = len(l) - 1

    while left < right:
        if l[left] + l[right] == s:
            return (left, right)

        elif l[left] + l[right] < s:
            left += 1

        else:
            right -= 1

    return None

numbers = sorted([random.randint(1,100000) for i in range(100000)])

target = random.randint(0,10000)
print("Target: ", target)
two_sum(numbers, target)

def three_sum(l: list, s:int=0) -> list:
    """
        Returns a triplet whose sum = s
        Using sliding windows technique
    """
    result = []
    l.sort()

    for third in range(0, len(l)-2):
        left = third + 1
        right = len(l) - 1

        while left < right:
            if l[third] + l[right] + l[left] == s:
                result.append([l[third], l[left], l[right]])
                left += 1
                right -= 1

            elif l[third] + l[right] + l[left] < s:
                left += 1
            else:
                right -=1

    return result

import random

for i in range(5):
    numbers = [random.randint(1,10) for i in range(10)]
    print("Numbers: ", numbers)
    target = random.randint(0,15)
    print("Target: ", target)

    result = three_sum(numbers, target)
    print("Result: ", result)
    print("-----------------------")

