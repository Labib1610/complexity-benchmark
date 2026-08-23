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
    
    # Color nodes with BFS (2-coloring for bipartite check)
    color = [-1] * (n + 1)  # -1: unvisited, 0: color 1, 1: color 2
    visited = [False] * (n + 1)
    
    def bfs(start):
        queue = deque()
        queue.append(start)
        color[start] = 0
        visited[start] = True
        
        while queue:
            node = queue.popleft()
            current_color = color[node]
            
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    color[neighbor] = 1 - current_color
                    queue.append(neighbor)
                elif color[neighbor] == current_color:
                    return False
        return True
    
    # Check all components
    for i in range(1, n + 1):
        if not visited[i] and graph[i]:  # Only process if it has edges
            if not bfs(i):
                print("NO")
                return
    
    # Handle isolated nodes (nodes with no constraints)
    for i in range(1, n + 1):
        if color[i] == -1:
            color[i] = 0  # Assign to shift 1
    
    # Convert colors to shifts (0->1, 1->2)
    shifts = []
    for i in range(1, n + 1):
        shifts.append(str(color[i] + 1))
    
    print("YES")
    print(" ".join(shifts))

if __name__ == "__main__":
    main()