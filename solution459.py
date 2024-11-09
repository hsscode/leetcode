
# Given a string s, check if it can be constructed by taking a substring of it 
# and appending multiple copies of the substring together.

 

# Example 1:

# Input: s = "abab"
# Output: true
# Explanation: It is the substring "ab" twice.
# Example 2:

# Input: s = "aba"
# Output: false
# Example 3:

# Input: s = "abcabcabcabc"
# Output: true
# Explanation: It is the substring "abc" four times or the substring "abcabc" twice.


# logic 1: 
# Here i can count characters and if and check if the count is even then it can be repeated substring.
#this logic get failed eg. ababab > a3 b3 
# logic 2: now just count of char if it is same for all char and > 1 then we can say>> 
#this also got failed 

#logic 3 ,,, concatinate the original string with itself and then check after removing 1st and last char from the concatinate 
#string that orginal string exist into it or not
#this worked 


# s = "abab"
# a=2
# b=2

# ans ab 

# abcabc
# a2 b2 c2 
# abc 

# 3rd solution:

s= 'abcabc'


doubled_s = s + s
print(doubled_s)

print(doubled_s[1:-1])

print(s in doubled_s[1:-1])

















# 1st sol:

# s= 'abab'


# for i in s:
#     f=s.index(i)
#     ee.append(f)

# print(ee)


# d= {}

# for i in s:
#     d[i] = s.count(i)

# ans= True

# e=[]

# for key, value  in d.items():
#     e.append(value)

# ##

# if  len(set(e))==1 and e[0]>1:
#     print(True)
# else:
#     print(False)

# #now this case is having fail here ababba



# vall_max= max(e)-1
# print(e,"ddsododo")


# # print(e)

# # using list comprehension 
# print(ee)


# chunk_size= vall_max

# chunks=[]

# for i in range(0,len(ee), chunk_size):
#     chunk = ee[i:i + chunk_size]
#     chunks.append(chunk)

# print("test")
# print(chunks)

# # print(set(ee))

# # if chunks[0]==set(chunks):
# #     print(True)
# # else:
# #     print(False)


# ans2= True

# for i in chunks:
#     if chunks[0]!= i:
#         ans2=False
#         break

# print(ans2)

    




# 2nd solution :-------------------


# s= 'abac'

# e=[]
# d= {}
# e_val=[]
# chunks=[]
# ans= True



# for i in s:
#     f=s.index(i)
#     e.append(f)

# print(e)



# for i in s:
#     d[i] = s.count(i)


# for key, value in d.items():
#     e_val.append(value)




# chunk_size= max(e)+1



# for i in range(0,len(e), chunk_size):
#     chunk = e[i:i + chunk_size]
#     chunks.append(chunk)



# for i in chunks:
#     if chunks[0]!= i:
#         ans=False
#         break


# print(chunk_size)

# print(chunks)


# print(ans)




