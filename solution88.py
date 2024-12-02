# https://leetcode.com/problems/merge-sorted-array/description/?envType=problem-list-v2&envId=array&difficulty=EASY

# Merge Sorted Array

# nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]
# Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
# The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
#asaa


# nums1 = [1,2,3,0,0,0]  #6
# nums2 = [2,5,6]


# nums1= [4,5,6,0,0,0]
# nums2 =[1,2,3]


nums1=[-1,0,0,3,3,3,0,0,0]
nums2= [1,2,2]

count=0

for i in range(len(nums1)):
        if nums1[i]==0 and count<len(nums2):
              nums1[i]= nums2[count]
              count= count + 1

print(nums1, 'unsorted string ')


#for sorting i can use this loop method 
for i in range(len(nums1)):
    for q in range(len(nums1)-1-i):
        if nums1[q]>nums1[q+1]:
              nums1[q],nums1[q+1]= nums1[q+1], nums1[q]

print(nums1, 'sorted string ')

# or can use sort()

nums1.sort()

print(nums1)

