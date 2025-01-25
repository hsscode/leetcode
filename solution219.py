# 219. Contains Duplicate II
# https://leetcode.com/problems/contains-duplicate-ii/description/?envType=study-plan-v2&envId=top-interview-150


# Example 1:
# Input: nums = [1,2,3,1], k = 3
# Output: true

# Example 2:
# Input: nums = [1,0,1,1], k = 1
# Output: true

# Example 3:
# Input: nums = [1,2,3,1,2,3], k = 2
# Output: false



# Logic:

# I have to check if delta of indices is less then or equal to k.
# These indices are which are same in the array.





# nums = [1,2,3,1,2,3] 
# k = 2

# nums = [1,2,3,1] 
# k = 3

# nums =[1]
# k =1


# for i in range(len(nums)):
#     for q in range(len(nums)):
#         if (i==q):
#             continue
#         if nums[i] == nums[q] and abs(q-i)<= k:
#             print(True)
# else:
#     print(False) 



# nums = [1]
# k=1

# s=0

# for i in range(len(nums)):
#     for q in range(len(nums)):
#         if nums[i] == nums[q]:
#             s=q-i
# print(abs(s))

# if abs(s)<=k and len(nums)>1:
#     print(True)
# else:
#     print(False)




nums = [1,2,3,1]
k = 3
# Output: true



e = {}


for i in range(len(nums)):

    if nums[i] in e:
        if abs(e[nums[i]] - i) <= k:
            print(True)
            break
    else:
        e[nums[i]] = i

else:
    print(False)




















# last_seen= {}


# for i in range(len(nums)):
#     if nums[i] in last_seen:
#         if i - last_seen[nums[i]] <= k:
#             print(True)
#             break
#     last_seen[nums[i]]=i 

# else:
#     print(False)


