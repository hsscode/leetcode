# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/?envType=problem-list-v2&envId=array&difficulty=EASY

# Remove Duplicates from Sorted Array


nums = [0,0,1,1,1,2,2,3,3,4]

# Output: [1,2]
# logic:  we hqave to remove duplicate 

l=1

for r in range(1,len(nums)-1):
    if nums[r] != nums[r+1]:
        nums[l]=nums[r+1]
        l=l+1

print(nums)



# for r in range(1,len(nums)):
#     if nums[r] != nums[r-1]:
#         nums[l]=nums[r]
#         l=l+1

# print(nums)

