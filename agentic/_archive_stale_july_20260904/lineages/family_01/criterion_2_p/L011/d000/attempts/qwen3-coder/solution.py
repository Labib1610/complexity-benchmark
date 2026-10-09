import sys
from collections import defaultdict, deque

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    # Graph representation: each variable can be 1 or 2
    # For each constraint x_u + x_v = 3:
    # if x_u = 1, then x_v = 2
    # if x_u = 2, then x_v = 1
    # This creates a bipartite graph structure
    
    adj = [[] for _ in range(n+1)]
    edges = []
    
    index = 2
    for _ in range(m):
        u = int(data[index])
        v = int(data[index+1])
        edges.append((u, v))
        adj[u].append(v)
        adj[v].append(u)
        index += 2
    
    # We need to assign values 1 or 2 to each variable such that:
    # for every edge (u,v), x_u + x_v = 3
    # That means if x_u=1 then x_v=2, and vice versa.
    # So this is essentially a 2-coloring (bipartite check) where color 0 maps to value 1, color 1 to value 2.
    
    color = [-1] * (n+1)  # -1: unvisited, 0: color 0, 1: color 1
    
    # Check each component
    for i in range(1, n+1):
        if color[i] == -1:
            # BFS to color this component
            queue = deque()
            queue.append(i)
            color[i] = 0
            
            while queue:
                node = queue.popleft()
                current_color = color[node]
                
                for neighbor in adj[node]:
                    if color[neighbor] == -1:
                        color[neighbor] = 1 - current_color
                        queue.append(neighbor)
                    elif color[neighbor] == current_color:
                        # Conflict: not bipartite
                        print("NO")
                        return
    
    # If we reach here, a valid assignment exists.
    # To get the lexicographically smallest vector:
    # Assign color 0 to 1, color 1 to 2
    result = []
    for i in range(1, n+1):
        if color[i] == 0:
            result.append('1')
        else:
            result.append('2')
    
    print("YES")
    print(' '.join(result))

if __name__ == "__main__":
    main()