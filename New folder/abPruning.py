# graph={'A':['B','C'],
# 'B':['D','E'],
# 'C':['F','G'],
# 'D':['H','I'],
# 'E':['J','K'],
# 'F':['L','M'],
# 'G':['N','O'],
# 'H':[],
# 'I':[],
# 'J':[],
# 'K':[],
# 'L':[],
# 'M':[],
# 'N':[],
# 'O':[]
# }
# val = {
#     'H':5,
#     'I':3,
#     'J':7,
#     'K':2,
#     'L':4,
#     'M':3,
#     'N':1,
#     'O':7,
#     'A':-1,
#     'B':-1,
#     'C':-1,
#     'D':-1,
#     'E':-1,
#     'F':-1,
#     'G':-1
# }


graph={'A':['B','C'],
'B':['D','E'],
'C':['F','G'],
'D':['H','I'],
'E':['J','K'],
'F':['L','M'],
'G':['N','O'],
'H':['P','Q'],
'I':['R','S'],
'J':['T','U'],
'K':['V','W'],
'L':['X','Y'],
'M':['Z','Z1'],
'N':['Z2','Z3'],
'O':['Z4','Z5'],
'P':[],
'Q':[],
'R':[],
'S':[],
'T':[],
'U':[],
'V':[],
'W':[],
'X':[],
'Y':[],
'Z':[],
'Z1':[],
'Z2':[],
'Z3':[],
'Z4':[],
'Z5':[],
}
val = {
    'A':-1,
    'B':-1,
    'C':-1,
    'D':-1,
    'E':-1,
    'F':-1,
    'G':-1,
    'H':-1,
    'I':-1,
    'J':-1,
    'K':-1,
    'L':-1,
    'M':-1,
    'N':-1,
    'O':-1,
    'P':3,
    'Q':4,
    'R':2,
    'S':1,
    'T':7,
    'U':8,
    'V':9,
    'W':10,
    'X':2,
    'Y':11,
    'Z':1,
    'Z1':12,
    'Z2':14,
    'Z3':9,
    'Z4':13,
    'Z5':16,
}


i=0
def ABPruning(graph,node,parent):
    global i

    i+=1

    children = graph[node]
    if children:
        for child in children:
            if val[node] == -1:
                val[node] = ABPruning(graph,child,val[node])
            else:
                if i%2:
                    if parent == -1:
                        if val[node] < ABPruning(graph,child,val[node]):
                            val[node] = ABPruning(graph,child,val[node])
                    else:
                        if parent <= val[node]:
                            i-=1
                            return val[node]
                        else:
                            if val[node] < ABPruning(graph,child,val[node]):
                                val[node] = ABPruning(graph,child,val[node])
                    
                else:
                    if parent == -1:
                        if val[node] > ABPruning(graph,child,val[node]):
                            val[node] = ABPruning(graph,child,val[node])
                    else:
                        if parent >= val[node]:
                            i-=1
                            return val[node]
                        else:
                            if val[node] > ABPruning(graph,child,val[node]):
                                val[node] = ABPruning(graph,child,val[node])

    i-=1
    return val[node]


ABPruning(graph,'A',-1)
print(val)
