# https://leetcode.com/problems/reverse-words-in-a-string-iii/description/?envType=problem-list-v2&envId=string&difficulty=EASY
# # 557. Reverse Words in a String III


# Example 1:
# Input: s = "Let's take LeetCode contest"
# Output: "s'teL ekat edoCteeL tsetnoc"

# Example 2:
# Input: s = "Mr Ding"
# Output: "rM gniD"



# Output: "s'teL ekat edoCteeL tsetnoc"

s = "Let's take LeetCode contest"

ss= s.split(" ")

print(ss)


e=[]

for i in range(len(ss)): 
    e.append(ss[i][::-1])

print(" ".join(e))




