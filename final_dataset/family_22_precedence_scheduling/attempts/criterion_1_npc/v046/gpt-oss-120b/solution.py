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
    indeg = [0] * n
    for _ in range(m):
        a = int(next(it)) - 1
        b = int(next(it)) - 1
        adj[a].append(b)
        indeg[b] += 1

    # topological order and earliest term (longest path)
    q = deque([i for i in range(n) if indeg[i] == 0])
    earliest = [1] * n
    topo = []
    while q:
        u = q.popleft()
        topo.append(u)
        eu = earliest[u]
        for v in adj[u]:
            if earliest[v] < eu + 1:
                earliest[v] = eu + 1
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)

    if len(topo) != n:
        print("NO")
        return

    if max(earliest) > T:
        print("NO")
        return

    # bucket modules by earliest term
    buckets = [[] for _ in range(T + 2)]
    for i, e in enumerate(earliest):
        buckets[e].append(i)

    assign = [0] * n
    waiting = deque()
    for term in range(1, T + 1):
        # add newly available modules
        waiting.extend(buckets[term])
        # assign up to M modules this term
        for _ in range(M):
            if not waiting:
                break
            mod = waiting.popleft()
            assign[mod] = term
    if any(a == 0 for a in assign):
        print("NO")
    else:
        print("YES")
        print(' '.join(str(x) for x in assign))

if __name__ == "__main__":
    solve()