# Length of Last Word

# Given a string s consisting of words and spaces, return the length of the last word in the string.

# A word is a maximal substring consisting of non-space characters only.



s = "   fly me   to   the moon  "


# Output: 5
# Explanation: The last word is "World" with length 5.


ss= s.strip()
a= ss.split(' ')
print(a)

b= len(a[-1])
print(b)
