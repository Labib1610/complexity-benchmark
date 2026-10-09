import sys
from collections import defaultdict, deque

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    index = 2
    edges = []
    adj = [[] for _ in range(n + 1)]
    
    for _ in range(m):
        u = int(data[index])
        v = int(data[index + 1])
        index += 2
        edges.append((u, v))
        adj[u].append(v)
        adj[v].append(u)
    
    # If no constraints, assign all phase 1
    if m == 0:
        print("YES")
        print(" ".join(["1"] * n))
        return
    
    # Color the graph with 2 colors (1 and 2). Each edge represents that endpoints must have different colors.
    color = [0] * (n + 1)  # 0 means unvisited
    
    # Check each connected component
    for start in range(1, n + 1):
        if color[start] != 0:
            continue
        # BFS to check bipartiteness and assign colors
        queue = deque()
        queue.append(start)
        color[start] = 1  # Assign color 1 to the starting node
        
        while queue:
            node = queue.popleft()
            current_color = color[node]
            opposite_color = 3 - current_color  # flips 1->2 and 2->1
            
            for neighbor in adj[node]:
                if color[neighbor] == 0:
                    color[neighbor] = opposite_color
                    queue.append(neighbor)
                elif color[neighbor] == current_color:
                    print("NO")
                    return
    
    # If we reach here, the graph is bipartite.
    # Now we want the lexicographically smallest assignment.
    # That means we prefer to assign 1 to earlier processes if possible.
    # Since our coloring already ensures a valid assignment, and we started with color 1,
    # it's already the lexicographically smallest valid assignment.
    
    # But let's double-check by trying to flip the entire component colors to see if we get a lex smaller one.
    # Actually, since we're doing BFS and always assigning the first available color as 1, 
    # this already gives us the lex smallest assignment.
    
    # Just to make sure, we can reassign colors per component to ensure lex smallest:
    # But given our BFS approach starting from node 1, 2, ..., and always preferring color 1 first,
    # it should be fine.
    
    # Let's just output what we have:
    result = color[1:n+1]
    print("YES")
    print(" ".join(map(str, result)))

if __name__ == "__main__":
    main()