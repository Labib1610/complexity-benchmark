import sys
from collections import defaultdict, deque

def main():
    import sys
    sys.setrecursionlimit(1 << 25)
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    if m == 0:
        print("YES")
        print(" ".join(["1"] * n))
        return
    
    edges = []
    adj = [[] for _ in range(n + 1)]
    degree = [0] * (n + 1)
    
    index = 2
    for _ in range(m):
        u = int(data[index])
        v = int(data[index + 1])
        index += 2
        edges.append((u, v))
        adj[u].append(v)
        adj[v].append(u)
        degree[u] += 1
        degree[v] += 1
    
    # Check if the graph is bipartite
    color = [-1] * (n + 1)
    visited = [False] * (n + 1)
    
    def bfs(start):
        queue = deque()
        queue.append(start)
        color[start] = 0
        while queue:
            u = queue.popleft()
            visited[u] = True
            for v in adj[u]:
                if color[v] == -1:
                    color[v] = 1 - color[u]
                    queue.append(v)
                elif color[v] == color[u]:
                    return False
        return True
    
    for i in range(1, n + 1):
        if not visited[i] and adj[i]:
            if not bfs(i):
                print("NO")
                return
    
    # Assign default colors to isolated nodes
    for i in range(1, n + 1):
        if color[i] == -1:
            color[i] = 0
    
    # Count edges crossing between the two partitions
    cross_edges = 0
    for u, v in edges:
        if color[u] != color[v]:
            cross_edges += 1
    
    # Check condition: k = m (all edges must cross)
    if cross_edges != m:
        print("NO")
        return
    
    # Check condition: sum of degrees in each partition equals 2m
    sum_P1 = sum(degree[i] for i in range(1, n + 1) if color[i] == 0)
    sum_P2 = sum(degree[i] for i in range(1, n + 1) if color[i] == 1)
    
    if sum_P1 + sum_P2 != 2 * m:
        print("NO")
        return
    
    # Now we need to find the lexicographically smallest valid assignment
    # Since we already have a valid bipartition, we just need to choose which side is 1 and which is 2
    # We try both assignments and pick the lex smaller one
    
    # Assignment 1: color 0 -> 1, color 1 -> 2
    res1 = [1 if color[i] == 0 else 2 for i in range(1, n + 1)]
    
    # Assignment 2: color 0 -> 2, color 1 -> 1
    res2 = [2 if color[i] == 0 else 1 for i in range(1, n + 1)]
    
    # Choose lexicographically smaller
    if res1 <= res2:
        result = res1
    else:
        result = res2
    
    print("YES")
    print(" ".join(map(str, result)))

if __name__ == "__main__":
    main()