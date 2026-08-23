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
    adj = defaultdict(list)
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        adj[u].append(v)
        adj[v].append(u)
    
    # Color array: 0 means unvisited, 1 and 2 are the two colors
    color = [0] * (n + 1)
    
    # Check if bipartite using BFS and assign lexicographically smallest coloring
    for start in range(1, n + 1):
        if color[start] == 0:
            # Start BFS with color 1 for the first node
            queue = deque()
            queue.append((start, 1))
            color[start] = 1
            
            while queue:
                node, c = queue.popleft()
                next_c = 3 - c  # flips 1->2 and 2->1
                
                for neighbor in adj[node]:
                    if color[neighbor] == 0:
                        color[neighbor] = next_c
                        queue.append((neighbor, next_c))
                    elif color[neighbor] == c:
                        print("NO")
                        return
    
    # If we reach here, it's bipartite
    print("YES")
    print(" ".join(str(color[i]) for i in range(1, n + 1)))

if __name__ == "__main__":
    main()