
popolation=[
[1,2,1,2],
[4,3,1,4],
[2,1,3,2],
[2,3,4,1]
]

# goals=[[3,1,4,2],[2,4,1,3]]
no_of_att=[]
q_index=[]
att_prob_per=[]
import random
def AttackOnQueen(p):
    q_index.clear()
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
                # print(f"Attack at Q{k+1} by Q{j+1}")
                att_count+=1
    # print("Lower Moment")
    for m in q_index:
        temp=list(i+1 for i in m)
        # print(f"for Q{temp[1]}")
        while temp[0]<=3 and temp[1]<=3:
            
            # print(temp)
            if temp in q_index:
                # print(f"attck at Q{temp[1]+1}")
                att_count+=1
            temp=list(i+1 for i in temp)
    # print(att_count)
    # print("upper Moment")
    for m in q_index:
        temp=[m[0]-1,m[1]+1]
        # print(f"for Q{temp[1]}")
        while temp[0]>=0 and temp[1]>=0:
            
            # print(temp)
            if temp in q_index:
                # print(f"attck at Q{temp[1]+1}")
                att_count+=1
            temp=[temp[0]-1,temp[1]+1]
    no_of_att.append(att_count)
    print("No of attacks counted successfully.")
    print("No of attacks ",no_of_att)

def fittest_func(attacks):
    sum=0
    new_pop=[]
    # print(attacks)
    for i in attacks:
        sum+=i
    for j in range(0,4):
        att_prob_per.append(((attacks[j]/sum)*100))
    print(att_prob_per)
    for k in range(0,4):
        max_index=att_prob_per.index(max(att_prob_per))
        att_prob_per[max_index]=0
        new_pop.append(popolation[max_index])
        # print(new_pop)
    print("Fittest Function successfull")
    print(new_pop)
    return new_pop





def cross_over(p):
    # print(p)
    for i in range(0,4,2):
        temp1=p[i]
        temp2=p[i+1]
        for j in range((random.randint(0,2))+1,4):
            stemp=temp1[j]
            temp1[j]=temp2[j]
            temp2[j]=stemp
        # print(temp1, temp2)
        p[i]=temp1
        p[i+1]=temp2
    print("Cross-Over function successfull")
    print(p)
    return p

def mutation(p):
    for i in range(0,4,2):
        index1=random.randint(0,3)
        index2=random.randint(0,3)
        temp=p[i][index1]
        p[i][index1]=p[i+1][index2]
        p[i+1][index2]=temp
    print("Mutation successfull")
    print(p)
    return p


while True:
    no_of_att.clear()
    att_prob_per.clear()
    for i in popolation:
        AttackOnQueen(i)
    if 0 in no_of_att:
        index=no_of_att.index(0)
        print(f"goal {popolation[index]} found")
        break

    fit_pop=fittest_func(no_of_att)
    cross_pop=cross_over(fit_pop)
    popolation=mutation(cross_pop)