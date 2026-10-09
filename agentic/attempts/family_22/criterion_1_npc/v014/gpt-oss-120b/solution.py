import sys
import heapq

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it)); M = int(next(it)); T = int(next(it)); m = int(next(it))
    adj = [[] for _ in range(n)]
    radj = [[] for _ in range(n)]
    indeg = [0]*n
    for _ in range(m):
        a = int(next(it))-1
        b = int(next(it))-1
        adj[a].append(b)
        radj[b].append(a)
        indeg[b] += 1

    # topological order
    from collections import deque
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

    # earliest (release) times
    earliest = [1]*n
    for v in topo:
        for to in adj[v]:
            if earliest[to] < earliest[v] + 1:
                earliest[to] = earliest[v] + 1

    # latest (deadline) times
    latest = [T]*n
    for v in reversed(topo):
        for pre in radj[v]:
            if latest[pre] > latest[v] - 1:
                latest[pre] = latest[v] - 1

    for i in range(n):
        if earliest[i] > latest[i]:
            print("NO")
            return

    # schedule using earliest release and latest deadline
    tasks_by_release = [[] for _ in range(T+2)]
    for i in range(n):
        tasks_by_release[earliest[i]].append(i)

    heap = []  # (deadline, task)
    schedule = [0]*n
    scheduled = 0
    for time in range(1, T+1):
        for task in tasks_by_release[time]:
            heapq.heappush(heap, (latest[task], task))
        # take up to M tasks whose deadline >= time
        cnt = 0
        while heap and cnt < M:
            dl, task = heapq.heappop(heap)
            if dl < time:   # missed deadline
                print("NO")
                return
            schedule[task] = time
            cnt += 1
            scheduled += 1
        # continue
    if scheduled != n:
        print("NO")
        return
    print("YES")
    print(' '.join(map(str, schedule)))

if __name__ == "__main__":
    solve()