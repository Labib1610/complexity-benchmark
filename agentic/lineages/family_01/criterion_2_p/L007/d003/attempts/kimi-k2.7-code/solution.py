import sys
from collections import deque

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        if u == v:
            print("NO")
            return
        adj[u].append(v)
        adj[v].append(u)

    color = [-1] * n
    for i in range(n):
        if color[i] != -1:
            continue
        color[i] = 0
        q = deque([i])
        comp = []
        min_v = i
        while q:
            u = q.popleft()
            comp.append(u)
            if u < min_v:
                min_v = u
            for w in adj[u]:
                if color[w] == -1:
                    color[w] = color[u] ^ 1
                    q.append(w)
                elif color[w] == color[u]:
                    print("NO")
                    return
        if color[min_v] == 1:
            for u in comp:
                color[u] ^= 1

    out = [str(c + 1) for c in color]
    print("YES")
    print(" ".join(out))

if __name__ == "__main__":
    solve()