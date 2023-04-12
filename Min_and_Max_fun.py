nums=[2,20,4]

# print(min(nums))
# print(max(nums))

def greatest_diff(l):
    return max(l)-min(l)


print(greatest_diff(nums))