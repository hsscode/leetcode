# 392. Is Subsequence

# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
# A subsequence of a string is a new string that is formed from the original string by 
# deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. 
# (i.e., "ace" is a subsequence of "abcde" while "aec" is not).


# Example 1:
# Input: s = "abc", t = "ahbgdc"
# Output: true

# Example 2:
# Input: s = "axc", t = "ahbgdc"
# Output: false
 

#logic ,, we will first check if all char in s exist in t,, then index,, index should be in asc order. 
# eg. 0 3 5 and also abc exist hence true,  

# s = "abc"
# t = "ahbgdc"



# s = "aaaaaa"
# t = "bbaaaa"



# s = "ab"
# t = "baab"


# e=[]

# check= True


# for i in range(len(s)) :
#     if s[i] not in t:
#         check=False
#         break        
#     else:
#         e.append(t.index(s[i])) 
#         t=t.replace(s[i],'',1)     # this is for handling cases like aaaaaa and cbaaaa, index issue

    
#     if sorted(e)==e and len(e)==len(s) or s in t:  #checking here if the order of string same, len same and if string of s exist in t
#         check=True
#     else:
#         check= False


# print(e)
# print(sorted(e))
# print(check)

# 2nd solution -- two pointer technique 


s = "abc"
t = "ahbgdc"


i= 0 
j= 0 

e= []

while i < len(s) and j < len(t):
    if s[i]==t[j]:
        e.append(s[i])
       
        i = i + 1
    j=j+1


print(i==len(s)) 
print(e)