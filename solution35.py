# 35. Search Insert Position

# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
# You must write an algorithm with O(log n) runtime complexity.

# Input: nums = [1,3,5,6], target = 5
# Output: 2

# Input: nums = [1,3,5,6], target = 2
# Output: 1

# Input: nums = [1,3,5,6], target = 7
# Output: 4


# You must write an algorithm with O(log n) runtime complexity.

# nums = [1,3,5,6]
# target = 5
# Output: 2


# nums = [1,3,5,6] 
# target = 2
# # Output: 1


# nums = [1,3,5,6]
# target = 7
# Output: 4


# logic: return index if value is in list or return index if not exit according to the fitment (ascending)---

nums = [1,3,5,6] 
target = 2
# Output: 1


for i in nums:   # if we find the target into the list 
    if i == target:
        print(nums.index(i),'1st loop')
        break

    elif target not in nums and i > target: 
        print(nums.index(i),'2nd loop')
        break

# here for last condition where target is greater then all element and not exist , exist loop and print len
# i was getting stucked here

else:
    print(len(nums), '3rd loop')






