import sys
from collections import defaultdict, deque

def main():
    import sys
    sys.setrecursionlimit(1 << 25)
    
    n, m = map(int, sys.stdin.readline().split())
    
    if m == 0:
        print("YES")
        print(" ".join(["1"] * n))
        return
    
    edges = []
    adj = [[] for _ in range(n + 1)]
    
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        edges.append((u, v))
        adj[u].append(v)
        adj[v].append(u)
    
    # For each edge (u,v), R_{u,v} = s_u^2 + s_u*s_v + s_v^2
    # If s_u = 1, s_v = 1: R = 1 + 1 + 1 = 3
    # If s_u = 1, s_v = 2: R = 1 + 2 + 4 = 7
    # If s_u = 2, s_v = 1: R = 4 + 2 + 1 = 7
    # If s_u = 2, s_v = 2: R = 4 + 4 + 4 = 12
    
    # We want the product of all R to be 7^m
    # So each R must be 7 => each edge must have (1,2) or (2,1)
    # This is equivalent to 2-coloring the graph: bipartite check
    
    color = [-1] * (n + 1)
    visited = [False] * (n + 1)
    
    def bfs(start):
        queue = deque()
        queue.append(start)
        color[start] = 0
        while queue:
            u = queue.popleft()
            if visited[u]:
                continue
            visited[u] = True
            for v in adj[u]:
                if color[v] == -1:
                    color[v] = color[u] ^ 1
                    queue.append(v)
                elif color[v] == color[u]:
                    return False
        return True
    
    for i in range(1, n + 1):
        if not visited[i] and adj[i]:
            if not bfs(i):
                print("NO")
                return
    
    # If bipartite, assign 1 to color 0, 2 to color 1
    # To get lexicographically smallest, we need to ensure that
    # among nodes with same component, we follow the coloring
    # But also, for isolated nodes (not in any edge), we can assign 1 (to keep lex smallest)
    
    result = [1] * (n + 1)
    
    for i in range(1, n + 1):
        if color[i] != -1:
            if color[i] == 1:
                result[i] = 2
    
    # Verify the solution
    product = 1
    for u, v in edges:
        su = result[u]
        sv = result[v]
        R = su*su + su*sv + sv*sv
        if R != 7:
            print("NO")
            return
    
    print("YES")
    print(" ".join(map(str, result[1:])))

if __name__ == "__main__":
    main()