GRAPH = {
'A':['B','D','E'],
'B':['A','C','D'],
'C':['B','G'],
'D':['A','B','E','F'],
'E':['A','D'],
'F':['D'],
'G':['C']
}

visited = []
queue = ['','','','','','','']
front = 0
back = 0

current_vertex = 'A'
while len(GRAPH[current_vertex]) != 0:
    if not (current_vertex in visited):
        visited.append(current_vertex)
    for x in GRAPH[current_vertex]:
        if not (x in visited):
            queue[back] = x
            back += 1
            visited.append(x)
        GRAPH[current_vertex].remove(x)
    if front != back:
        current_vertex = queue[front]
        queue[front] = ''
        front += 1

for x in visited:
    print(x)
    
print(GRAPH)    

