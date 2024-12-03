# Adding Spaces to a String

s = "EnjoyYourCoffee" 
spaces = [5, 9]
# Enjoy Your Coffee

e=[]


for i in range(len(s)):
    if i in spaces:
        e.append(" ")
        e.append(s[i])
        
    else:
        e.append(s[i])

print("".join(e))



#         print(i,q)
        # e.append(s[i])
        # if q ==i:
        #     e.append(" ")
        #     break



# for i in enumerate(s,1):




