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
    indeg = [0]*n
    for _ in range(m):
        a = int(next(it))-1
        b = int(next(it))-1
        adj[a].append(b)
        indeg[b] += 1

    # topological order
    q = deque([i for i in range(n) if indeg[i]==0])
    topo = []
    while q:
        v = q.popleft()
        topo.append(v)
        for to in adj[v]:
            indeg[to] -= 1
            if indeg[to]==0:
                q.append(to)
    if len(topo)!=n:
        print("NO")
        return

    # earliest possible layer (longest path length)
    earliest = [1]*n
    for v in topo:
        for to in adj[v]:
            if earliest[to] < earliest[v]+1:
                earliest[to] = earliest[v]+1

    # schedule greedily by earliest, respecting capacity
    slots = [[] for _ in range(T+1)]  # 1-indexed
    assigned = [0]*n
    # bucket jobs by earliest
    bucket = defaultdict(list)
    for i in range(n):
        bucket[earliest[i]].append(i)

    # use a list of ready jobs (whose predecessors already scheduled)
    ready = []
    # maintain count of unscheduled predecessors
    rem_pred = [0]*n
    for i in range(n):
        rem_pred[i] = sum(1 for _ in adj_rev if False)  # placeholder

    # compute reverse adjacency and remaining preds
    rev = [[] for _ in range(n)]
    for u in range(n):
        for v in adj[u]:
            rev[v].append(u)
    rem_pred = [len(rev[i]) for i in range(n)]

    # initially add jobs with no preds and earliest <=1
    for i in range(n):
        if rem_pred[i]==0:
            ready.append(i)

    # we will process shifts 1..T
    import heapq
    heap = []  # (earliest, job)
    for i in ready:
        heapq.heappush(heap, (earliest[i], i))
    ready.clear()

    for shift in range(1, T+1):
        # add newly eligible jobs whose earliest == shift
        for job in bucket.get(shift, []):
            if rem_pred[job]==0:
                heapq.heappush(heap, (earliest[job], job))
        cnt = 0
        while heap and cnt < M:
            _, job = heapq.heappop(heap)
            if assigned[job]:
                continue
            assigned[job] = shift
            cnt += 1
            for nb in adj[job]:
                rem_pred[nb] -= 1
                if rem_pred[nb]==0 and earliest[nb] <= shift+1:
                    heapq.heappush(heap, (earliest[nb], nb))
        # continue
    if any(a==0 for a in assigned):
        print("NO")
    else:
        print("YES")
        print(' '.join(str(x) for x in assigned))

if __name__ == "__main__":
    solve()