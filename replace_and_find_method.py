#replace()
# find()

string1="She is so beautiful and she is good dancer."

# print(string.replace(" ","_"))
# print(string.replace("is","was"))
# print(string.replace("is","was", 1))


is_pos1=(string1.find("is"))
is_pos2=(string1.find("is",is_pos1+1))
print(is_pos2)