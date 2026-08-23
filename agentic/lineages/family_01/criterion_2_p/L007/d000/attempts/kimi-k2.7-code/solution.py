import sys
from collections import deque

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u].append(v)
        adj[v].append(u)

    color = [-1] * (n + 1)
    comp = []

    for start in range(1, n + 1):
        if color[start] != -1:
            continue
        q = deque([start])
        color[start] = 0
        comp.clear()
        comp.append(start)
        min_v = start
        while q:
            u = q.popleft()
            if u < min_v:
                min_v = u
            for w in adj[u]:
                if color[w] == -1:
                    color[w] = color[u] ^ 1
                    q.append(w)
                    comp.append(w)
                elif color[w] == color[u]:
                    sys.stdout.write("NO")
                    return
        if color[min_v] != 0:
            for v in comp:
                color[v] ^= 1

    out = ['YES']
    out.append(' '.join(str(color[i] + 1) for i in range(1, n + 1)))
    sys.stdout.write('\n'.join(out))

if __name__ == "__main__":
    solve()