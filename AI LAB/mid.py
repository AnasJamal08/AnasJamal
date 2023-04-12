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
dfs(visited, graph, 'B','G')