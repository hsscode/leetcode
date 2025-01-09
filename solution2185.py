# https://leetcode.com/problems/counting-words-with-a-given-prefix/description/
# # 2185. Counting Words With a Given Prefix


# Input: words = ["pay","attention","practice","attend"], pref = "at"
# Output: 2
# Explanation: The 2 strings that contain "at" as a prefix are: "attention" and "attend"


# Input: words = ["leetcode","win","loops","success"], pref = "code"
# Output: 0
# Explanation: There are no strings that contain "code" as a prefix.



# words = ["pay","attention","practice","attend"]
# pref = "at"


words = ["leetcode","win","loops","success"] 
pref = "code"




count=0

for i in words: 
    if i.startswith(pref):
        count= count + 1


print(count)