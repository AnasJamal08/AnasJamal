
def sublist_counter(l):
    countt=0
    for i in l:
        if type(i)==list:
            countt+=1
    return countt


mixed =[1,[1,2],[3,4]]
print(sublist_counter(mixed))      