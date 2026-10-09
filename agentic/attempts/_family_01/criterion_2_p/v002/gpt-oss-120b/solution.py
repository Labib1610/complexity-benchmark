import sys
from collections import deque

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(it)); v = int(next(it))
        adj[u].append(v)
        adj[v].append(u)

    colour = [-1] * (n + 1)          # provisional 0/1
    answer = [0] * (n + 1)           # final 1/2

    for start in range(1, n + 1):
        if colour[start] != -1:
            continue
        # start new component
        q = deque([start])
        colour[start] = 0
        comp = [start]
        ok = True
        while q:
            u = q.popleft()
            cu = colour[u]
            for v in adj[u]:
                if colour[v] == -1:
                    colour[v] = cu ^ 1
                    q.append(v)
                    comp.append(v)
                elif colour[v] == cu:
                    # not bipartite
                    print("NO")
                    return
        # decide orientation
        vmin = min(comp)
        need_flip = colour[vmin]          # 0 -> keep, 1 -> flip
        for v in comp:
            answer[v] = 1 + (colour[v] ^ need_flip)

    # all components processed, graph bipartite
    out = ['YES', ' '.join(str(answer[i]) for i in range(1, n + 1))]
    sys.stdout.write('\n'.join(out))

if __name__ == "__main__":
    solve()