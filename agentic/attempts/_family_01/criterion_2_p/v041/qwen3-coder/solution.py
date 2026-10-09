import sys
from collections import defaultdict, deque

def main():
    import sys
    sys.setrecursionlimit(1 << 25)
    
    n, m = map(int, sys.stdin.readline().split())
    
    # Build adjacency list
    adj = defaultdict(list)
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        adj[u].append(v)
        adj[v].append(u)
    
    # Color array: 0 = unvisited, 1 = color 1, 2 = color 2
    color = [0] * (n + 1)
    
    # Check if bipartite using BFS for each component
    for start in range(1, n + 1):
        if color[start] == 0:
            queue = deque()
            queue.append(start)
            color[start] = 1  # Assign color 1 to the starting node
            
            while queue:
                u = queue.popleft()
                current_color = color[u]
                neighbor_color = 3 - current_color  # flips 1->2 and 2->1
                
                for v in adj[u]:
                    if color[v] == 0:
                        color[v] = neighbor_color
                        queue.append(v)
                    elif color[v] != neighbor_color:
                        print("NO")
                        return
    
    # If we reach here, the graph is bipartite
    print("YES")
    result = []
    for i in range(1, n + 1):
        if color[i] == 0:
            result.append('1')
        else:
            result.append(str(color[i]))
    print(' '.join(result))

if __name__ == "__main__":
    main()