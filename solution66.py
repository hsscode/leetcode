# 66. Plus One---------#####------#####-----#####!!!!!!!-------!!!!!!!!----!!!!!--_!--!_!__!_!__!_!_

# Input: digits = [1,2,3]
# Output: [1,2,4]

# Input: digits = [4,3,2,1]
# Output: [4,3,2,2]

# Input: digits = [9]
# Output: [1,0]


# digits = [1,2,3]
# digits = [4,3,2,1]



# digits = [1,2,3] >  [1,2,3]  this is what we want 
# digits = [9,9,9] >  [1,0,0,0]     this is what we want 

digits = [9,9]
output=[1,0,0]

e=[]
carry= 1
i= 0


#first we have to reverse the array coz append insert in the last 
digits= digits[::-1]

digits = [9, 9]
e = []
carry = 1
i = 0

# Use a while loop for iteration
while carry:  # This carry is used to add 1 and handle cases where 9 becomes 10
    if i < len(digits):
        if digits[i] == 9:
            digits[i] = 0
        else:
            digits[i] = digits[i] + 1
            carry = 0  # Proper assignment here
    else:
        digits.append(1)
        carry = 0  # Proper assignment here as well

    i = i + 1

# Reverse the array back to its original order
print(digits[::-1])

















# digits= digits[::-1]

# while one ==1:
#     if i < len(digits):
#         if digits[i]==9:
#             digits[i]=0
#         else:
#             digits[i]= digits[i]+ 1 

#             one=0
#     else:
#         digits.append(1)
#         one= 0
#     i = i + 1 

# print(digits[::-1])









