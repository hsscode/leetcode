# 796. Rotate String

# https://leetcode.com/problems/rotate-string/description/?envType=problem-list-v2&envId=string&difficulty=EASY




# Given two strings s and goal, return true if and only if s can become goal after
# some number of shifts on s.
# A shift on s consists of moving the leftmost character of s to the rightmost position.
# For example, if s = "abcde", then it will be "bcdea" after one shift.



# Example 1:
# Input: s = "abcde", goal = "cdeab"
# Output: true

# Example 2:
# Input: s = "abcde", goal = "abced"
# Output: false


##this logic is gonna work only for 1 char , not for more then 1 char

# s = "abcde"
# goal = "cdeab"

# l1=len(s)
# last_word= s[l1-1:l1]
# first_word= s[0]

# goall= s[1:len(s)] + first_word

# if goall == goal:
#     print(True)
# else:
#     print(False)



# logic: check first char then 2 char then 3 char , we to ittirate it untill it match

# "abcde"
# "bcdea"
# "cdeab"


# s = "abcde"
# goal = "cdeab"


s = "abcde" 
goal = "abced"


l1=len(s)
last_word= s[l1-1:l1]


for i in range(l1):
    goall= s[1:len(s)] + s[0]
    if goall == goal:
        print(True, goall)
        break
    else:
        s = goall

else:
    print(False)


