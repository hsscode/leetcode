# https://leetcode.com/problems/longest-palindrome/description/?envType=problem-list-v2&envId=string&difficulty=EASY
# 409. Longest Palindrome


# Example 1:
# Input: s = "abccccdd"
# Output: 7
# Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.



# Example 2:
# Input: s = "a"
# Output: 1
# Explanation: The longest palindrome that can be built is "a", whose length is 1.



# logic: Finding the longest palindrome >>  palindrome ex are:
# # soos , moom, deed, ddssassdd, sssss, aaa, asdedsa , asa
# s2,o2 4 2 

# booksb
# b2, o2, k1, s1


# So here we have to count the char only and on bASIS of that finalise the decision 


s = "ccc"
d={}
count=0
is_even= True



# making dict to store the count of the word 

for i in s:
    d[i]= s.count(i)
print(d)



for key , values in d.items():
    if values % 2 == 0 :
        count= count + values   # adding all even numbers 


    else:
        is_even= False
        count= count + values -1      #here to get the largest even number from the odd we are minusing 1 ,, eg. ccc c3-1 c2 will be considered 

        

if is_even==False:           #to add the 1   number at the centre 
    count= count + 1   #to keep only 1 number at the centre 



print(count)