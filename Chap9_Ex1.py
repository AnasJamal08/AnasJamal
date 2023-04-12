def reverse_fun(l):
    return [name[::-1] for name in l]


print(reverse_fun(['abc','xyz','Tom']))



numbers=list(range(1,11))
even_numbers=[i for i in range(1,11) if i%2==0]
odd_numbers=[i for i in range(1,11) if i%2!=0]
print(odd_numbers)
print(even_numbers)


# Exercise 2
def num_to_str(l):
    return [str(i) for i in l if (type(i)==int or type(i)==float)]

print(num_to_str(['Anas',1,2,1.3,[1,2,3],{'Anas':'3'}]))