import sys
from collections import deque

def solve():
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
    
    # earliest slot for each task (1-indexed)
    earliest = [1] * n
    q = deque()
    for i in range(n):
        if indeg[i] == 0:
            q.append(i)
    
    topo = []
    while q:
        u = q.popleft()
        topo.append(u)
        for v in adj[u]:
            if earliest[v] < earliest[u] + 1:
                earliest[v] = earliest[u] + 1
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)
    
    if len(topo) != n:
        print("NO")
        return
    
    # check deadline feasibility
    for i in range(n):
        if earliest[i] > T:
            print("NO")
            return
    
    # latest slot for each task (1-indexed)
    latest = [T] * n
    for u in reversed(topo):
        for v in adj[u]:
            if latest[u] > latest[v] - 1:
                latest[u] = latest[v] - 1
    
    # check if latest >= earliest for all
    for i in range(n):
        if latest[i] < earliest[i]:
            print("NO")
            return
    
    # assign slots greedily from earliest to latest
    tasks_by_earliest = [[] for _ in range(T + 1)]
    for i in range(n):
        tasks_by_earliest[earliest[i]].append(i)
    
    slot = [0] * n
    # tasks waiting to be scheduled, sorted by latest deadline
    waiting = []
    
    for t in range(1, T + 1):
        # add tasks that become available at this slot
        for task in tasks_by_earliest[t]:
            # insert into waiting list maintaining sorted order by latest
            # use binary search for efficiency
            lo, hi = 0, len(waiting)
            while lo < hi:
                mid = (lo + hi) // 2
                if latest[waiting[mid]] < latest[task]:
                    lo = mid + 1
                else:
                    hi = mid
            waiting.insert(lo, task)
        
        # schedule up to M tasks
        scheduled = 0
        new_waiting = []
        for task in waiting:
            if scheduled < M and latest[task] >= t:
                slot[task] = t
                scheduled += 1
            else:
                new_waiting.append(task)
        waiting = new_waiting
    
    # check if all tasks are scheduled
    for i in range(n):
        if slot[i] == 0:
            print("NO")
            return
    
    print("YES")
    print(' '.join(map(str, slot)))

solve()