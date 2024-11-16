# Given two strings ransomNote and magazine, 
# return true if ransomNote can be constructed by using the letters from magazine and false otherwise.
# Each letter in magazine can only be used once in ransomNote.


# Input: ransomNote = "a", magazine = "b"
# Output: false

# Input: ransomNote = "aa", magazine = "ab"
# Output: false

# Input: ransomNote = "aa", magazine = "aab"
# Output: true




#logic : if ransom exist in magazine  and 

# ransomNote = "bg"
# magazine = "efjbdfbdgfjhhaiigfhbaejahgfbbgbjagbddfgdiaigdadhcfcj"

ransomNote = "aa"
magazine = "ab"


a= ''.join(sorted(ransomNote))
b= ''.join(sorted(magazine))

print(a,b)

# if a in b:
#     print(True)
# else:
#     print(False)



# for i in a:
#     if i not in b:
#         print(False)
#         break
#     else:
#         print(True)


for i in a:
    if i not in b:
        print(False)
        break
    
    else:
        b=b.replace(i,'',1)
else:
    print(True)



# for i in a:
#     if i in b:
#         b=b.replace(i,'')
        
#     print(True)

# else:
#     print(False)

