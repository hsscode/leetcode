# 434. Number of Segments in a String

# Given a string s, return the number of segments in the string.
# A segment is defined to be a contiguous sequence of non-space characters.

# Example 1:
# Input: s = "Hello, my name is John"
# Output: 5
# Explanation: The five segments are ["Hello,", "my", "name", "is", "John"]

# Example 2:
# Input: s = "Hello"
# Output: 1



spcl_char= "!@#$%^&*()_+-=',.:"

s = "Hello, my name is John"


e=[]
ss=''

for i in spcl_char:
    if i in s:

        ss=s.replace(i,'')


split_word= ss.split(" ")

print(len(split_word))




# 2nd method 



s = "Hello, my name is John"

print(len(s.split()))












# print(s.replace(spcl_char,''))



# ss= s.replace(spcl_char,"")

# print(ss)
# l= ss.split(" ")
# print(l)



