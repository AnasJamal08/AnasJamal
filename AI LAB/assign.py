# DFS CODE

# graph = {
#   'A' : [[8,'B'],[5,'E']],
#   'B' : [[2,'D'],[1,'C']],
#   'E' : [[1,'G']],
#   'G' : [],
#   'C' : [[3,'F']],
#   'F' : [[4,'G']],
#   'D' : [[3,'E']]
  
# }  
# print("The Path Is = ",end = " ")
# found=0
# visited = set()
# def dfs(visited, graph, node,goal):
#     global found
#     if found==1:
#         return
#     elif node not in visited:
#         print(node,end=" ")
#         if node ==goal:
#             print ("\n***Goal Found***")
#             found=1 
#             return
#         visited.add(node)
#         templist=graph[node]
#         templist.sort()
#         for neighbour in templist:
#             if len(neighbour)>0:
#                 dfs(visited, graph,neighbour[1],'G')
# dfs(visited, graph, 'A','G')



# BFS CODE




# graph = {
#   'A' : ['B','E'],
#   'B' : ['D','C'],
#   'E' : ['G'],
#   'G' : [],
#   'C' : ['F'],
#   'F' : ['G'],
#   'D' : ['E']
  
# }  




# def BFS(graph, starting_node, goal):
#     visited = []
#     queue = [[starting_node]]
    
#     while queue:
#         path = queue.pop(0)
#         node = path[-1]
#         if node not in visited:
#             neighbours = []
#             for edge in graph[node]:
#                 neighbours.append(edge)
#             for neighbour in neighbours:
#                 new_path = list(path)
#                 new_path.append(neighbour)
#                 queue.append(new_path)
                
#                 if neighbour == goal:
#                     return new_path
            
#             visited.append(node)


# print(BFS(graph, 'A', 'D'))




# UCS


from queue import PriorityQueue
graph = {
  'A' : [[10,'B'],[8,'C']],
  'B' : [[5,'D'], [3,'F'],[2,'E']],
  'C' : [[5,'F']],
  'D' : [],
  'E' : [[2,'F']],
  'F' : []
}

mygoal='F' 
visited=set()
def UCS(visited, graph, startnode,goal):  #function for dfs 
    
    expque=PriorityQueue()
    path=[startnode]
    visited = set() # Set to keep track of visited nodes of graph.
    expque.put((0,startnode,startnode))
    
    while expque.qsize() > 0 :
        
        node=expque.get()
        curcost=node[0]
        curname=node[1]
        curpath=node[2]
        
              
        if curname not in visited:
            visited.add(curname)
            print('name:', curname, '\t gn:', curcost)
            
            if curname==goal:
                print ('---Goal Found---' )
                print('Path Cost: ',curcost,'Path Track: ',curpath )
                return
            
            suclist=graph[curname]
            for sucnode in suclist:
                if sucnode[1] not in visited:
                    gn=sucnode[0]+curcost                                  
                    st=''
                    st=node[2]+' '+sucnode[1]
                    expque.put((gn,sucnode[1],st))
                    

print("Following is the Uniform Cost Search")
UCS(visited, graph, 'A',mygoal)