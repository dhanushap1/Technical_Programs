"""Find the longest consecutive sequence
Given an unsorted list of integers, find the length of the longest consecutive sequence.
Example:
Input: [100, 4, 200, 1, 3, 2]
Output: 4
Explanation:
The longest consecutive sequence is:
[1, 2, 3, 4]
Its length is 4."""
def cons(nums):
    max_count = 0

    for i in range(len(nums)):
        count = 1
        next_num = nums[i] + 1

        while next_num in nums:
            count += 1
            if count > max_count:
                max_count = count
            next_num += 1

    return max_count
