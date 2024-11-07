# Find the Index of the First Occurrence in a String


# 1st solution: 

haystack = "hello"
needle = "ll"


if needle in haystack:
    print(haystack.index(needle))
else:
    print(-1)





# # The first occurrence is at index 0, so we return 0.

# a=haystack.split(needle)

# print(a)


# # if '' not in a:
# #     print(-1)

# # else:
# #     print(a.index(''))










# class Solution:
#     def strStr(self, haystack: str, needle: str) -> int:
#         if needle in haystack:
#             a=haystack.index(needle)
#             return a
#         else:
#             return -1





