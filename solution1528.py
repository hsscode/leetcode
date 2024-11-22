# 1528. Shuffle String

# https://leetcode.com/problems/shuffle-string/description/?envType=problem-list-v2&envId=string&difficulty=EASY



# Input: s = "codeleet", indices = [4,5,6,7,0,2,1,3]
# Output: "leetcode"
# Explanation: As shown, "codeleet" becomes "leetcode" after shuffling.


# Input: s = "abc", indices = [0,1,2]
# Output: "abc"
# Explanation: After shuffling, each character remains in its position.




# logic:  i have to map s char with indexes , eg. c4, 05,, this dict i have to create and then sort on value asc
# >>>>> map, enumerate , zip   <<<<<


# s = "abc"
# indices = [0,1,2]

# 1st method 

# s = "codeleet"


# indices = [4,5,6,7,0,2,1,3]

# s2=''
# combined= zip(s,indices)
# combined2= list(combined)


# # def x(n):
# #     return n[1] 

# ans=sorted(combined2, key= lambda x : x[1])   # i can use lambda here for the function 

# for i in ans:
#     s2= s2+ i[0]

# print(s2)






# 2nd method 


s = "codeleet"
indices = [4,5,6,7,0,2,1,3]



z=''


for i in range(len(indices)):
    a= indices.index(i)

    z= z+ s[a]

print(z)

