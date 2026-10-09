import sys
from collections import deque

def solve():
    data = sys.stdin.buffer.read().split()
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

    # earliest[i] = earliest week sector i can be scheduled (1-indexed)
    earliest = [1] * (n + 1)
    q = deque()
    for i in range(1, n + 1):
        if indeg[i] == 0:
            q.append(i)

    topo = []
    while q:
        u = q.popleft()
        topo.append(u)
        for v in adj[u]:
            if earliest[u] + 1 > earliest[v]:
                earliest[v] = earliest[u] + 1
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)

    if len(topo) != n:
        print("NO")
        return

    # Check feasibility: earliest week must be <= T
    for i in range(1, n + 1):
        if earliest[i] > T:
            print("NO")
            return

    # Greedy assignment: process sectors in topological order,
    # assign each to the earliest available week >= earliest[i]
    # Use a min-heap of (week, count) to track available slots.
    import heapq

    # We'll maintain for each week how many slots are used.
    # To find earliest available week >= e, use a heap of weeks with free slots.
    free_heap = []  # min-heap of weeks that have free capacity
    week_count = {}  # week -> number assigned
    ans = [0] * (n + 1)

    # We can lazily manage free slots.
    # Initialize: all weeks 1..T have M free slots, but we add on demand.
    # Actually, let's just push weeks as needed.

    for u in topo:
        e = earliest[u]
        # Find earliest week >= e with free slot
        # Clean up heap top if it's < e or no longer free
        while free_heap:
            w = free_heap[0]
            if w < e:
                heapq.heappop(free_heap)
            elif week_count.get(w, 0) >= M:
                heapq.heappop(free_heap)
            else:
                break
        if free_heap and free_heap[0] >= e:
            w = heapq.heappop(free_heap)
        else:
            w = e
        ans[u] = w
        c = week_count.get(w, 0) + 1
        week_count[w] = c
        if c < M:
            heapq.heappush(free_heap, w)

    # Verify all weeks <= T
    for i in range(1, n + 1):
        if ans[i] > T or ans[i] < 1:
            print("NO")
            return

    # Verify capacity
    from collections import Counter
    cnt = Counter(ans[1:])
    for w, c in cnt.items():
        if c > M:
            print("NO")
            return

    print("YES")
    print(" ".join(str(ans[i]) for i in range(1, n + 1)))

solve()