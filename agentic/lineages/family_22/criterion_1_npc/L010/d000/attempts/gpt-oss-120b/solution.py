import sys
from collections import deque

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    N = int(next(it))
    M = int(next(it))
    D = int(next(it))
    P = int(next(it))

    adj = [[] for _ in range(N + 1)]
    indeg = [0] * (N + 1)

    for _ in range(P):
        a = int(next(it))
        b = int(next(it))
        adj[a].append(b)
        indeg[b] += 1

    q = deque([i for i in range(1, N + 1) if indeg[i] == 0])
    slot = [0] * (N + 1)          # 0 = not scheduled yet

    for t in range(1, D + 1):
        cnt = 0
        while cnt < M and q:
            v = q.popleft()
            slot[v] = t
            cnt += 1
            for w in adj[v]:
                indeg[w] -= 1
                if indeg[w] == 0:
                    q.append(w)

    if any(s == 0 for s in slot[1:]):
        sys.stdout.write("NO")
    else:
        sys.stdout.write("YES\n")
        sys.stdout.write(' '.join(str(slot[i]) for i in range(1, N + 1)))

if __name__ == "__main__":
    solve()