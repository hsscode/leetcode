# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/?envType=problem-list-v2&envId=array&difficulty=EASY

# Remove Duplicates from Sorted Array


nums = [0,0,1,1,1,2,2,3,3,4]

# Output: [1,2]
# logic:  we have to remove duplicate without using extra space , so we compare 2 numbers and move forward
# coz they are in ascending  


l=1  # Start the  pointer at index 1

for r in range(1,len(nums)):   #pointer starts from index 1
    if nums[r] != nums[r-1]:  # Compare current number with the previous one
        nums[l]=nums[r]
        l=l+1   # Move the slow pointer

print(nums)


