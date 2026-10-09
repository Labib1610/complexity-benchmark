import sys
from collections import deque

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    M = int(next(it))
    T = int(next(it))
    m = int(next(it))
    adj = [[] for _ in range(n)]
    indeg = [0]*n
    for _ in range(m):
        a = int(next(it))-1
        b = int(next(it))-1
        adj[a].append(b)
        indeg[b] += 1

    ready = deque([i for i in range(n) if indeg[i]==0])
    phase = [0]*n
    cur = 1
    scheduled = 0
    while cur <= T and ready:
        cnt = 0
        nxt = []
        while ready and cnt < M:
            v = ready.popleft()
            phase[v] = cur
            scheduled += 1
            cnt += 1
            for nb in adj[v]:
                indeg[nb] -= 1
                if indeg[nb]==0:
                    nxt.append(nb)
        # add newly ready vertices for next phases
        for x in nxt:
            ready.append(x)
        cur += 1

    if scheduled == n:
        sys.stdout.write("YES\n")
        sys.stdout.write(" ".join(map(str, phase)))
    else:
        sys.stdout.write("NO")

if __name__ == "__main__":
    solve()