# https://leetcode.com/problems/most-common-word/description/?envType=problem-list-v2&envId=string&difficulty=EASY

# 819. Most Common Word

# Example 1:

# Input: paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.", banned = ["hit"]
# Output: "ball"

# Explanation: 
# "hit" occurs 3 times, but it is a banned word.
# "ball" occurs twice (and no other word does), so it is the most frequent non-banned word in the paragraph. 
# Note that words in the paragraph are not case sensitive,
# that punctuation is ignored (even if adjacent to words, such as "ball,"), 
# and that "hit" isn't the answer even though it occurs more because it is banned.

# Example 2:
# Input: paragraph = "a.", banned = []
# Output: "a"




paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]



paragraph = paragraph.lower()

punct=  "!?',;."

for p in punct:
    paragraph= paragraph.replace(p,"")


words= paragraph.split()

word_count={}


for word in words:
    if word not in banned:
        if word in word_count:
            word_count[word] +=  1
        else:
            word_count[word]= 1

print(word_count)


max_word= ""
max_count= 0


for word, count in word_count.items():
    if count> max_count:
        max_count= count
        max_word= word

print(max_word)