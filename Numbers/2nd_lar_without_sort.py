"""Find the second-largest distinct number
Example:
Input: [10, 20, 4, 45, 99]
Output: 45"""
def sec_lar(nums):
  n=len(nums)
  for i in range(n):
    for j in range(i,n):
      if nums[j]<nums[i]:
        nums[i],nums[j]=nums[j],nums[i]
  print(nums[-2])
