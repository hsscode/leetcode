# <!-- https://leetcode.com/problems/longest-nice-substring/description/?envType=problem-list-v2&envId=string -->


# <!-- 1763. Longest Nice Substring -->

# <!-- A string s is nice if, for every letter of the alphabet that s contains, it appears both in 
# uppercase and lowercase. For example, "abABB" is nice because 'A' and 'a' appear, and 'B' and 'b' 
# appear. However, "abA" is not because 'b' appears, but 'B' does not.
# Given a string s, return the longest substring of s that is nice. 
# If there are multiple, return the substring of the earliest occurrence. 
# If there are none, return an empty string. -->


# <!-- Example 1:
# Input: s = "YazaAay"
# Output: "aAa"
# Explanation: "aAa" is a nice string because 'A/a' is the only letter of the alphabet in s, and both 'A' and 'a' appear.
# "aAa" is the longest nice substring.


# Example 2:
# Input: s = "Bb"
# Output: "Bb"

# Explanation: "Bb" is a nice string because both 'B' and 'b' appear. The whole string is a substring.

# Example 3:
# Input: s = "c"
# Output: ""
# Explanation: There are no nice substrings. -->


# logic:    
# 
# nice string > small and capital and initial strings first and ,longest and empty string if not 


# s = "Bb"

# s = "YazaAay"

# uni= set(s)
# e=  []
# e2= []
# e3= []
# e4= ""


# if len(set(s.lower())) == 1: 
#     for i in uni:
#         if (i.lower() and i.upper()) in s:
#             e4 = e4 + i
#     print(e4)


# elif len(s) < 2:
#     print("")


# else:
#     for i in range(len(s)):
#         if s[i].upper() not in  s or s[i].lower() not in s:
#             e=(s.split(s[i]))


#     for i in e:
#         for q in range(len(i)):
#             if i[q].upper() not in  i or i[q].lower() not in i:
#                 e2=(i.split(i[q]))


# if len(e2)>2:
#     print(e4)
# else:
#     print("".join(e2))






# s = "YazaAay"

# e=[]

# ss= set(s)


# for i in s:
#     if (i.lower() not in ss) or (i.upper() not in ss):
#         d=s.split(i)

# print(d)


# for s in d:
#     print(s)
#     for i in s:
#         print(i,'last loop')
        
#         if (i.lower() not in ss) or (i.upper() not in ss):
#             f=s.split(i)



# print(f)




        

# # new=s.split(e)


# # for i in e:
# #     print(e[0][0])






#  Longest Nice Substring


# s = "YazaAay"

# ##logic:  need to find small and big characters 


# l1= []
# l2= []
# l3= []


# for i in s:
#     if i.lower() in s  and i.upper() in s :
#         pass 

#     else: 
#         l1.append(i)


# d=s.split(l1[0])

# # print(d)

# # Step 3: Now loop through each split part and check again

# final_parts = []

# for part in d:
#     # print(part)

#     temp = [part]
#     # print(temp)
#     for ch in part:

#         if ch.lower() in part and ch.upper() in part:
#             pass 
#         else:
#              # If bad char found in this part, split it again
#             new_temp= []
#             for t in temp:
#                 new_temp.extend(t.split(ch))
            
#             temp= new_temp

#     final_parts.extend(temp)


# print(final_parts)

# for i in final_parts:
#     if  i == "": 
#         pass
#     else:
#         print(i)




s = "YazaAay"


e=  []
e2= []



if s == "":
    print("")




else:
    found = False 

    for i in range(len(s)):                                    
        if (s[i].lower() not in s) or (s[i].upper() not in s):
            print(s[i])
            e= s.split(s[i])

            found = True 
            break

    if not found:
        # if no bad character found, the string itself is nice    
        pass

    else:



        for i in e: 
            for q in range(len(i)):
                if (i[q].lower() not in i) or (i[q].upper() not in i):
                    e2= i.split(i[q])
                    break


    print("".join(e2))





