"""Find the missing number
You are given a list containing numbers from 1 to N, but one number is missing.

Find the missing number.

Example 1:
Input: [1, 2, 3, 5, 6]
Output: 4"""
def miss_num(nums):
    n = len(nums) + 1
    s = sum(nums)
    total = n * (n + 1) // 2
    miss = total - s
    return miss

nums = [1, 2, 3, 5, 6]
print(miss_num(nums))
