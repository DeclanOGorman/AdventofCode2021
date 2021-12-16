#Life is too short to rewrite this myself - https://pypi.org/project/Dijkstar/
from dijkstar import Graph, find_path 

with open('./15/input_a.txt', 'r') as f:
    input = [list(map(int, a.strip())) for a in f]

graph = Graph()
d = len(input)
nodes = {(x,y) for x in range(d*5) for y in range(d*5)}
scaledinput = [a*5 for a in input*5]
for x in range(d*5): 
    for y in range(d*5):
        scaledinput[y][x] = (scaledinput[y][x] + int(x/d) + int(y/d) - 1) % 9 + 1

for n in nodes:
    if n[0] > 0: graph.add_edge(n, (n[0]-1,n[1]), scaledinput[n[0]-1][n[1]])
    if n[0] < d*5-1: graph.add_edge(n, (n[0]+1,n[1]), scaledinput[n[0]+1][n[1]])
    if n[1] > 0: graph.add_edge(n, (n[0],n[1]-1), scaledinput[n[0]][n[1]-1])
    if n[1] < d*5-1: graph.add_edge(n, (n[0],n[1]+1), scaledinput[n[0]][n[1]+1])

print(f'Part A: Shortest route cost to original end - {find_path(graph, (0,0), (d-1,d-1)).total_cost}') # test a = 40
print(f'Part B: Shortest route cost to x5 scaled end - {find_path(graph, (0,0), (d*5-1,d*5-1)).total_cost}') # test b = 315