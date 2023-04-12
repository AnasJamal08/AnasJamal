P1=[2,3,1,2]
q_index=[]
def index(q):
    # att_count=0
    temp_row=0
    temp_col=0
    for i in range(0,4):
        temp_col=i
        temp_row=q[i]-1
        q_index.append([temp_row,temp_col])

index(P1)
for j in range(0,4):
    for k in range(j+1,4):
        if q_index[j][0]==q_index[k][0]:
            print(f"Same row of Q{j+1} Q{k+1}")
            # att_count+=1
            # print(att_count)
for m in q_index:
    temp=list(i+1 for i in m)
    # print(temp)
    while temp[0]<=3:
        if m==temp:
            print(f"Attack at Q{temp[1]+1}")
            # att_count+=1
    


print(q_index)


