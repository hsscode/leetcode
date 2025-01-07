# https://leetcode.com/problems/string-matching-in-an-array/description/?envType=daily-question&envId=2025-01-07

# 1408. String Matching in an Array

# Given an array of string words, return all strings in words that is a substring of another word. 
# You can return the answer in any order.




# Example 1:
# Input: words = ["mass","as","hero","superhero"]
# Output: ["as","hero"]
# Explanation: "as" is substring of "mass" and "hero" is substring of "superhero".
# ["hero","as"] is also a valid answer.


# Example 2:
# Input: words = ["leetcode","et","code"]
# Output: ["et","code"]
# Explanation: "et", "code" are substring of "leetcode".

# Example 3:
# Input: words = ["blue","green","bu"]
# Output: []
# Explanation: No string of words is substring of another string.


# logic:  pick 1 word, then check it in others string 



# words = ["mass","as","hero","superhero"] 
# words = ["leetcode","et","code"]

words = ["leetcoder","leetcode","od","hamlet","am"]



e= []

for i in range(len(words)):
    for q in range(len(words)):
        if words[i] in words[q] and i!=q:
            e.append(words[i])


ee= set(e)

print(ee)
