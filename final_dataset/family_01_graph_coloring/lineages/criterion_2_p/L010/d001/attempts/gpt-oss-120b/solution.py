import sys
from collections import deque

def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    it = iter(data)
    n = next(it)
    m = next(it)

    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = next(it); v = next(it)
        adj[u].append(v)
        adj[v].append(u)

    parity = [-1] * (n + 1)          # temporary 0/1 colours
    answer = [0] * (n + 1)           # final 1/2 values

    for start in range(1, n + 1):
        if parity[start] != -1:
            continue
        # BFS of one component
        q = deque([start])
        parity[start] = 0
        comp = [start]
        while q:
            v = q.popleft()
            pv = parity[v]
            for to in adj[v]:
                if parity[to] == -1:
                    parity[to] = pv ^ 1
                    q.append(to)
                    comp.append(to)
                elif parity[to] == pv:
                    # not bipartite
                    sys.stdout.write("NO")
                    return

        # orient so that smallest index gets value 1
        min_v = min(comp)
        want = parity[min_v]          # parity that must become 1
        for v in comp:
            answer[v] = 1 if parity[v] == want else 2

    # all components processed successfully
    out_lines = ["YES", " ".join(str(answer[i]) for i in range(1, n + 1))]
    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    solve()