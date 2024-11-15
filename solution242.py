# 242. Valid Anagram
# Given two strings s and t, return true if t is an anagram  of s, and false otherwise.



# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true

# Example 2:
# Input: s = "rat", t = "car"
# Output: false


#logic: check the distinct value in both and  the length should be same 


s = "rat"
t = "car"


# if set(s)==set(t) and len(s) == len(t):
#     print(True)

# else:
#     print(False)

# this above logic is not working in the case of   s= "aacc", t ="ccac"


#2nd logic: sort them and see if the are same or not 


if sorted(s) == sorted(t):
    print(True)

else:
    print(False)