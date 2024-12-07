#https://leetcode.com/problems/palindrome-number/submissions/1472505127/?envType=study-plan-v2&envId=top-interview-150

# Palindrome Number

# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.

# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.



x=121 
xx= str(x)

if xx== xx[::-1]:
    print(True)
else:
    print(False)
