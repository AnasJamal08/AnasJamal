puzzle=[[2,6,3],[1,8,4],[5,7,0]]

goal = [[1,2,3],[4,5,6],[7,8,0]]

def misplaced(goal, puzzle):
    m_count = 0
    for x in range(3):
        for y in range(3):
            if puzzle[x][y] != goal[x][y]:
                m_count += 1
    return m_count

print(misplaced(goal,puzzle))

heuristic=list()
def heu(goal,puzzle):
    for g_x in range(3):
        for g_y in range(3):
            for x in range(3):
                for y in range(3):
                    if puzzle[g_x][g_y]==goal[x][y]:
                        temp_x=x
                        temp_y=y
            dis=abs(temp_x-g_x)+abs(temp_y-g_y)
            heuristic.append(dis)
    sum=0
    for i in heuristic:
        sum+=i
    return sum



print(heu(goal,puzzle))
print(heuristic)

