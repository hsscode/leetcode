# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.


# Example 1:

# Input: s = "()"

# Output: true

# Example 2:

# Input: s = "()[]{}"

# Output: true

# Example 3:

# Input: s = "(]"

# Output: false






### Logic :    The logic is to use a stack to track opening brackets and ensure that each closing
#  bracket matches the most recent opening bracket; if any mismatch or unbalanced bracket is found, 
# return False; otherwise, check if the stack is empty at the end to confirm all brackets are properly closed.




s = "(]"


brackets = {'{': '}', '(': ')', '[': ']'}


# print(not stack)    >>>>> not stack(list) mean is it empty or not , if empty then it will show True 
stack=[]




for i in s:
    if i in brackets:
        stack.append(i)
    elif not stack or brackets[stack.pop()] != i:
        print(False)
        break

else:
    print(not stack)


