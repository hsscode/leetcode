# https://leetcode.com/problems/climbing-stairs/description/?envType=study-plan-v2&envId=top-interview-150

# Climbing Stairs

# Input: n = 2
# Output: 2

# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
# n = 2


# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step

n=4

# 1,2,1
# 2+1+1
# 1+1+2
# 1+1+1+1
# 2+2

one= 1 
two= 1 

for i in range(n-1):
    temp=one 
    one= one+two
    two = temp

print(one)











