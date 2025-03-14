# 2529. Maximum Count of Positive Integer and Negative Integer

# Example 1:
# Input: nums = [-2,-1,-1,1,2,3]
# Output: 3
# Explanation: There are 3 positive integers and 3 negative integers. The maximum count among them is 3.

# Example 2:
# Input: nums = [-3,-2,-1,0,0,1,2]
# Output: 3
# Explanation: There are 2 positive integers and 3 negative integers. The maximum count among them is 3.

# Example 3:
# Input: nums = [5,20,66,1314]
# Output: 4
# Explanation: There are 4 positive integers and 0 negative integers. The maximum count among them is 4.


# nums = [-2,-1,-1,1,2,3]

nums = [-3,-2,-1,0,0,1,2]


pos= []
neg= []

for i in nums:
    if i <0:
        neg.append(i)
    if i>0:
        pos.append(i)

print(max(len(pos),len(neg)))

