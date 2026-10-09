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
    graph = defaultdict(list)
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        graph[u].append(v)
        graph[v].append(u)
    
    # Color array: 0 = unvisited, 1 = color 1, 2 = color 2
    color = [0] * (n + 1)
    
    # Check if bipartite using BFS
    def bfs(start):
        queue = deque()
        queue.append(start)
        color[start] = 1
        
        while queue:
            node = queue.popleft()
            current_color = color[node]
            next_color = 2 if current_color == 1 else 1
            
            for neighbor in graph[node]:
                if color[neighbor] == 0:
                    color[neighbor] = next_color
                    queue.append(neighbor)
                elif color[neighbor] == current_color:
                    return False
        return True
    
    # Process each connected component
    for i in range(1, n + 1):
        if color[i] == 0 and graph[i]:
            if not bfs(i):
                print("NO")
                return
    
    # Assign default color 1 to isolated nodes (nodes with no edges)
    for i in range(1, n + 1):
        if color[i] == 0:
            color[i] = 1
    
    # Output result
    print("YES")
    print(" ".join(str(color[i]) for i in range(1, n + 1)))

if __name__ == "__main__":
    main()