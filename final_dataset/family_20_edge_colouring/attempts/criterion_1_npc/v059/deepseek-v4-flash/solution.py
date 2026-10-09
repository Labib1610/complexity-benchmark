import sys
from collections import deque

def solve():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    edges = []
    adj = [[] for _ in range(n)]
    for idx in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        edges.append((u, v))
        adj[u].append((v, idx))
        adj[v].append((u, idx))
    
    # Check bipartiteness
    color = [-1] * n
    is_bipartite = True
    for i in range(n):
        if color[i] == -1:
            color[i] = 0
            q = deque([i])
            while q:
                u = q.popleft()
                for v, _ in adj[u]:
                    if color[v] == -1:
                        color[v] = color[u] ^ 1
                        q.append(v)
                    elif color[v] == color[u]:
                        is_bipartite = False
                        break
                if not is_bipartite:
                    break
        if not is_bipartite:
            break
    
    if not is_bipartite:
        print("NO")
        return
    
    # Now we have a bipartite 3-regular graph.
    # We'll find 3 perfect matchings.
    result = [0] * m
    left = [i for i in range(n) if color[i] == 0]
    right = [i for i in range(n) if color[i] == 1]
    
    # Build adjacency for matching
    for shift in range(1, 4):
        # Build bipartite graph for matching
        adj_match = [[] for _ in range(n)]
        for idx, (u, v) in enumerate(edges):
            if result[idx] == 0:
                if color[u] == 0:
                    adj_match[u].append(v)
                else:
                    adj_match[v].append(u)
        
        # Find perfect matching using DFS (Kuhn's algorithm)
        match_to = [-1] * n
        def dfs(u, visited):
            for v in adj_match[u]:
                if visited[v]:
                    continue
                visited[v] = True
                if match_to[v] == -1 or dfs(match_to[v], visited):
                    match_to[v] = u
                    return True
            return False
        
        for u in left:
            visited = [False] * n
            dfs(u, visited)
        
        # Assign shift to matched edges
        for v in right:
            u = match_to[v]
            if u != -1:
                # find edge index
                for idx, (a, b) in enumerate(edges):
                    if result[idx] == 0 and ((a == u and b == v) or (a == v and b == u)):
                        result[idx] = shift
                        break
    
    print("YES")
    print(" ".join(map(str, result)))

if __name__ == "__main__":
    solve()