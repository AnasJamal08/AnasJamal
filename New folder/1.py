Graph = {
    '5': ['3', '7'],
    '3': ['2', '4'],
    '7': ['8'],
    '2': [],
    '4': ['8'],
    '8': [],
}

Visited=[]
Found=False
Goal='4'


def DFS(Graph, Node, Visited):
    global Found
    if (Node==Goal):
        Found=True
        return
    if Node not in Visited:
        Visited.append(Node)
    for Neighbour in Graph[Node]:
        if Found==False:
            DFS(Graph,Neighbour,Visited)

DFS(Graph, '5', Visited)
print(Visited)