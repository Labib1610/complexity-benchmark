import sys
from collections import deque

def solve():
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
        adj[u].append(v)
        adj[v].append(u)

    parity = [-1] * n
    comp = [-1] * n
    comp_min = []

    for i in range(n):
        if parity[i] != -1:
            continue
        q = deque([i])
        parity[i] = 0
        comp[i] = len(comp_min)
        mn = i
        while q:
            u = q.popleft()
            if u < mn:
                mn = u
            for w in adj[u]:
                if parity[w] == -1:
                    parity[w] = parity[u] ^ 1
                    comp[w] = comp[i]
                    q.append(w)
                elif parity[w] == parity[u]:
                    sys.stdout.write("NO")
                    return
        comp_min.append(mn)

    out = ['YES']
    res = []
    for i in range(n):
        c = (parity[i] ^ parity[comp_min[comp[i]]]) + 1
        res.append(str(c))
    out.append(' '.join(res))
    sys.stdout.write('\n'.join(out))

if __name__ == '__main__':
    solve()