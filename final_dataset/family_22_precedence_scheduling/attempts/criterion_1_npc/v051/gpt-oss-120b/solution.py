import sys
from collections import deque

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it)); M = int(next(it)); T = int(next(it)); m = int(next(it))
    adj = [[] for _ in range(n)]
    indeg = [0]*n
    for _ in range(m):
        a = int(next(it))-1
        b = int(next(it))-1
        adj[a].append(b)
        indeg[b] += 1

    # topological order and earliest week (release time)
    q = deque([i for i in range(n) if indeg[i]==0])
    topo = []
    earliest = [1]*n
    while q:
        u = q.popleft()
        topo.append(u)
        for v in adj[u]:
            if earliest[u]+1 > earliest[v]:
                earliest[v] = earliest[u]+1
            indeg[v] -= 1
            if indeg[v]==0:
                q.append(v)
    if len(topo)!=n:
        print("NO")
        return

    # check feasibility via cumulative condition
    # count tasks with release <= k
    release_counts = [0]*(T+2)
    for e in earliest:
        if e > T:
            print("NO")
            return
        release_counts[e] += 1
    cum = 0
    for week in range(1, T+1):
        cum += release_counts[week]
        if cum > M*week:
            print("NO")
            return
    if n > M*T:
        print("NO")
        return

    # construct schedule greedily
    # bucket tasks by release week
    buckets = [[] for _ in range(T+1)]
    for i, e in enumerate(earliest):
        buckets[e].append(i)
    unscheduled = set()
    for week in range(1, T+1):
        for v in buckets[week]:
            unscheduled.add(v)
        take = []
        while unscheduled and len(take) < M:
            v = unscheduled.pop()
            take.append(v)
        for v in take:
            # assign week
            earliest[v] = week  # reuse array for answer
    # after loop, all should be scheduled
    if any(isinstance(x, int) and x>0 and x<=T for x in earliest):
        # all assigned
        ans = [str(earliest[i]) for i in range(n)]
        print("YES")
        print(' '.join(ans))
    else:
        print("NO")

if __name__ == "__main__":
    solve()