import sys

def prim(graph, V):
    selected = [False] * V
    selected[0] = True

    for _ in range(V - 1):
        min_edge = sys.maxsize
        x = y = 0

        for i in range(V):
            if selected[i]:
                for j in range(V):
                    if not selected[j] and graph[i][j]:
                        if min_edge > graph[i][j]:
                            min_edge = graph[i][j]
                            x, y = i, j

        print(f"{x} - {y} : {graph[x][y]}")
        selected[y] = True

# Example graph (Adjacency Matrix)
graph = [
    [0, 2, 0, 6, 0],
    [2, 0, 3, 8, 5],
    [0, 3, 0, 0, 7],
    [6, 8, 0, 0, 9],
    [0, 5, 7, 9, 0]
]

prim(graph, 5)