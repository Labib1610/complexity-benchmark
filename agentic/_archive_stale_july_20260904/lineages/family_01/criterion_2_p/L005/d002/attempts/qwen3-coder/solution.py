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
    
    # Build adjacency list
    adj = defaultdict(list)
    edges = []
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        u -= 1
        v -= 1
        adj[u].append(v)
        adj[v].append(u)
        edges.append((u, v))
    
    # For each component, we need to 2-color it with constraints
    # If nodes u and v are connected, then tier[u] + tier[v] = 3
    # So tier[v] = 3 - tier[u]
    # This means in a component, fixing one node's tier fixes all others
    # We model this as a 2-SAT problem or bipartite check
    
    color = [-1] * n  # -1: unvisited, 0: tier 1, 1: tier 2
    result = [0] * n  # 0 means tier 1, 1 means tier 2
    
    # For lex smallest, we try to assign tier 1 (color 0) to nodes with smaller indices first
    
    visited = [False] * n
    
    for i in range(n):
        if visited[i]:
            continue
        # BFS to check bipartiteness and assign tiers
        queue = deque()
        queue.append(i)
        # Try assigning tier 1 (0) to node i first for lex smallest
        color[i] = 0
        visited[i] = True
        
        while queue:
            u = queue.popleft()
            c_u = color[u]
            tier_u = c_u + 1  # tier is 1 or 2
            
            for v in adj[u]:
                required_tier_v = 3 - tier_u
                required_color_v = required_tier_v - 1
                
                if not visited[v]:
                    visited[v] = True
                    color[v] = required_color_v
                    queue.append(v)
                else:
                    # Check consistency
                    if color[v] != required_color_v:
                        print("NO")
                        return
    
    # If we reach here, a valid assignment exists
    print("YES")
    ans = []
    for i in range(n):
        if color[i] == 0:
            ans.append("1")
        else:
            ans.append("2")
    print(" ".join(ans))

if __name__ == "__main__":
    main()