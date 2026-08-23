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
    
    adj = defaultdict(list)
    edges = []
    
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        adj[u].append(v)
        adj[v].append(u)
        edges.append((u, v))
    
    # For each component, we'll do BFS and check bipartiteness with constraints
    # Each node can be value 1 or 2. 
    # If u-v is an edge, then one must be twice the other => (1,2) or (2,1)
    # So for each edge, the values must be (1,2) or (2,1)
    
    # This is like a 2-coloring where colors are 1 and 2, and adjacent nodes must have ratio 2
    # That means: if a node is colored 1, all neighbors must be 2
    #             if a node is colored 2, all neighbors must be 1
    # But wait, that's not right. The constraint is that one is twice the other.
    # So if a node is 1, neighbors must be 2
    # If a node is 2, neighbors must be 1
    # This IS just 2-coloring with colors 1 and 2!
    
    color = [0] * (n + 1)  # 0: unvisited, 1: color 1, 2: color 2
    visited = [False] * (n + 1)
    
    def bfs(start):
        queue = deque()
        queue.append(start)
        color[start] = 1  # Start with color 1
        visited[start] = True
        
        while queue:
            u = queue.popleft()
            c = color[u]
            next_c = 2 if c == 1 else 1
            
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    color[v] = next_c
                    queue.append(v)
                else:
                    # Check consistency
                    if color[v] != next_c:
                        return False
        return True
    
    # Check all components
    for i in range(1, n + 1):
        if not visited[i]:
            if not bfs(i):
                print("NO")
                return
    
    # Verify all edges satisfy the constraint
    for u, v in edges:
        c_u = color[u]
        c_v = color[v]
        if not ((c_u == 1 and c_v == 2) or (c_u == 2 and c_v == 1)):
            print("NO")
            return
    
    print("YES")
    print(" ".join(str(color[i]) for i in range(1, n + 1)))

if __name__ == "__main__":
    main()