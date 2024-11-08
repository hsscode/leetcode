# Longest Common Prefix

# Input: strs = ["flower","flow","flight"]
# Output: "fl"



# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.


# Logic:  sort the string > match 1st char of first word with last word's first char


strs = ["flower","flow","flight"]
# strs = ["dog","racecar","car"]
# strs = ["dog","racecar","car"]

#sort the string 
strs.sort()

#now find the smallest word so that we can itterate upto min length of the word 

e= []

for i in strs:
    e.append(len(i))

min_word_len= min(e)

ans=[]

#now  fix the first word 

# fw= strs[0][0]
# lw= strs[-1][0]
# print(fw,lw)

# fw= strs[0][1]
# lw= strs[-1][1]
# print(fw,lw)

# fw= strs[0][2]
# lw= strs[-1][2]
# print(fw,lw)
#here it is not matching ,, ans is fl , now this is hardcoded , we have to make it dynamic 

for i in range(min_word_len):
    if strs[0][i] != strs[-1][i]:
        break
    else:
        ans.append(strs[0][i])


print("".join(ans))




