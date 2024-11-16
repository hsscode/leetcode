# First Unique Character in a String

# Given a string s, find the first non-repeating character in it and
# return its index. If it does not exist, return -1.

# Input: s = "leetcode"
# Output: 0

# Explanation:The character 'l' at index 0 is the first character that does not occur at any other index.

# Input: s = "loveleetcode"
# Output: 2

# Input: s = "aabb"
# Output: -1

# s = "leetcode"
# s = "aabb"



s = "loveleetcode"

for i in s:
    a= s.replace(i,'',1)
    if i not in a:
        print(s.index(i))
        break
else:
    print(-1)

