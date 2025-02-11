# https://leetcode.com/problems/clear-digits/?envType=daily-question&envId=2025-02-10

# 3174. Clear Digits


# Input: s = "abc"
# Output: "abc"



# Output: ""

# Explanation:

# First, we apply the operation on s[2], and s becomes "c4".
# Then we apply the operation on s[1], and s becomes "".


s = "cb34"
ss = list(s)

i = 0

while i <len(ss):

    if  ss[i].isdigit():
        ss.pop(i)
        if i>0:
            ss.pop(i-1)
            i= i-1 
    else:
        i=i+1 

print("".join(ss))





# s = "cb34"
# ss = list(s)

# i = len(ss) - 1  # Start from the last index
# while i > 0:  # Stop at index 1 (since we always remove i and i-1)
#     if ss[i].isdigit():
#         ss.pop(i)   # Remove digit
#         ss.pop(i-1) # Remove character to the left
#         i -= 1  # Move index back since we removed two elements
#     i -= 1  # Move to the previous element

# print("".join(ss))  # Output: ""




