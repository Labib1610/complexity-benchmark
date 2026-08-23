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
    
    # Build graph
    adj = defaultdict(list)
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        adj[u].append(v)
        adj[v].append(u)
    
    # Color coding: 1 and 2 are the colors (planes)
    # We need product of colors to be 2 => so colors must be (1,2) or (2,1)
    color = [0] * (n + 1)  # 0 means unvisited
    
    # Check if bipartite
    visited = [False] * (n + 1)
    
    for start in range(1, n + 1):
        if visited[start]:
            continue
            
        # BFS to check bipartiteness and assign colors
        queue = deque()
        queue.append(start)
        color[start] = 1
        visited[start] = True
        
        while queue:
            u = queue.popleft()
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    color[v] = 3 - color[u]  # Flip color: 1->2, 2->1
                    queue.append(v)
                else:
                    # Check if the constraint is satisfied
                    if color[u] * color[v] != 2:
                        print("NO")
                        return
    
    # If we reach here, a valid assignment exists
    # Ensure lexicographically smallest: prefer color 1 for earlier nodes
    # But we already did that with our BFS starting with color 1
    
    # Reconstruct result
    result = []
    for i in range(1, n + 1):
        if color[i] == 0:
            result.append('1')  # Isolated node, assign 1
        else:
            result.append(str(color[i]))
            
    print("YES")
    print(" ".join(result))

if __name__ == "__main__":
    main()