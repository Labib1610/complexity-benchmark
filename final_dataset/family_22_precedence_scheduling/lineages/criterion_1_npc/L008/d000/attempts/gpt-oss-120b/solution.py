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

    # topological order and compute minimal level (release time)
    q = deque([i for i in range(n) if indeg[i]==0])
    topo = []
    min_level = [1]*n
    while q:
        u = q.popleft()
        topo.append(u)
        for v in adj[u]:
            if min_level[v] < min_level[u] + 1:
                min_level[v] = min_level[u] + 1
            indeg[v] -= 1
            if indeg[v]==0:
                q.append(v)

    if len(topo)!=n:
        print("NO")
        return

    if max(min_level) > T:
        print("NO")
        return

    # bucket tasks by their minimal feasible level
    buckets = [[] for _ in range(T+2)]
    for i, lvl in enumerate(min_level):
        buckets[lvl].append(i)

    assign = [0]*n
    waiting = deque()
    assigned_cnt = 0
    for cur in range(1, T+1):
        # add newly released tasks
        waiting.extend(buckets[cur])
        # assign up to M tasks this stage
        for _ in range(M):
            if not waiting:
                break
            node = waiting.popleft()
            assign[node] = cur
            assigned_cnt += 1

    if assigned_cnt == n:
        print("YES")
        print(' '.join(str(assign[i]) for i in range(n)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()