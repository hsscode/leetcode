# 128. Longest Consecutive Sequence
# https://leetcode.com/problems/longest-consecutive-sequence/description/?envType=study-plan-v2&envId=top-interview-150


# nums = [100,4,200,1,3,2]
# Output: 4

# nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9


# Logic: first sort then  delta should be 1 

# nums = [100,4,200,1,3,2]
# nums = [0,3,7,2,5,8,4,6,0,1]
# nums= [9,1,4,7,3,-1,0,5,8,-1,6]
# nums= [0,3,7,2,5,8,4,6,0,1]

nums= [1,2,0,1]


nums= set(nums)
numss= sorted(nums)

e=[]

for i in range(len(nums)-1):
    if numss[i+1]- numss[i]==1:
        e.append("1")
    else:
        e.append("0")


ee="".join(e)

# print(ee)
splitt= ee.split("0")


e= []
for i in splitt:
    e.append(len(i))


print(max(e)+1)
