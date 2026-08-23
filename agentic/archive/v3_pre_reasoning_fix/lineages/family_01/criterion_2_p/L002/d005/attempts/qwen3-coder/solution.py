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
        adj[u].append(v)
        adj[v].append(u)
        edges.append((u, v))
    
    # Color array: 0 means unvisited, 1 and 2 are the two colors
    color = [0] * (n + 1)
    visited = [False] * (n + 1)
    
    # Check if bipartite using BFS
    def bfs(start):
        queue = deque()
        queue.append(start)
        color[start] = 1
        visited[start] = True
        
        while queue:
            node = queue.popleft()
            current_color = color[node]
            next_color = 3 - current_color  # flips 1->2 and 2->1
            
            for neighbor in adj[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    color[neighbor] = next_color
                    queue.append(neighbor)
                elif color[neighbor] != next_color:
                    return False
        return True
    
    # Process each connected component
    for i in range(1, n + 1):
        if not visited[i]:
            if not bfs(i):
                print("NO")
                return
    
    # Verify all edges satisfy XOR condition
    for u, v in edges:
        if (color[u] ^ color[v]) != 3:
            print("NO")
            return
    
    # If we reach here, a valid assignment exists
    # Ensure lexicographically smallest: we want color[1] = 1 if possible
    # Since valid colorings are complements, choose the one starting with 1
    if color[1] == 2:
        # Flip all colors
        for i in range(1, n + 1):
            color[i] = 3 - color[i]
    
    print("YES")
    print(" ".join(str(color[i]) for i in range(1, n + 1)))

if __name__ == "__main__":
    main()