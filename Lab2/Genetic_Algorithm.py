import random
def attack(r1,c1,r2,c2):

    if r1==r2:
        return True
    #Left to right 
    #up
    i=r1
    j=c1
    while i<5 or j<5:
        if i==r2 and j==c2:
            return True
        i+=1
        j+=1
    #down
    i=r1
    j=c1
    while i>0 or j>0:
        if i==r2 and j==c2:
            return True
        i-=1
        j-=1
    #Right to Left 
    #up
    i=r1
    j=c1
    while i>0 or j<5:
        if i==r2 and j==c2:
            return True
        i-=1
        j+=1
    #Down
    i=r1
    j=c1
    while i<5 or j>0:
        if i==r2 and j==c2:
            return True
        i+=1
        j-=1

def selection(pl):
    q1=random.choice(pl)
    q2=random.choice(pl)
    q3=random.choice(pl)
    q4=random.choice(pl)
    print("\nBefore Selection\n",q1,q2,q3,q4)
    temp=q1[3]
    q1[3]=q2[3]
    q2[3]=temp
    
    for i in range(2,4):
        temp=q3[i]
        q3[i]=q4[i]
        q4[i]=temp
    print("\nAfter Selection\n",q1,q2,q3,q4)
    plist=[q1,q2,q3,q4]
    mutation(plist)

def mutation(plist):
    print("\nBefore Mutation",plist)
    print("\nAfter Mutation\n")
    for i in plist:
        x=random.choice(i)
#         print(x)
        #print(i)
        y=random.randint(1,4)
        n_index=i.index(x)
        i[n_index]=y
#         print(y)
        print(i)
    game(plist)

p1=[2,3,3,3]
p2=[3,2,4,1]
p3=[1,4,2,3]
p4=[3,2,1,3]
pl=[p1,p2,p3,p4]
no_attack=[]
count=0

def game(pl):

    ind=[]
    for k in pl:
        count=0
        for i in range(len(k)):
            for j in range(i+1,len(k)):
                if attack(k[i],i+1,k[j],j+1):
                    count+=1
        no_attack.append(count)    
        print(f"Number of attacks : {count} for {k}")
        for i in no_attack:
            if i==0:
                return True
    selection(pl)

if game(pl):
    print("Goal Found")

