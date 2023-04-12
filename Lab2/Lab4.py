graph={
    'A':[[7,'B'],[3,'C']],
    'B':[[2,'C'],[3,'D']],
    'C':[[7,'D'],[2,'E']]
}

# print(graph['B'][1][1])

# for item in graph:
#     temp=graph[item]
#     temp.sort()
#     print(temp)
visited=set()
def dfs(visited,graph,node):
    if node in visited:
        return
    else:
        for i in graph:
            temp=graph[i]
            temp=temp.sort()
            tempnode=temp[0]
            print(tempnode)
            visited.add(i)
            for i in tempnode:
                dfs(visited,graph,i)


print(dfs(visited,graph,'A'))