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
    
    adj = defaultdict(list)
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        adj[u].append(v)
        adj[v].append(u)
    
    color = [0] * (n + 1)  # 0: unvisited, 1: color 1, 2: color 2
    visited = [False] * (n + 1)
    
    def bfs(start):
        queue = deque()
        queue.append(start)
        color[start] = 1
        visited[start] = True
        
        while queue:
            u = queue.popleft()
            current_color = color[u]
            next_color = 3 - current_color  # flips 1->2, 2->1
            
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    color[v] = next_color
                    queue.append(v)
                elif color[v] != next_color:
                    return False
        return True
    
    for i in range(1, n + 1):
        if not visited[i] and adj[i]:  # Only process nodes with edges
            if not bfs(i):
                print("NO")
                return
    
    # For isolated nodes (not in any edge), assign color 1
    for i in range(1, n + 1):
        if color[i] == 0:
            color[i] = 1
    
    print("YES")
    print(" ".join(str(color[i]) for i in range(1, n + 1)))

if __name__ == "__main__":
    main()