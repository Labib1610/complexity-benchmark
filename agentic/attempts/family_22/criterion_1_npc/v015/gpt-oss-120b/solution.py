import sys
from collections import deque, defaultdict

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
    indeg = [0] * n
    for _ in range(m):
        a = int(next(it)) - 1
        b = int(next(it)) - 1
        adj[a].append(b)
        indeg[b] += 1

    ready = deque([i for i in range(n) if indeg[i] == 0])
    schedule = [0] * n
    assigned = 0

    for shift in range(1, T + 1):
        cnt = 0
        # take up to M tasks that are ready
        while ready and cnt < M:
            v = ready.popleft()
            schedule[v] = shift
            assigned += 1
            cnt += 1
            for nb in adj[v]:
                indeg[nb] -= 1
                if indeg[nb] == 0:
                    ready.append(nb)
        if assigned == n:
            break

    if assigned == n:
        sys.stdout.write("YES\n")
        sys.stdout.write(" ".join(map(str, schedule)) + "\n")
    else:
        sys.stdout.write("NO\n")

if __name__ == "__main__":
    solve()