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
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        adj[u].append(v)
        adj[v].append(u)
    
    # Color array: 0 = unvisited, 1 and 2 are the two colors
    color = [0] * (n + 1)
    
    # Check if bipartite using BFS
    def bfs(start):
        queue = deque()
        queue.append(start)
        color[start] = 1
        while queue:
            u = queue.popleft()
            current_color = color[u]
            next_color = 3 - current_color  # flips 1->2 and 2->1
            for v in adj[u]:
                if color[v] == 0:
                    color[v] = next_color
                    queue.append(v)
                elif color[v] == current_color:
                    return False
        return True
    
    # Process each connected component
    for i in range(1, n + 1):
        if color[i] == 0:
            if not bfs(i):
                print("NO")
                return
    
    print("YES")
    # Ensure lexicographically smallest: node 1 gets color 1 if possible
    # Since we're doing BFS starting from node 1, and we start with color 1,
    # this should already be satisfied. But let's verify and adjust if needed.
    # Actually, our BFS ensures that the component containing node 1 will have
    # node 1 colored 1, which is what we want for lex smallest.
    result = []
    for i in range(1, n + 1):
        if color[i] == 0:
            result.append('1')
        else:
            result.append(str(color[i]))
    print(" ".join(result))

if __name__ == "__main__":
    main()