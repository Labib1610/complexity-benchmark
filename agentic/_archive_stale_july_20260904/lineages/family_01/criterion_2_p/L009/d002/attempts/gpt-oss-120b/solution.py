import sys
from collections import deque

def solve() -> None:
    data = sys.stdin.read().strip().split()
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

    parity = [-1] * (n + 1)          # temporary 0/1 inside component
    answer = [0] * (n + 1)           # final 1/2

    for start in range(1, n + 1):
        if parity[start] != -1:
            continue
        # BFS this component
        q = deque([start])
        parity[start] = 0
        comp = [start]
        ok = True
        while q:
            u = q.popleft()
            pu = parity[u]
            for v in adj[u]:
                if parity[v] == -1:
                    parity[v] = pu ^ 1
                    q.append(v)
                    comp.append(v)
                elif parity[v] == pu:
                    # not bipartite
                    print("NO")
                    return
        # decide orientation for lexicographically smallest result
        vmin = min(comp)
        if parity[vmin] == 0:
            for x in comp:
                answer[x] = 1 if parity[x] == 0 else 2
        else:
            for x in comp:
                answer[x] = 1 if parity[x] == 1 else 2

    # all components processed successfully
    out = ["YES", " ".join(str(answer[i]) for i in range(1, n + 1))]
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()