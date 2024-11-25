
# https://leetcode.com/problems/word-pattern/description/?envType=problem-list-v2&envId=string&difficulty=EASY

# 290. Word Pattern

# Input: pattern = "abba", s = "dog cat cat dog"
# Output: true



# Input: pattern = "aaaa", s = "dog cat cat dog"
# Output: false


# pattern = "abba"
# s = "dog cat cat dog"

pattern = "aaaa" 
s = "dog cat cat dog"


#working logic: we have to check word in pattern and pattern to word is same mapped or not 




words= s.split(" ")

p_to_s= {}
s_to_p= {}

check= True

if len(pattern)!= len(words):   #if len is not same it is false 
    print(False)

else:
    for c, w in zip(pattern, words):
        if c in p_to_s and p_to_s[c]!=w:  #checking if a exist in dict and value of a mapped with dog if not false 
            check =False
            break
        if w in s_to_p and s_to_p[w]!=c: #same if dog exist in dict and dog mapped with a  
            check= False
            break

        p_to_s[c]=w  # making dict 
        s_to_p[w]=c

print(check)

