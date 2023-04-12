P1=[2,3,1,2]


q_index=[]
def index(p):
    att_count=0
    tempr=0
    tempc=0
    for i in range(0,4):
        tempc=i
        tempr=p[i]-1
        q_index.append([tempr,tempc])
        
    for j in range(0,4):
        for k in range(j+1,4):
            if q_index[j][0]==q_index[k][0]:
                print(f"same row of Q{j+1}  Q{k+1}")
                att_count+=1
                print(att_count)
    for m in q_index:
        temp=list(i+1 for i in m)
        while temp[0]<=3:
            if m==temp:
                print(f"attck at {temp[1]}")
                att_count+=1
    
        
                
        
index(P1)
print(q_index)