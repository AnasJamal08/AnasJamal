# How to create sets
s={1,2,3}
s10={3,4,5}
# l=[1,2,3,4,4,4,5,5,6,6,7,7,8,8]
# s2=set(l)
# s3=list(set(l))
# print(s3)
# print(s2)
s.add(4)
s.add(5)
print(s)
s.remove(5)   #While using remove if we put an element which is not in set,then there would be an error
print(s)
s.discard(7)
print(s)  #But there will be no error in discard()
# s.clear()
# print(s)
s1=s.copy()
print(s1)


union_set=s|s10
print(union_set)

intersection=s&s10
print(intersection)


