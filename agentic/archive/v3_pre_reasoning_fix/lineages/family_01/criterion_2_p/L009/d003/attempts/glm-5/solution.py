import sys
from collections import deque

def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(data[idx]); idx += 1
    m = int(data[idx]); idx += 1
    
    adj = [[] for _ in range(n+1)]
    for _ in range(m):
        u = int(data[idx]); idx += 1
        v = int(data[idx]); idx += 1
        adj[u].append(v)
        adj[v].append(u)
    
    color = [0] * (n+1)
    
    for start in range(1, n+1):
        if color[start] != 0:
            continue
        success = False
        for try_color in (1, 2):
            color[start] = try_color
            q = deque([start])
            ok = True
            changed = [start]
            while q:
                u = q.popleft()
                for w in adj[u]:
                    if color[w] == 0:
                        color[w] = 3 - color[u]
                        changed.append(w)
                        q.append(w)
                    elif color[w] == color[u]:
                        ok = False
                        break
                if not ok:
                    break
            if ok:
                success = True
                break
            else:
                for node in changed:
                    color[node] = 0
        if not success:
            print("NO")
            return
    
    print("YES")
    print(' '.join(str(color[i]) for i in range(1, n+1)))

main()