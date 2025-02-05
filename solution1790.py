# https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/description/?envType=daily-question&envId=2025-02-05

# 1790. Check if One String Swap Can Make Strings Equal
# Output: true
# Explanation: For example, swap the first character with the last character of s2 to make "bank"



# s1 = "kelb", s2 = "kelb"
# s1 = "attack", s2 = "defend"

s1 = "bank"
s2 = "kanb"
e=[]
count= 0 

e= []

p = 0

while p <len(s1):
    if s1[p] != s2[p]:
        e.append(p)
        count= count+ 1 
    p = p+1


print(e)

if count==2 and s1[e[0]] == s2[e[1]] and s1[e[1]] == s2[e[0]]:
    print(True)
else:
    print(False)







# for i in range(len(s1)):
#     for q in range(len(s2)):
#         if s1[i] != s2[q]:

#             e.append(s1[i])
#             e.append(s2[q])
            

#             # s1[i] = s2[q]
#             print(s1)
#             break

#             count= count + 1 

# print(e)            


# print(set(e))






