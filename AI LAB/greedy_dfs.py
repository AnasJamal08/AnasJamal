from queue import PriorityQueue
graph = {
    
    'S' : [[3,'A'],[2,'D']],
  'A' : [[5,'B'],[10,'c']],
  'B' : [[2,'C'],[1,'E']],
  'C' : [[4,'G']],
  'D' : [[1,'B'],[4,'E']],
  'E' : [[3,'G']],
  
}

heuristic={
    'S' : 7,
    'A' : 9,
    'B' : 4,
    'C' : 2,
    'D' : 5,
    'E' : 3,
    'G' : 0
}

visited=set()
found=0
def greedy_dfs(visited,graph,node,goal,hn):
    if found==1:
        return
    elif node not in visited:
        
