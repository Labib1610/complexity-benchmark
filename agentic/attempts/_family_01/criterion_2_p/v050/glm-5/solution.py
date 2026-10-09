import sys
from collections import deque

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    n = int(data[0])
    m = int(data[1])
    adj = [[] for _ in range(n + 1)]
    idx = 2
    for _ in range(m):
        u = int(data[idx]); v = int(data[idx+1])
        idx += 2
        adj[u].append(v)
        adj[v].append(u)
    
    color = [0] * (n + 1)
    possible = True
    
    for i in range(1, n + 1):
        if color[i] == 0:
            color[i] = 1
            q = deque([i])
            while q:
                u = q.popleft()
                for w in adj[u]:
                    if color[w] == 0:
                        color[w] = 3 - color[u]
                        q.append(w)
                    elif color[w] == color[u]:
                        possible = False
                        break
                if not possible:
                    break
        if not possible:
            break
    
    if not possible:
        sys.stdout.write("NO")
    else:
        out = "YES\n" + " ".join(str(color[i]) for i in range(1, n + 1))
        sys.stdout.write(out)

solve()