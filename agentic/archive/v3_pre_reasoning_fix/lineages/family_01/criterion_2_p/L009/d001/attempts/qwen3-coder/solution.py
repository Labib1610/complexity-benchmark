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
    
    edges = []
    index = 2
    for _ in range(m):
        u = int(data[index]) - 1
        v = int(data[index+1]) - 1
        edges.append((u, v))
        index += 2
    
    # Build adjacency list
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    
    # Color array: 0 means unvisited, 1 and 2 are the two colors
    color = [0] * n
    visited = [False] * n
    
    # Check each component
    for i in range(n):
        if not visited[i]:
            # BFS to check bipartiteness and assign lex smallest coloring
            queue = deque()
            queue.append(i)
            color[i] = 1
            visited[i] = True
            
            while queue:
                u = queue.popleft()
                current_color = color[u]
                next_color = 3 - current_color  # if current is 1, next is 2; if current is 2, next is 1
                
                for v in adj[u]:
                    if not visited[v]:
                        visited[v] = True
                        color[v] = next_color
                        queue.append(v)
                    elif color[v] != next_color:
                        print("NO")
                        return
    
    # If we reach here, a valid assignment exists
    # We need the lexicographically smallest one
    # Since we started with color 1 for the first node in each component,
    # and followed the constraints, this should already be lex smallest
    # But we can double-check by ensuring that for each component,
    # the first node (in order) is colored 1.
    
    # Actually, our BFS ensures that the coloring follows the constraints
    # and starts with 1 for the first node encountered in each component.
    # This gives us the lex smallest valid assignment.
    
    print("YES")
    result = []
    for c in color:
        result.append(str(c))
    print(" ".join(result))

if __name__ == "__main__":
    main()