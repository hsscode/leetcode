# # https://leetcode.com/problems/delete-characters-to-make-fancy-string/description/?envType=problem-list-v2&envId=string&difficulty=EASY

# # 1957. Delete Characters to Make Fancy String


# #logic1:; fancy mean:  convert whenver we see 3 char together , make it into 2 char 


# # logic: Here we have to find 3 consecutive same char, I tried using count of char in the string,
# #and made dictionary, but   e 4 , l1 , t 1 ,  c 1 , o 1 >>>>>---------- |||





# s = "aaabaaaa"

# count=0

# for i in range(len(s)-1):

#     if s[i] == s[i+1]:
#         count= count + 1 
#         print(s[i], count,"first ifff ", "and  check",i)


#     if count == 2:
#         s=s.replace(s[i],'@',1)
#         print(s,'2nd if, elemnimate',i)
#         count = 0




# print(count, 'final count')
# print(s, "final result")




s= "aaabaaaa"

e= []

for i in range(len(s)):
    if len(e)>=2 and s[i] == e[-1] == e[-2]:
        continue
    else:
       e.append(s[i])

print("".join(e))




