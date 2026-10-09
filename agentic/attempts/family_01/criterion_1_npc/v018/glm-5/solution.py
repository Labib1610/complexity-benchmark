import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    m = int(data[1])
    adj = [0] * (n + 1)
    idx = 2
    for _ in range(m):
        u = int(data[idx]); v = int(data[idx+1]); idx += 2
        adj[u] |= 1 << v
        adj[v] |= 1 << u
    
    color = [0] * (n + 1)
    
    def dfs(u):
        for c in (1, 2, 3):
            if (adj[u] & color[c]) == 0:
                color[c] |= 1 << u
                color[0] |= c << (2 * (u - 1))
                ok = True
                v = u + 1
                while v <= n and ok:
                    if color[0] >> (2 * (v - 1)) & 3 == 0:
                        ok = dfs(v)
                    v += 1
                if ok:
                    return True
                color[c] &= ~(1 << u)
                color[0] &= ~(3 << (2 * (u - 1)))
        return False
    
    if not dfs(1):
        print("NO")
    else:
        out = []
        for i in range(1, n + 1):
            out.append(str((color[0] >> (2 * (i - 1))) & 3))
        print("YES")
        print(" ".join(out))

solve()