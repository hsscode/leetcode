# # https://leetcode.com/problems/number-of-days-between-two-dates/?envType=problem-list-v2&envId=string&difficulty=EASY

# # 1360. Number of Days Between Two Dates

# # Input: date1 = "2019-06-29", date2 = "2019-06-30"
# # Output: 1

# # Input: date1 = "2020-01-15", date2 = "2019-12-31"
# # Output: 15


# # date1 = "2019-06-29"
# # date2 = "2019-06-30"

# # date1 = "2020-01-15"
# # date2 = "2019-12-31"


# # import datetime

# # print(date2-date1)



# # import datetime 


# # print(datetime.date.today()) ## to print the date today

# # print(datetime.datetime.now())  current time and date 

# # print(datetime.today()+timedelta(days = 730))






# 1st method : 

date1 = "2018-06-29"
date2 = "2019-06-30"




from datetime import datetime

s1= datetime.strptime(date1, '%Y-%m-%d')
s2= datetime.strptime(date2, '%Y-%m-%d')



if s2>s1:
    print((s2-s1).days)
else:
    print((s1-s2).days)




#2nd method 



from dateutil import relativedelta


s1= datetime.strptime(date1, '%Y-%m-%d')
s2= datetime.strptime(date2, '%Y-%m-%d')


diff= relativedelta.relativedelta(s2,s1)

print(diff,"2nd method")