# Longest Uncommon Subsequence I-----------


# Input: a = "aba", b = "cdc"
# Output: 3

# Input: a = "aaa", b = "bbb"
# Output: 3

# Input: a = "aaa", b = "aaa"
# Output: -1



# a = "aba" 
# b = "cdc"


a = "aaa" 
b = "bbb"

if a==b or a == b[::-1]:
    print(-1)


else:
    if a not in b:
        if len(a)>len(b):
            print(len(a))
        else:
            print(len(b))


