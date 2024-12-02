# Check If a Word Occurs As a Prefix of Any Word in a Sentence
# sentence = "i love eating burger" 
# searchWord = "burg"
# # Output: 4
####################

# sentence = "this problem is an easy problem"
# searchWord = "pro"

# sentence = "i am tired" 
# searchWord = "you"


sentence = "this problem is an easy problem"
searchWord = "this"


words= sentence.split(" ")

for i, q in enumerate(words,1):   #here we use 1 to start counting /index from the 1 , default it is 0
    if q.startswith(searchWord):
        print(i)
        break


else:
    print(-1)




# for i in words:
#     if searchWord in i and searchWord[0] ==i[0]:
#         print(words.index(i) + 1 )
#         check= True
#         break

# if check == False:
#     print(-1)

