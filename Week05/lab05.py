# Lab 05: Recursion and Searching
# Student Name: Emir Sadi
# Date: [Enter Today's Date]

# ============================================
# Question 1: Fibonacci
# ============================================

def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)


print("Fibonacci values from 0 to 10:")
for i in range(11):
    print(f"fib({i}) =", fib(i))


# ============================================
# Question 2: FizzBuzz
# ============================================

def fizz_buzz(n):
    result = []

    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))

    return result


print("\nFizzBuzz for n = 15:")
print(fizz_buzz(15))


# ============================================
# Question 3: Binary Search
# ============================================

def binary_search_iterative(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        elif target < nums[mid]:
            right = mid - 1
        else:
            left = mid + 1

    return -1


def binary_search_recursive(nums, target, left, right):
    if left > right:
        return -1

    mid = (left + right) // 2

    if nums[mid] == target:
        return mid
    elif target < nums[mid]:
        return binary_search_recursive(nums, target, left, mid - 1)
    else:
        return binary_search_recursive(nums, target, mid + 1, right)


nums = [-1, 0, 3, 5, 9, 12]

print("\nBinary Search Iterative:")
print("Target 9:", binary_search_iterative(nums, 9))
print("Target 2:", binary_search_iterative(nums, 2))

print("\nBinary Search Recursive:")
print("Target 9:", binary_search_recursive(nums, 9, 0, len(nums) - 1))
print("Target 2:", binary_search_recursive(nums, 2, 0, len(nums) - 1))
