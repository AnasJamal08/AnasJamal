from queue import Empty, PriorityQueue
graph = {
  'S' : [[3,'A'],[2,'D']],
  'A' : [[5,'B'],[10,'c']],
  'B' : [[2,'C'],[1,'E']],
  'C' : [[4,'G']],
  'D' : [[4,'E'],[1,'B']],
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

mygoal='G' 
visited=set()
def g_dfs(visited, graph, startnode,goal,hn):  
    
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

        expque.queue.clear()
        
        
        
        
        if curname not in visited:
            visited.add(curname)
            print('name:', curname, '\t fn:', curcost+huer)
            
            if curname==goal:
                print ('---Goal Found---' )
                print('Path Cost: ',curcost+huer,'Path Track: ',curpath )
                return
            
            suclist=graph[curname]
            for sucnode in suclist:
                if sucnode[1] not in visited:
                    fn=sucnode[0]+curcost+ hn[sucnode[1]]
                    st=''
                    st=node[2]+' '+sucnode[1]
                    expque.put((fn,sucnode[1],st,hn[sucnode[1]]))
                    

g_dfs(visited, graph, 'S',mygoal,heuristic)