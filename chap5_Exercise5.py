def common_finder(l1,l2):
    common_list=[]
    for i in l1:
        if i in l2:
            common_list.append(i)
    return common_list
    


print(common_finder([1,2,3,4],[3,4,5,6]))   