# # https://leetcode.com/problems/reverse-string-ii/description/?envType=problem-list-v2&envId=string&difficulty=EASY

# # 541. Reverse String II

# # Example 1:
# # Input: s = "abcdefg", k = 2
# # Output: "bacdfeg"

# # Example 2:
# # Input: s = "abcd", k = 2
# # Output: "bacd"


# # s = "abcdefg"
# # k=2

# s= "abcd"
# k=2


# e1= []
# e2= []



# for i in range(0,len(s)):
#     if i <k:
#         e1.append(s[i])
#     else:
#         e2.append(s[i])

# ans_l= e1[::-1] + e2

# print("".join(ans_l))








# #this p[roblen i have solved when k value has to do change in the begininng of the strin g 

# #now ques is , we have to change in every position of k and 2k....

s = "abcdefg"
k=2

e=[]

# this is for the 2nd case of the question 

if k>len(s):
    s[::-1]


s= list(s)  # making a list of s 

for i in range(0, len(s), 2*k):
    s[i:i+k]= (s[i:i+k])[::-1]

print("".join(s))


