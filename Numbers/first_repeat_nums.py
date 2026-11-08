"""Find the first repeated element
Given a list of numbers, find the first element that appears more than once, considering the original left-to-right order.

Example 1:
Input: [10, 5, 3, 4, 3, 5, 6]
Output: 3"""
def first_repeat(nums):
    l = []
    for n in nums:
        if n not in l:
            l.append(n)
        else:
            return n
    return "No repeated element"
