# bfs and dfs using python language


# graph={
#     'A':['B','C'],
#     'B':['D','E'],
#     'C':['F'],
#     'D':[],
#     'E':['F'],
#     'F':[]
# }


# visited_nodes=set() #set to keep track of visited nodes of graph.

# def dfs(visited_nodes,graph,node): #function for dfs
#     if node not in visited_nodes:
#         print(node)
#         visited_nodes.add(node)
#         for neighbour in graph[node]:
#             dfs(visited_nodes,graph,neighbour)

# print("following is depth first search")
# dfs(visited_nodes,graph,'5')





# Using a Python dictionary to act as an adjacency list
graph = {
  'A' : [[0,'B'],[0,'E']],
  'B' : [[0,'D'],[0,'C'],[0,'G']],
  'E' : [[0,'F']],
  'G' : [],
  'C' : [[0,'F']],
  'F' : [[0,'G']],
  'D' : [[0,'E'],[0,'G']]
  
}  
print("The Path Is = ",end = " ")
found=0
visited =[]
def dfs(visited, graph, node,goal):
    global found
    if found==1:
        return
    elif node not in visited:
        print(node,end=" ")
        if node ==goal:
            print ("\n***Goal Found***")
            found=1 
            return
        visited.append(node)
        templist=graph[node]
        # templist.sort()
        for neighbour in templist:
            if len(neighbour)>0:
                dfs(visited, graph,neighbour[1],'G')
dfs(visited, graph, 'A','G')