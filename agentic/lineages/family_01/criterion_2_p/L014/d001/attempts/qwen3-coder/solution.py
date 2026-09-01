import sys
from collections import defaultdict, deque

def main():
    import sys
    sys.setrecursionlimit(1 << 25)
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    if m == 0:
        # No constraints, assign all to 1 (lexicographically smallest)
        print("YES")
        print(" ".join(["1"] * n))
        return

    # Build graph
    adj = defaultdict(list)
    edges = []
    index = 2
    for _ in range(m):
        u = int(data[index]) - 1  # Convert to 0-based indexing
        v = int(data[index+1]) - 1
        index += 2
        adj[u].append(v)
        adj[v].append(u)
        edges.append((u, v))
    
    # Color array: -1 unvisited, 0 color 1, 1 color 2
    color = [-1] * n
    
    # Check bipartiteness for each component
    for start in range(n):
        if color[start] == -1:
            queue = deque()
            queue.append(start)
            color[start] = 0  # Assign color 1 (0 in our mapping)
            
            while queue:
                u = queue.popleft()
                current_color = color[u]
                next_color = 1 - current_color
                
                for v in adj[u]:
                    if color[v] == -1:
                        color[v] = next_color
                        queue.append(v)
                    elif color[v] != next_color:
                        print("NO")
                        return
    
    # If bipartite, construct the lex smallest solution
    result = []
    for i in range(n):
        if color[i] == 0:
            result.append('1')
        else:
            result.append('2')
    
    print("YES")
    print(" ".join(result))

if __name__ == "__main__":
    main()