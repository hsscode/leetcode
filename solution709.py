# https://leetcode.com/problems/to-lower-case/description/?envType=problem-list-v2&envId=string

# 709. To Lower Case

# Given a string s, return the string after replacing every uppercase letter with the same lowercase letter...

# s = "Hello"

# s = "here"

s = "LOVELY"


# Hello to hello


e= []

for i in s :
    if i == i.upper():
        e.append(i.lower())
    else:
        e.append(i)


print("".join(e))

