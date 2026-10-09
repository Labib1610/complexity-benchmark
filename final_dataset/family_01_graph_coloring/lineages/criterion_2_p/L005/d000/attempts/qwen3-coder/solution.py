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
        adj[u].append(v)
        adj[v].append(u)
        edges.append((u, v))
    
    # Color nodes with BFS/DFS to check bipartiteness and get lexicographically smallest coloring
    color = {}
    
    # Process nodes in sorted order to ensure lexicographically smallest result
    nodes = sorted(adj.keys())
    visited = set()
    
    for start_node in range(1, n+1):
        if start_node not in visited:
            # BFS coloring
            queue = deque()
            queue.append(start_node)
            color[start_node] = 1
            visited.add(start_node)
            
            while queue:
                u = queue.popleft()
                current_color = color[u]
                next_color = 3 - current_color  # flips 1->2, 2->1
                
                for v in adj[u]:
                    if v not in visited:
                        visited.add(v)
                        color[v] = next_color
                        queue.append(v)
                    elif color[v] != next_color:
                        print("NO")
                        return
    
    # If we reach here, graph is bipartite
    # Assign default color 1 to isolated nodes (not in adj)
    result = []
    for i in range(1, n+1):
        if i in color:
            result.append(str(color[i]))
        else:
            result.append("1")
    
    print("YES")
    print(" ".join(result))

if __name__ == "__main__":
    main()