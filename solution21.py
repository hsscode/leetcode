# https://leetcode.com/problems/merge-two-sorted-lists/description/?envType=study-plan-v2&envId=top-interview-150

# node logic: https://www.youtube.com/watch?v=j_UNYW6Ap0k

# 21. Merge Two Sorted Lists

# this is the simple solution but has differnt req --

# list1 = [1,2,4] 
# list2 = [1,3,4]


# # Output: [1,1,2,3,4,4]

# e=[]


# e= list1 + list2 

# for i in range(len(e)):
#     for q in range(len(e)-1):
#         if e[i]<e[q]:
#             e[i],e[q]= e[q], e[i]

# print(e)



## now using two pointer approach 


list1 = [1,2,4,6,7]
list2 = [1,3,4]

p1,p2= 0,0   # initing from the 0  from both pointers


merge_list= []  #create empty list 


while p1< len(list1) and p2<len(list2):   #run untill the both list lenth used 

    if list1[p1]<=list2[p2]:  # if p1 value is smaller or equal then insert into the empty list 
        merge_list.append(list1[p1])
        p1 = p1 + 1   #increasing the count of the pointer 

    else:   #else here we append the p2 value  
        merge_list.append(list2[p2])
        p2=p2+ 1 

# where this loop if one of  both list length used then we check remaining elements from the both list 
#here we are checking for the list 1 

while p1 < len(list1):
    merge_list.append(list1[p1])
    p1= p1+ 1 

#same here we are checking  for the list 2 

while p2 < len(list2):
    merge_list.append(list2[p2])
    p2 = p2  +  1 

print(merge_list)


##this is the pointer technique which we are using and can be helpful for practise 

