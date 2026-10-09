import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)
    q = int(next(it))
    t = int(next(it))
    
    adj = [[] for _ in range(2 * q + 1)]
    edges = []
    
    for _ in range(t):
        a = int(next(it))
        b = int(next(it))
        edges.append((a, b))
        adj[a].append(b)
        adj[b].append(a)
    
    match = [0] * (2 * q + 1)
    visited = [False] * (2 * q + 1)
    parent = [0] * (2 * q + 1)
    
    def bfs():
        queue = deque()
        for u in range(1, q + 1):
            if match[u] == 0:
                visited[u] = True
                parent[u] = 0
                queue.append(u)
            else:
                visited[u] = False
                parent[u] = 0
        
        found = False
        while queue:
            u = queue.popleft()
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    parent[v] = u
                    if match[v] == 0:
                        found = True
                    else:
                        u2 = match[v]
                        if not visited[u2]:
                            visited[u2] = True
                            parent[u2] = v
                            queue.append(u2)
        return found
    
    def dfs(u):
        for v in adj[u]:
            if not visited[v]:
                visited[v] = True
                if match[v] == 0 or dfs(match[v]):
                    match[u] = v
                    match[v] = u
                    return True
        return False
    
    # Hopcroft-Karp algorithm
    matching = 0
    while bfs():
        visited = [False] * (2 * q + 1)
        for u in range(1, q + 1):
            if match[u] == 0:
                if dfs(u):
                    matching += 1
    
    if matching == q:
        print("YES")
        for u in range(1, q + 1):
            print(u, match[u])
    else:
        print("NO")

if __name__ == "__main__":
    solve()