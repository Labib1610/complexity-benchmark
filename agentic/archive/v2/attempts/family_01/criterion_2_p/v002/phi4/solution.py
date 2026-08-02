import sys
input = sys.stdin.read
from collections import defaultdict

def solve():
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    edges = []
    index = 2
    for _ in range(m):
        u = int(data[index])
        v = int(data[index + 1])
        edges.append((u, v))
        index += 2
    
    if n == 1:
        print("YES")
        print(1)
        return
    
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    color = [-1] * (n + 1)
    
    def dfs(node, c):
        if color[node] != -1:
            return color[node] == c
        color[node] = c
        for neighbor in graph[node]:
            if not dfs(neighbor, 3 - c):
                return False
        return True
    
    for i in range(1, n + 1):
        if color[i] == -1:
            if not dfs(i, 1):
                print("NO")
                return
    
    result = [color[i] for i in range(1, n + 1)]
    
    print("YES")
    print(' '.join(map(str, result)))

solve()