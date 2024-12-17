# https://leetcode.com/problems/single-number/description/?envType=study-plan-v2&envId=top-interview-150

# 136. Single Number--------------


# Example 1:
# Input: nums = [2,2,1]
# Output: 1

# Example 2:
# Input: nums = [4,1,2,1,2]
# Output: 4

# Example 3:
# Input: nums = [1]
# Output: 1


nums= [4,1,2,1,2]


for i in range(len(nums)):
   if  nums.count(nums[i])== 1:
      print(nums[i])
      break



    


    
