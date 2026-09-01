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
    edges = []
    
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        adj[u].append(v)
        adj[v].append(u)
        edges.append((u, v))
    
    color = [0] * (n + 1)
    visited = [False] * (n + 1)
    
    for start in range(1, n + 1):
        if visited[start]:
            continue
            
        queue = deque()
        queue.append(start)
        color[start] = 1
        visited[start] = True
        
        while queue:
            u = queue.popleft()
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    color[v] = 3 - color[u]
                    queue.append(v)
                elif color[v] == color[u]:
                    print("NO")
                    return
    
    print("YES")
    res = []
    for i in range(1, n + 1):
        if color[i] == 1:
            res.append("1")
        else:
            res.append("2")
    print(" ".join(res))

if __name__ == "__main__":
    main()