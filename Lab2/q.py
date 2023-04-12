from queue import PriorityQueue
graph = {
  'S' : [[10,'A'],[2,'D']],
  'A' : [[5,'B'], [10,'C']],
  'D' : [[4,'E'],[1,'B']],
  'B' : [],
  'C' : [[4,'G']],
  'E' : [[3,'G']],
  'G' : []
}

heuristic={
    'S' : 7,
    'A' : 9,
    'D' : 5,
    'B' : 4,
    'C' : 2,
    'E' : 3,
    'G' : 0
}

mygoal='G' 
visited=set()
def A_staric(visited, graph, startnode,goal,hn):  
    
    expque=PriorityQueue()
    path=[startnode]
    visited = set() 
    expque.put((0,startnode,startnode,0))
    
    while expque.qsize() > 0 :
        
        node=expque.get()
        huer=node[3]
        curcost=node[0]-huer
        curname=node[1]
        curpath=node[2]

        
        
        if curname not in visited:
            visited.add(curname)
            print('name:', curname, '\t gn:', curcost+huer)
            
            if curname==goal:
                print ('---Goal Found---' )
                print('Path Cost: ',curcost+huer,'Path Track: ',curpath )
                return
            
            suclist=graph[curname]
            for sucnode in suclist:
                if sucnode[1] not in visited:
                    gn=sucnode[0]+curcost+ hn[sucnode[1]]
                    st=''
                    st=node[2]+' '+sucnode[1]
                    expque.put((gn,sucnode[1],st,hn[sucnode[1]]))
                    

print("Following is the A*")
A_staric(visited, graph, 'G',mygoal,heuristic)