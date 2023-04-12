#AI LAB ASSESMENT 2
import random as rand
def prob_c(att):
    for i in att:
        prob.append(round((i/sum(att))*100,2))
def crossover(lst1,lst2,lst3,lst4):
    lst1[rand.randint(0,3)]=rand.randint(1,4)
    lst2[rand.randint(0,3)]=rand.randint(1,4)
    lst3[rand.randint(0,3)]=rand.randint(1,4)
    lst4[rand.randint(0,3)]=rand.randint(1,4)
    print("Cross-over = ",lst1,lst2,lst3,lst4)
def selection(lst1,lst2,lst3,lst4):
    #75% same
    temp=lst1[3]
    lst1[3]=lst2[3]
    lst2[3]=temp
    #50% same
    for i in range(2,4):
        temp=lst3[i]
        lst3[i]=lst4[i]
        lst4[i]=temp
    print("Selection Answer= ",lst1,lst2,lst3,lst4)
def attack (x1,y1,x2,y2):
    attck=int()
    if (x1==x2):
        attck+=1
    #Up Left Diagonal
    i=x1
    j=y1
    while i>0 or j>0:
        if x2==i and y2==j:
            attck+=1
            
        i-=1
        j-=1
    #Down Left Diagonal
    i=x1
    j=y1
    while i<4 or j<4:
        
        if x2==i and y2==j:
            attck+=1
            
        i+=1
        j+=1
    #Up Right Diagonal
    i=x1
    j=y1
    while i>0 or j<4:
        
        if x2==i and y2==j:
            attck+=1
            
        i-=1
        j+=1
    #Down Right Diagonal
    i=x1
    j=y1
    while i<4 or j>0:
        
        if x2==i and y2==j:
            attck+=1
            
        i+=1
        j-=1
    return attck
att=list()
prob=list()
select=list()
player1=[2,3,1,2]
player2=[1,2,1,1]
player3=[3,3,2,4]
player4=[1,3,4,2]
def main_function():
    x=int()
    for i in range(len(player1)):
        for j in range(i+1,len(player1)):
            x+=attack(player1[i],i,player1[j],j)
    att.append(x)
    x=0
    for i in range(len(player2)):
        for j in range(i+1,len(player2)):
            x+=attack(player2[i],i,player2[j],j)
    att.append(x)
    x=0
    for i in range(len(player3)):
        for j in range(i+1,len(player3)):
            x+=attack(player3[i],i,player3[j],j)
    att.append(x)
    x=0
    for i in range(len(player4)):
        for j in range(i+1,len(player4)):
            x+=attack(player4[i],i,player4[j],j)
    att.append(x)
    #att.sort(reverse=True)
    print("Initial position= ",player1,player2,player3,player4)
    print("Attacks =",att)
    prob_c(att)
    print("Probability =",prob)
    prob.clear()
    selection(player1,player2,player3,player4)
    crossover(player1,player2,player3,player4)
    if att.count(0)>0:
        print("Game Over \n")
    else:
        att.clear()
        main_function()
main_function()