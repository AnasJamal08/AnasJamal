graph={
    'A':[[0,'B'],[0,'C']],
    'B':[[0,'D'],[0,'E']],
    'C':[[0,'F'],[0,'G']],
    'D':[[0,'H'],[0,'I']],
    'E':[[0,'J'],[0,'K']],
    'F':[[0,'L'],[0,'M']],
    'G':[[0,'N'],[0,'O']],
    'H':5,
    'I':4,
    'J':7,
    'K':3,
    'L':7,
    'M':6,
    'N':2,
    'O':9
}
# print(G)
def dfs(G,node,flag):
    # if type(G[node])==int:
    #     return G[node]
    #     print("It is leaf node.")

    var=G[node]
    if isinstance(var,int):
        return var
    minimum=1000
    maximum=0
    result=0
    for i in G[node]:
        # print(i)
        if flag==0:
            value=dfs(G,i[1],1)
            # result=G[node][1]
            if value>maximum:
                maximum=value
                result=maximum
        else:
            value=dfs(G,i[1],0)
            if value<minimum:
                minimum=value
                result=minimum
    G[node]=result
    return result

print(dfs(graph,'A',0))
print(graph)