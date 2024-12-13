# # https://leetcode.com/problems/thousand-separator/description/?envType=problem-list-v2&envId=string&difficulty=EASY

# # 1556. Thousand Separator


# # Example 1:
# # Input: n = 987
# # Output: "987"

# # Example 2:
# # Input: n = 1234
# # Output: "1.234"

# # n=123456789

# # if n <1000:
# #     print(str(n))
# # else:
# #     print(str((n/1000)/1000))

# # this is working till we get  123456789>>> "123.456.789"



# a=123456789
a=3760


b= str(a)

#reverse the string 
reveresed_string= b[::-1]

#now i have to make the chunks of 3 

e= []

for i in range(0,len(reveresed_string),3):
    z= reveresed_string[i:i+3]

    e.append(z)

print(e)

ans= []

for i in reversed(range(len(e))):
    e[i]= e[i][::-1] 
    ans.append(e[i])


print(ans)

print(".".join(ans))

