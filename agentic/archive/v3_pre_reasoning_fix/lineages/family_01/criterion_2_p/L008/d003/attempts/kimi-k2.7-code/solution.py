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

    color = [-1] * n
    comp_id = [-1] * n
    comp_min = []
    cid = 0

    for i in range(n):
        if color[i] != -1:
            continue
        q = deque([i])
        color[i] = 0
        mn = i
        while q:
            u = q.popleft()
            comp_id[u] = cid
            if u < mn:
                mn = u
            for w in adj[u]:
                if color[w] == -1:
                    color[w] = color[u] ^ 1
                    q.append(w)
                elif color[w] == color[u]:
                    sys.stdout.write("NO")
                    return
        comp_min.append(mn)
        cid += 1

    ans = [0] * n
    for v in range(n):
        c = comp_id[v]
        if color[comp_min[c]] == 0:
            ans[v] = color[v] + 1
        else:
            ans[v] = 2 - color[v]

    sys.stdout.write("YES\n" + " ".join(map(str, ans)))

if __name__ == "__main__":
    solve()