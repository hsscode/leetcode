# https://leetcode.com/problems/isomorphic-strings/description/?envType=problem-list-v2&envId=string&difficulty=EASY

# Isomorphic Strings


# Given two strings s and t, determine if they are isomorphic.
# Two strings s and t are isomorphic if the characters in s can be replaced to get t.
# All occurrences of a character must be replaced with another character while preserving the order of characters.
# No two characters may map to the same character, but a character may map to itself.


# Input: s = "egg", t = "add"
# Output: true

# Input: s = "foo", t = "bar"
# Output: false

# Input: s = "paper", t = "title"
# Output: true




# logic:  we have  to map from s to t , if mapping happen distinctly from s then it is true else false 
# # eg.egg, add  -->>   e > a , g > d   here all mapping happen so it is isophormic 



s = "egg"
t = "add"

e={}

#  doing maping  using  zip and making dictionary len

for i , j in zip(s,t):
    e[i]=j


#we can also use the dict indicing method , both has same result 

# for i in range(len(s)):
#     e[s[i]]=t[i]






#here checking the duplicacy of the mapping, so validating by checking length.
if len(set(e.values()))!= len(e.keys()):
    print(False)

else:    # in else will check if we can make the new string by using the first string value from dict 
    str=''
    for i in s:
        str= str + e[i]

    if str==t:  # if we can make the same string its good to go else false 
        print(True)
    else:
        print(False)