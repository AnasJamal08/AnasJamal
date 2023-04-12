# min_max algo

graph={
    'A':['B','C'],
    'B':['D','E'],
    'C':['F','G'],
    'D':['H','I'],
    'E':['J','K'],
    'F':['L','M'],
    'G':['N','O'],
    'H':3,
    'I':5,
    'J':7,
    'K':4,
    'L':3,
    'M':2,
    'N':3,
    'O':4
}


def dfs(graph,node,flag):
    var=graph[node]
    if isinstance(var,int):
        return var
    diff=13
    summ=0
    results=0
    for i in graph[node]:
        if flag==0:
            val=dfs(graph,i,1)
            # if val > summ:
            summ1=val+summ
            results=summ1
        else:
            value=dfs(graph,i,0)
            # if value < diff:
            diff1=-(value-diff)
            results=diff
    graph[node]=results
    return results


print(dfs(graph,'A',0))
print(graph)