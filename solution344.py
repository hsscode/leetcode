# Reverse String
# Write a function that reverses a string. The input string is given as an array of characters s.

# You must do this by modifying the input array in-place with O(1) extra memory.


# Input: s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]
# Example 2:

# Input: s = ["H","a","n","n","a","h"]
# Output: ["h","a","n","n","a","H"]
 


# Logic : we have to reverse the string can use indexing 


s = ["h","e","l","l","o"]

# print(s[::-1])

# but this is not giving what we are looking reason,, this method ::-1 give a new string or list in a space, we have
#to utilize no space so we have to  use 2 pointer technique 


left = 0
right = len(s)-1


while left<right:
    s[left],s[right]= s[right], s[left]
    left= left +1 
    right= right -1 

print(s)
































# left= 0
# right = len(s)-1
# while left<right:
#     s[left], s[right]= s[right], s[left]
            
#              # Move the left pointer forward
#     left = left + 1
#             # Move the right pointer backward
#     right = right -1

# print(s)

