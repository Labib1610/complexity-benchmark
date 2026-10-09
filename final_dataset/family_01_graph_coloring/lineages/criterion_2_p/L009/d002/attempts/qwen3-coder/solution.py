import sys
from collections import defaultdict, deque

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    if m == 0:
        print("YES")
        print(" ".join(["1"] * n))
        return
    
    # Build adjacency list
    adj = defaultdict(list)
    edges = []
    index = 2
    for _ in range(m):
        u = int(data[index]) - 1  # Convert to 0-indexed
        v = int(data[index+1]) - 1
        adj[u].append(v)
        adj[v].append(u)
        edges.append((u, v))
        index += 2
    
    # The condition is 3xy = 2(x + y)
    # Let's check which combinations of (x,y) satisfy this:
    # x=1, y=1: 3*1*1 = 3, 2*(1+1) = 4 → 3 ≠ 4
    # x=1, y=2: 3*1*2 = 6, 2*(1+2) = 6 → 6 = 6 ✓
    # x=2, y=1: 3*2*1 = 6, 2*(2+1) = 6 → 6 = 6 ✓
    # x=2, y=2: 3*2*2 = 12, 2*(2+2) = 8 → 12 ≠ 8
    # So only (1,2) and (2,1) are allowed. This means neighbors must have different values.
    # This is a bipartite graph check.
    
    # Color array: -1 unvisited, 0 and 1 are the two colors (representing mode 1 and 2)
    color = [-1] * n
    
    # Check if the graph is bipartite
    def is_bipartite():
        for start in range(n):
            if color[start] == -1:
                queue = deque()
                queue.append(start)
                color[start] = 0  # Start with color 0
                
                while queue:
                    node = queue.popleft()
                    current_color = color[node]
                    next_color = 1 - current_color
                    
                    for neighbor in adj[node]:
                        if color[neighbor] == -1:
                            color[neighbor] = next_color
                            queue.append(neighbor)
                        elif color[neighbor] != next_color:
                            return False
        return True
    
    if not is_bipartite():
        print("NO")
        return
    
    # If bipartite, construct the lexicographically smallest solution
    # We want mode 1 (which corresponds to color 0) as much as possible
    result = []
    for c in color:
        if c == 0:
            result.append('1')
        else:
            result.append('2')
    
    print("YES")
    print(" ".join(result))

if __name__ == "__main__":
    main()