"""Move all zeros to the end
Given a list of integers, move all zeros to the end while maintaining the relative order of non-zero elements.
Example 1:
Input: [0, 1, 0, 3, 12]
Output: [1, 3, 12, 0, 0]"""
def move_zero(nums):
  l=[]
  for n in nums:
    if n!=0:
      l.append(n)
  for n in nums:
    if n==0:
      l.append(0)
  return l
  #OR
  def move(nums):
    index = 0

    for n in nums:
        if n != 0:
            nums[index] = n
            index += 1

    while index < len(nums):
        nums[index] = 0
        index += 1

    return nums

nums = [0, 1, 0, 3, 12]
print(move(nums))
