# https://leetcode.com/problems/remove-element/description/?envType=problem-list-v2&envId=array&difficulty=EASY

# 27. Remove Element

# ex 1:
# Input: nums = [3,2,2,3], val = 3
# Output: 2, nums = [2,2,_,_]


# Example 2:
# Input: nums = [0,1,2,2,3,0,4,2], val = 2
# Output: 5, nums = [0,1,4,0,3,_,_,_]


# nums = [3,2,2,3]
# val = 3

nums = [0,1,2,2,3,0,4,2]
val = 2


# logic: remove element, to remove the element ,,, if match then i can use drop 

l= 1

for i in range(len(nums)-1):
    if nums[i]!=val:
        nums[i]=nums[l]
        l=l+1

print(l)