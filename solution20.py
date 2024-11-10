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




s = "()[]{}"


brackets = {'{': '}', '(': ')', '[': ']'}
        
stack = []
        
for char in s:
    if char in brackets:
        stack.append(char)
    elif not stack or brackets[stack.pop()] != char:
        print(False)
            
print(not stack)

