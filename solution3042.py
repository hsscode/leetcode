# https://leetcode.com/problems/count-prefix-and-suffix-pairs-i/description/

# 3042. Count Prefix and Suffix Pairs I


# isPrefixAndSuffix(str1, str2) returns true if str1 is both a 
# prefix and a suffix of str2, and false otherwise.

# For example, isPrefixAndSuffix("aba", "ababa") is true because "aba" is a prefix of "ababa" and also a suffix, but isPrefixAndSuffix("abc", "abcd") is false.


# Input: words = ["a","aba","ababa","aa"]
# Output: 4


# Input: words = ["pa","papa","ma","mama"]
# Output: 2


# words = ["a","aba","ababa","aa"]


# logic= i+1,len(words)     here we are using to handle index out of range 


words = ["abab","ab"]

count=0

for i in range(len(words)):
    for q in range(i+1,len(words)):

        ww= words[i]
        dd= words[q]

        if i !=q and  dd.startswith(ww) is True and  dd.endswith(ww) is True:
            count= count + 1
    
        
print(count)








