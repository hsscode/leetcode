# Reverse Vowels of a String

# Given a string s, reverse only all the vowels in the string and return it.
# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.


# Input: s = "IceCreAm"      IceCreAm >

# Output: "AceCreIm"

# The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

# Input: s = "leetcode"
# Output: "leotcede"
 

 
s = "IceCreAm"

sl= list(s)

vowel = ['A','E','I','O','U', 'a','e','i','o','u']

left = 0
right= len(s)-1


while left < right:
    if sl[left] in vowel and sl[right] in vowel :
        sl[left] , sl[right] = sl[right], sl[left]

        left = left + 1 
        right = right -1 
    else:
        if sl[left] not in vowel:
            left = left + 1 
        
        if sl[right] not in vowel:
            right = right - 1 



print("".join(sl))

