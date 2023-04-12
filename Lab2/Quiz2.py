from queue import PriorityQueue



graph = {
    'A':[[5,'B'],[10,'C']],
    'B':[[2,'C'],[1,'E']],
    'C':[[4,'G']],
    'D':[[1,'B'],[4,'E']],
    'E':[[3,'G']],
    'G':[[]],
    'S':[[3,'A'],[2,'D']]
}
heuristic={
    'A':9,
    'B':4,
    'C':2,
    'D':5,
    'E':3,
    'G':0,
    'S':7
    
}
def calculateTotalCost(preCost,item,heuristic):
    totalCost=preCost+item[0]+heuristic[item[1]]
    return [totalCost,item[0],item[1]]


q = PriorityQueue()
def DFS(graph,heuristic,node,goal):
    previousPathCost=0
    if node==goal: 
        print("Goal Found ",node)
        return
    print(node,end="->")

    for item in graph[node]:
        cost=calculateTotalCost(previousPathCost,item,heuristic)
        q.put(cost)
      
    while not q.empty():
    
        currnode=q.get()
    
        
        previousPathCost=previousPathCost+currnode[1]
        

        if currnode[2]==goal: 
            print(currnode[2])