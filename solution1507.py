# https://leetcode.com/problems/reformat-date/description/?envType=problem-list-v2&envId=string&difficulty=EASY

# 1507. Reformat Date


# Example 1:
# Input: date = "20th Oct 2052"
# Output: "2052-10-20"

# Example 2:
# Input: date = "6th Jun 1933"
# Output: "1933-06-06"

# Example 3:
# Input: date = "26th May 1960"
# Output: "1960-05-26"


# Convert the date string to the format YYYY-MM-DD, where:



# ssssDay is in the set {"1st", "2nd", "3rd", "4th", ..., "30th", "31st"}.
# Month is in the set {"Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"}.

Day = {"1st", "2nd", "3rd", "4th","30th", "31st", "20th"} 
Month = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
# Year= [1900, 2100]


# Output: "2052-10-20"




date=  "6th Jun 1933"


print(date[-4:])


# date = "20th Oct 2052"
# print(len(date),"lke")



yyyy=""

month_d= {}
for a,v in enumerate(Month,1):
    month_d[v]=a




date_split= date.split(" ")

if len(date)==13:
    dd=date[:2]
    yyyy= date[-4:]

else:
    dd= date[:1]
    yyyy= date[-4:]


for i in date_split:
    if i in month_d:
        mm= month_d[i]



# if len(str(dd))==1 :
#     dd= "0"+str(dd)


if len(str(mm)) ==1 :   #i can use print(dd.zfill(2)) too

    mm= "0"+str(mm)


print(dd)
print(mm)

print(yyyy)


ans=str(yyyy+str("-")+str(mm)+("-")+dd)

print(ans)







# ________


