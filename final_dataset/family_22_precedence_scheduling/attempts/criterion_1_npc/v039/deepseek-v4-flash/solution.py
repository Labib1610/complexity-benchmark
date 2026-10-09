from collections import deque
import sys

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    M = int(next(it))
    T = int(next(it))
    m = int(next(it))

    adj = [[] for _ in range(n + 1)]
    indeg = [0] * (n + 1)

    for _ in range(m):
        a = int(next(it))
        b = int(next(it))
        adj[a].append(b)
        indeg[b] += 1

    # Topological order
    q = deque()
    for i in range(1, n + 1):
        if indeg[i] == 0:
            q.append(i)

    topo = []
    while q:
        u = q.popleft()
        topo.append(u)
        for v in adj[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)

    if len(topo) != n:
        print("NO")
        return

    # Assign minutes greedily
    pred_min = [0] * (n + 1)  # latest predecessor minute
    ans = [0] * (n + 1)
    count = [0] * (T + 1)  # count of jobs per minute

    for u in topo:
        # Earliest minute = pred_min[u] + 1
        minute = pred_min[u] + 1
        # Find first minute >= minute with free capacity
        while minute <= T and count[minute] >= M:
            minute += 1
        if minute > T:
            print("NO")
            return
        ans[u] = minute
        count[minute] += 1
        # update successors
        for v in adj[u]:
            if pred_min[v] < minute:
                pred_min[v] = minute

    print("YES")
    print(" ".join(str(ans[i]) for i in range(1, n + 1)))

if __name__ == "__main__":
    solve()