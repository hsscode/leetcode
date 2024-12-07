# https://leetcode.com/problems/majority-element/description/?envType=study-plan-v2&envId=top-interview-150
# Majority Element---------------------

# the majority element is the element that appears more than ⌊n / 2⌋ times. 
# Example 1:
# Input: nums = [3,2,3]
# Output: 3


# Example 2:
# Input: nums = [2,2,1,1,1,2,2]
# Output: 2

# nums = [3,2,3]

# nums = [2,2,1,1,1,2,2]

# e={}
# d=[]

# for i in range(len(nums)):
#     x= nums.count(nums[i])
#     e[nums[i]] = nums.count(nums[i])


# for i,k in e.items():
#     d.append(k)

# ans= max(d)

# print(e)
# print(ans)

# for i,k in e.items():
#     if ans== k:    
#         print(i)

# this solution works but gives the error  : Time Limit Exceeded

# now we have to think some short methods 


nums = [2,2,1,1,1,2,2]




e={}
d=[]

s= list(set(nums))   ## found unique elements in the list and made a new list to count them in og list  

for i in range(len(s)):
    e[s[i]] = nums.count(s[i])

ans=max(e.values())


for i,k in e.items():
    if ans== k:    
        print(i)
