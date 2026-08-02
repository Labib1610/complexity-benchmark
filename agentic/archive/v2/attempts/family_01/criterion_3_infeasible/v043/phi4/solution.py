import sys

def find_mutual_interference():
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    edges = [tuple(map(int, data[i:i+2])) for i in range(2, len(data), 2)]
    
    graph = {i: set() for i in range(1, n + 1)}
    
    for u, v in edges:
        graph[u].add(v)
        graph[v].add(u)
    
    for a in range(1, n + 1):
        neighbors_a = sorted(graph[a])
        for b_index in range(len(neighbors_a)):
            b = neighbors_a[b_index]
            if a < b:
                common_neighbors = graph[a] & graph[b]
                for c in common_neighbors:
                    if b < c:
                        print(a, b, c)
                        return