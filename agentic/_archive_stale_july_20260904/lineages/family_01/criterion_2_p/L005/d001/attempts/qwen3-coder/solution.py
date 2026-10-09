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
        edges.append((u, v))
        adj[u].append(v)
        adj[v].append(u)
    
    # Color graph with BFS/DFS - each component is bipartite or not
    color = [0] * (n + 1)  # 0: unvisited, 1: color A, 2: color B
    visited = [False] * (n + 1)
    
    def bfs(start):
        queue = deque()
        queue.append(start)
        color[start] = 1
        visited[start] = True
        
        while queue:
            node = queue.popleft()
            current_color = color[node]
            next_color = 3 - current_color  # flips 1->2, 2->1
            
            for neighbor in adj[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    color[neighbor] = next_color
                    queue.append(neighbor)
                elif color[neighbor] != next_color:
                    return False
        return True
    
    # Check all components
    for i in range(1, n + 1):
        if not visited[i]:
            if not bfs(i):
                print("NO")
                return
    
    # If we reach here, a valid 2-coloring exists
    # Map colors to states: color 1 -> state 1, color 2 -> state 2
    # This ensures all edges have product 1*2 = 2
    states = [0] * (n + 1)
    for i in range(1, n + 1):
        if color[i] == 1:
            states[i] = 1
        else:
            states[i] = 2
    
    print("YES")
    print(" ".join(map(str, states[1:])))

if __name__ == "__main__":
    main()