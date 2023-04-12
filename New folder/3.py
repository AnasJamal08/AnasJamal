Graph={
    'A':['B','I'],
    'B':['C','F'],
    'C':['D','E'],
    'F':['G','H'],
    'I':['J','K'],
    'J':['L','M'],
    'K':['N','O'],
    'D':[],
    'E':[],
    'G':[],
    'H':[],
    'L':[],
    'M':[],
    'N':[],
    'O':[],
}
Cost={
    'A':0,
    'B':0,
    'I':0,
    'C':0,
    'F':0,
    'J':0,
    'K':0,
    'D':9,
    'E':7,
    'G':2,
    'H':3,
    'L':1,
    'M':4,
    'N':5,
    'O':6,

}
# Graph={
#     'A':['B','C'],
#     'B':['D','E'],
#     'C':['F','G'],
#     'D':['H','I'],
#     'E':['J','K'],
#     'F':['L','M'],
#     'G':['N','O'],
#     'H':['H1','H2'],
#     'I':['I1','I2'],
#     'J':['J1','J2'],
#     'K':['K1','K2'],
#     'L':['L1','L2'],
#     'M':['M1','M2'],
#     'N':['N1','N2'],
#     'O':['O1','O2'],
#     'H1':[],
#     'H2':[],
#     'I1':[],
#     'I2':[],
#     'J1':[],
#     'J2':[],
#     'K1':[],
#     'K2':[],
#     'L1':[],
#     'L2':[],
#     'M1':[],
#     'M2':[],
#     'N1':[],
#     'N2':[],
#     'O1':[],
#     'O2':[],
# }
# Cost={
#     'A':0,
#     'B':0,
#     'C':0,
#     'D':0,
#     'E':0,
#     'F':0,
#     'G':0,
#     'H':0,
#     'I':0,
#     'J':0,
#     'K':0,
#     'L':0,
#     'M':0,
#     'N':0,
#     'O':0,
    
#     'H1':2,
#     'H2':3,
#     'I1':9,
#     'I2':7,
#     'J1':5,
#     'J2':3,
#     'K1':5,
#     'K2':1,
#     'L1':9,
#     'L2':5,
#     'M1':4,
#     'M2':3,
#     'N1':2,
#     'N2':1,
#     'O1':10,
#     'O2':5,
# }
Visited=[]


def Check(Key):
    for Val in list(Graph.keys()):
        for Obj in Graph[Val]:
            if Obj==Key:
                return Val
    return False

def AlphaBeta(Start,Flag):
    if len(Start)==0:
        return
    else:
        if Flag==0:
            for Neighbour in Graph[Start]:
                AlphaBeta(Neighbour,1)
                if Cost[Neighbour]<Cost[Start]:
                    Cost[Start]=Cost[Neighbour]
                if Cost[Start]==0:
                    Cost[Start]=Cost[Neighbour]
                if Check(Start):
                    if Cost[Check(Start)]>0:
                        if Cost[Neighbour]<Cost[Check(Start)]:
                            return
        if Flag==1:
            for Neighbour in Graph[Start]:
                AlphaBeta(Neighbour,0)
                if Cost[Neighbour]>Cost[Start]:
                    Cost[Start]=Cost[Neighbour] 
                if Cost[Start]==0:
                    Cost[Start]=Cost[Neighbour]
                if Check(Start):
                    if Cost[Check(Start)]>0:
                        if Cost[Neighbour]>Cost[Check(Start)]:
                            return

AlphaBeta('A',1)
print(Cost)