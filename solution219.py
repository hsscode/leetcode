# # https://leetcode.com/problems/happy-number/description/?envType=study-plan-v2&envId=top-interview-150

# # 202. Happy Number


# # Example 1:
# # Input: n = 19
# # Output: true




# logic: make this number in string so that we can seperate using for loop, then do sq individually and sum,, 
# when u used this number , put it into the set,,  so that u can check if this no is not already used.



n= 19 

keep= set()


while n != 0 and  n not in keep:
    keep.add(n)
    total= 0

    for i in str(n):
        total = total + int(i)**2
        n= total 

if n ==1 :
    print(True)

else:
    print(False)































# n= 19 

# no_check= set()



# while n !=1 and n not in no_check:

#     total=0

#     for i in str(n):
#         total= total + int(i)**2 
#         no_check.add(n)
#         n = total

# if n==1 :
#     print(True)
# else:
#     print(False)




















# # n= 19
# # p1 = 0
# # nn= str(n)

# # a=''
# # b=''

# # i=0
# # q= len(nn)-1

# # while n != 1:
# #     n= 19
# #     a=nn[i]
# #     b= nn[q]
# #     p1=int(a)*int(a) + int(b)*int(b)
# #     p1 = p1
# #     n= int(p1)
# #     print(n)


# # print(n)


# n = 2

# seen = set()

# while n != 1 and n not in seen:
#     seen.add(n)
#     total = 0
#     for digit in str(n):
#         total += int(digit) ** 2
#     n = total
#     print(n)  # To trace the steps

# if n == 1:
#     print(True)
# else:
#     print(False)




# n= 2
# x=n
# while x >=10:
#     sum=0 
#     while x >0:
#         r= x % 10 
#         sum = sum + (r**2)
#         x= x//10
#         print(sum)
#     x= sum 
# if x==1:
#     print(True)
# else:
#     print(False)


