#3RD PROGRAM



from sys import maxsize
from itertools import permutations

def travellingSalesmanProblem(graph, s, V):
    vertex = []
    for i in range(V):
        if i != s:
            vertex.append(i)        
    min_path = maxsize
    next_permutation = permutations(vertex)

    for i in next_permutation:
        current_pathweight = 0
        k = s
        for j in i:
            current_pathweight += graph[k][j]
            k = j
            
        current_pathweight += graph[k][s]
        min_path = min(min_path, current_pathweight)
    return min_path, i

graph = [
    [0, 29, 20, 21],
    [29, 0, 15, 18],
    [20, 15, 0, 16],
    [21, 18, 16, 0]
]
s = 0
V = 4
cost, route = travellingSalesmanProblem(graph, s, V)

# optimal route
print("MIN COST ROUTE")
print(s, end="->")
for i in route:
    print(i, end="-> ")
print(s)

print("MIN COST")
print(cost)