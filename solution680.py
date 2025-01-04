# https://leetcode.com/problems/valid-palindrome-ii/description/?envType=problem-list-v2&envId=string

# 680. Valid Palindrome II

# Given a string s, return true if the s can be palindrome after deleting at most one character from it.


# Input: s = "aba"
# Output: true



# Input: s = "abca"
# Output: true
# Explanation: You could delete the character 'c'.


# Input: s = "abc"
# Output: false


# logic: 1st valid palindrome using 2 pointer 



#palindrome test and check--------------

strings = "fjsdkffnefe"


p1= 0
p2 = len(strings)-1




while p1<p2:

    if strings[p1] != strings[p2]:
        leftskip = strings[p1+1: p2+1]
        rightskip= strings[p1:p2]

        if leftskip == leftskip[::-1]  or  rightskip == rightskip[::-1]: 
            print("palindrome")
        else:
            print("not palindrome")
            
        break    ###avoiding multiple same output


    elif strings== strings[::-1]:
        print("Palindrome")
        break             ####avoiding multiple same output
    
    p1 = p1 + 1 
    p2=  p2 - 1 


