#151 Reverse Words in a String

# s = "  hello world  "
# "world hello"

# Input: s = "the sky is blue"
# Output: "blue is sky the"

# s="the sky is blue"
# s = "  hello world  "


s="a good   example"     ####Return a string of the words in reverse order concatenated by a single space.
# here strip is not gonna work as it handle extra spapce from front and back



ss= s.strip()


a= ss.split()    #split handle all spaces goood

print(a)

print(" ".join(a[::-1]))
