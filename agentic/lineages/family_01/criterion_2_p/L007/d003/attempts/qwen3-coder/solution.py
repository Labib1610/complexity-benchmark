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
        u -= 1
        v -= 1
        adj[u].append(v)
        adj[v].append(u)
        edges.append((u, v))
    
    color = [-1] * n
    impossible = False
    
    for start in range(n):
        if color[start] == -1:
            queue = deque()
            queue.append(start)
            color[start] = 0
            
            while queue:
                u = queue.popleft()
                for v in adj[u]:
                    if color[v] == -1:
                        color[u] = 1 - color[u] if color[u] != -1 else 0
                        color[v] = 1 - color[u]
                        queue.append(v)
                    elif color[v] == color[u]:
                        impossible = True
                        break
                if impossible:
                    break
        if impossible:
            break
    
    if impossible:
        print("NO")
    else:
        print("YES")
        result = []
        for i in range(n):
            if color[i] == 0:
                result.append("1")
            else:
                result.append("2")
        print(" ".join(result))

if __name__ == "__main__":
    main()