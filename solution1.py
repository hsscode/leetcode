# https://leetcode.com/problems/two-sum/description/?envType=problem-list-v2&envId=array&difficulty=EASY

# Two Sum

# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.


# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].


# Input: nums = [3,2,4], target = 6
# Output: [1,2]


# Input: nums = [3,3], target = 6
# Output: [0,1]




# nums = [2,7,11,15]
# target = 9

# nums = [3,2,4]
# target = 6
# Output: [1,2]


# nums = [3,3] 
# target = 6
# Output: [0,1]




# logic: pick 1 number and add with all iteration and  if match  then stop 

nums = [3,2,4] 
target = 6


e= []

for i in range(len(nums)):
    for j in range(i + 1, len(nums)):  # j > i to avoid duplicates
        if nums[i] + nums[j] == target:
            e.append(i)
            e.append(j)
            break  # Stop after finding the first valid pair

print(e)