# Floats: Could cause some numerical unexpected results.

x = 0

for i in range(10):
    x += 0.1

print(x == 1)
print(x)

import random
# Integers
def convert_to_binary(number):
    result = ''
    if number < 0:
        result += '-'
        number = abs(number)

    while number > 0:
        result += str(number % 2)
        number = number // 2
    return result
    
print(convert_to_binary(15))
print(convert_to_binary(9))

def convert_binary_to_int(binary):
    result = 0
    for i, char in enumerate(binary[::-1]):
        result += int(char) * 2 ** i

    return result

print(convert_binary_to_int('111'))

# Fractions - TODO

x =0.625
p = 0
while ((2**p)*x)%1 != 0:
    print('Remainder = ' + str((2**p)*x - int((2**p)*x)))
    p += 1
num = int(x*(2**p))
result = ''
if num == 0:
    result = '0'
while num > 0:
    result = str(num%2) + result
    num = num//2
for i in range(p - len(result)):
    result = '0' + result
result = result[0:-p] + '.' + result[-p:]
print("Result: ", result)


# Approximation
def sq_root_newton(x):
    """
        Task: Find a number whose sqaure is close to x
              Initialize with a random number as sq. root
              Test the differnce and update untill the number is reasonable
    """

    sq_root = x / 2
    epsilon = 0.0001
    attempts = 0
    while abs(sq_root ** 2 - x) > epsilon:
        sq_root -= (sq_root ** 2 - x) / (2 * sq_root)
        attempts +=1

    return sq_root, attempts

print(sq_root_newton(5))
print(sq_root_newton(15))
print(sq_root_newton(16))

# (2.236067977915804, 3)
# (3.8729834348980945, 4)
# (4.0000001858445895, 4)


def sq_root_brut_approx(x: float):
    """
        Use a small fixed increment to reach the square root
    """
    guess = 0
    attempt = 0
    increment = 0.0001
    epsilon = 0.001

    while abs(guess ** 2 - x) >  epsilon:
        guess += increment
        attempt += 1

    return guess, attempt

print(sq_root_brut_approx(5))
print(sq_root_brut_approx(15))
print(sq_root_brut_approx(16))

# (2.235900000000294, 22359)
# (3.8729000000037486, 38729)
# (3.9999000000040166, 39999)

def bisection_root(x: (int|float)) -> float:
    epsilon = 0.01

    low = 0
    high = x
    ans = (low + high) / 2.0

    while abs(ans ** 2 - x) > epsilon:
        if ans ** 2 > x:
            high = ans
        else:
            low = ans

        ans = (low + high) / 2.0
    return ans
print("Bisection Root: ")
print(bisection_root(25))
print(bisection_root(10))
print(bisection_root(123))
# Bisection Search

def binary_search(ls: list, num: int) -> bool:
    if len(ls) == 0:
        return False
    
    mid_ind = len(ls) // 2

    if ls[mid_ind] == num:
        return True
    elif ls[mid_ind] > num:
        return binary_search(ls[:mid_ind], num)
    else:
        return binary_search(ls[mid_ind+1:], num)
    
print(binary_search([1,2,3,4,5], 3))
print(binary_search([1,2,3,4,5], 3.5))


def is_triangular(n):
    """ n is an integer > 0
    Return True if n is triangular, i.e. equals a summation of natural numbers
    """
    total = 0
    for i in range(n):
        total += i
        if total == n:
            return True
    return False

print(is_triangular(3))
print(is_triangular(4))
print(is_triangular(5))
print(is_triangular(6))


# Function as a parameter (Is the code good??)
class Calculator:
    @staticmethod
    def calc(op, x, y):
        if Calculator.validate(x) and Calculator.validate(y):
            return op(x, y)
    
    @staticmethod
    def validate(x):
        if not isinstance(x, (int | float)):
            return False
        return True
         
def add (a, b):
    return a + b

def div (a, b):
    if b != 0:
        return a / b


c = Calculator()
print(c.calc(lambda x, y: x + y, 30, 4))

# Variable number of arguments

def mean(*args):
    total = 0

    for item in args:
        total += item

    return total / len(args)

print(mean(1,2,3,4))

# Lambda functions

is_even = lambda r: r % 2 == 0

print(is_even(3))
print(is_even(30))

def do_twice(n, fn):
    return fn(fn(n))

print(do_twice(5, lambda x : x ** 2))