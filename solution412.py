# https://leetcode.com/problems/fizz-buzz/description/?envType=problem-list-v2&envId=string
# 412. Fizz Buzz

# answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
# answer[i] == "Fizz" if i is divisible by 3.
# answer[i] == "Buzz" if i is divisible by 5.
# answer[i] == i (as a string) if none of the above conditions are true.



# Example 1:
# Input: n = 3
# Output: ["1","2","Fizz"]

# Example 2:
# Input: n = 5
# Output: ["1","2","Fizz","4","Buzz"]

# Example 3:
# Input: n = 15
# Output: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]




# Input: n = 3
# Output: ["1","2","Fizz"]



# logic:  user 15 multiple condition on first line 


n=15

e=[]

for i in range(1,n+1):
    if i %3 ==0 and i%5 ==0:
        e.append("FizzBuzz") 

    elif i % 3 ==0:
        e.append("Fizz")
 
    elif i % 5== 0:
        e.append("Buzz") 
 
    else:
        e.append(str(i))

print(e)
