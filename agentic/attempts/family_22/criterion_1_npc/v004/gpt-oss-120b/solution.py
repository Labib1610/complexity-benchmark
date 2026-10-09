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

    # topological order and earliest slot (release time)
    q = deque([i for i in range(n) if indeg[i]==0])
    topo = []
    earliest = [1]*n
    while q:
        u = q.popleft()
        topo.append(u)
        for v in adj[u]:
            indeg[v] -= 1
            if earliest[v] < earliest[u] + 1:
                earliest[v] = earliest[u] + 1
            if indeg[v]==0:
                q.append(v)
    if len(topo)!=n:
        print("NO")
        return

    # if any earliest > T, impossible
    if any(e > T for e in earliest):
        print("NO")
        return

    # bucket tasks by release time
    release = [[] for _ in range(T+2)]
    for i, e in enumerate(earliest):
        release[e].append(i)

    schedule = [0]*n
    ready = deque()
    for t in range(1, T+1):
        # add newly released tasks
        ready.extend(release[t])
        # schedule up to M tasks this slot
        for _ in range(M):
            if not ready:
                break
            task = ready.popleft()
            schedule[task] = t
    # after all slots, check if all scheduled
    if any(slot==0 for slot in schedule):
        print("NO")
    else:
        print("YES")
        print(' '.join(map(str, schedule)))

if __name__ == "__main__":
    solve()