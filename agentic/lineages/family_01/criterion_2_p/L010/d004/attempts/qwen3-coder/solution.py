import sys
from collections import defaultdict, deque

def read_ints():
    return list(map(int, sys.stdin.readline().split()))

def main():
    n, m = read_ints()
    
    if m == 0:
        print("YES")
        print(" ".join(["1"] * n))
        return
    
    # Build graph
    graph = defaultdict(list)
    edges = []
    for _ in range(m):
        u, v = read_ints()
        u -= 1  # Convert to 0-indexed
        v -= 1
        edges.append((u, v))
        graph[u].append(v)
    
    # For each edge (u,v), the constraint is that 10*s[u] + s[v] ≡ 0 (mod 3)
    # This means s[u] + s[v] ≡ 0 (mod 3) since 10 ≡ 1 (mod 3)
    # So we need s[u] + s[v] ≡ 0 (mod 3)
    # Since s[i] ∈ {1,2}, we have s[u] + s[v] ∈ {2,3,4}
    # Only sum=3 satisfies the condition, so we need s[u] ≠ s[v]
    
    # This is a 2-coloring problem. Each edge represents that the two nodes must have different colors.
    
    # Create adjacency list for the constraint graph
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    
    # Try 2-coloring with BFS
    color = [-1] * n  # -1: unvisited, 0: color 1, 1: color 2
    
    for i in range(n):
        if color[i] == -1:
            queue = deque([i])
            color[i] = 0  # Start with color 0
            
            while queue:
                node = queue.popleft()
                current_color = color[node]
                
                for neighbor in adj[node]:
                    if color[neighbor] == -1:
                        color[neighbor] = 1 - current_color
                        queue.append(neighbor)
                    elif color[neighbor] == current_color:
                        print("NO")
                        return
    
    # If we reach here, a valid coloring exists
    # We want the lexicographically smallest assignment
    # Color 0 -> mode 1, Color 1 -> mode 2
    result = []
    for i in range(n):
        if color[i] == 0:
            result.append("1")
        else:
            result.append("2")
    
    print("YES")
    print(" ".join(result))

if __name__ == "__main__":
    main()