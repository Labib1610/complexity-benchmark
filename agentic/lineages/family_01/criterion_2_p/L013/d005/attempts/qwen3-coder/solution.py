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
    
    adj = [[] for _ in range(n + 1)]
    edges = []
    
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        adj[u].append(v)
        adj[v].append(u)
        edges.append((u, v))
    
    # We need to check if the graph is bipartite and find a valid assignment
    # Let's define what compositions are allowed:
    # Rule 1: f(x) = -x
    # Rule 2: f(x) = 1/x
    # 
    # Compositions:
    # 1-1: f1(f1(x)) = f1(-x) = -(-x) = x  --> Not allowed
    # 1-2: f1(f2(x)) = f1(1/x) = -1/x     --> Allowed
    # 2-1: f2(f1(x)) = f2(-x) = 1/(-x) = -1/x  --> Allowed
    # 2-2: f2(f2(x)) = f2(1/x) = 1/(1/x) = x   --> Not allowed
    #
    # So, two nodes connected by an edge must have different rules.
    # This means we need a bipartite graph where each part gets the same rule.
    # But wait, both 1-2 and 2-1 give -1/x, so it's okay as long as the nodes have different rules.
    # Actually, let's recheck:
    # For link {u,v} to be stable, we need f_u(f_v(x)) = -1/x.
    # If s_u=1, s_v=2: f1(f2(x)) = f1(1/x) = -1/x  OK
    # If s_u=2, s_v=1: f2(f1(x)) = f2(-x) = -1/x   OK
    # If s_u=1, s_v=1: f1(f1(x)) = x               NOT OK
    # If s_u=2, s_v=2: f2(f2(x)) = x               NOT OK
    # So adjacent nodes must have different rules => Graph must be bipartite.
    
    color = [-1] * (n + 1)  # -1: unvisited, 0: group 0, 1: group 1
    visited = [False] * (n + 1)
    
    def bfs(start):
        queue = deque()
        queue.append(start)
        color[start] = 0
        visited[start] = True
        
        while queue:
            u = queue.popleft()
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    color[v] = 1 - color[u]
                    queue.append(v)
                elif color[v] == color[u]:
                    return False
        return True
    
    for i in range(1, n + 1):
        if not visited[i]:
            if not bfs(i):
                print("NO")
                return
    
    # If bipartition is possible, assign rules based on color to get lex smallest
    # Color 0 -> Rule 1, Color 1 -> Rule 2 to get lexicographically smallest
    result = []
    for i in range(1, n + 1):
        if color[i] == 0:
            result.append('1')
        else:
            result.append('2')
    
    print("YES")
    print(" ".join(result))

if __name__ == "__main__":
    main()