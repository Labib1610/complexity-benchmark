import sys
from collections import deque

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    M = int(next(it))
    T = int(next(it))
    m = int(next(it))
    
    adj = [[] for _ in range(n+1)]
    radj = [[] for _ in range(n+1)]
    indeg = [0]*(n+1)
    
    for _ in range(m):
        a = int(next(it))
        b = int(next(it))
        adj[a].append(b)
        radj[b].append(a)
        indeg[b] += 1
    
    # earliest cycle: longest path from any source
    earliest = [1]*(n+1)
    q = deque()
    for i in range(1, n+1):
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
        # cycle in prerequisites
        print("NO")
        return
    
    # latest cycle
    latest = [T]*(n+1)
    for u in reversed(topo):
        for v in adj[u]:
            if latest[u] > latest[v] - 1:
                latest[u] = latest[v] - 1
    
    for i in range(1, n+1):
        if earliest[i] > latest[i] or earliest[i] > T:
            print("NO")
            return
    
    # feasible scheduling with capacity M per cycle
    # process in topological order, assign each node the earliest available cycle >= earliest[i]
    # using a min-heap of (cycle, remaining_capacity)
    
    import heapq
    heap = []
    # available slots: we can use cycles 1..T
    # we'll lazily manage: push (cycle, capacity) when needed
    
    # To efficiently find earliest cycle with capacity:
    # We maintain a pointer to the next cycle to consider and a heap of freed cycles.
    
    # Simpler: since T can be large, use a segment tree or just a dict + heap.
    
    # Let's use a min-heap of cycles that have free capacity.
    # We also need to ensure we don't exceed capacity per cycle.
    
    # We'll process nodes in topological order. For each node, we need the smallest cycle >= earliest[i] with remaining capacity.
    
    # Use a heap of (cycle, remaining). But we need to query by cycle >= earliest[i].
    # Since we process in topo order, earliest is non-decreasing? Not necessarily, but let's just use a lazy approach.
    
    # Alternative: use a segment tree over cycles 1..T for max remaining capacity, and binary search.
    # But T can be up to 1e9? Let's check constraints... not given. Let's be safe.
    
    # Actually, let's use a simpler approach: maintain a sorted structure of cycles with free capacity.
    # Use a heap, but we need cycles >= earliest[i]. We can pop cycles < earliest[i] and reinsert them later? No.
    
    # Let's use a different approach: since we process in topo order and earliest[i] is the lower bound,
    # we can use a pointer `cur` that only moves forward, plus a min-heap of "freed" cycles (cycles that got capacity back? No, capacity doesn't come back).
    
    # Actually capacity doesn't free up. So we just need to assign each node to a cycle >= earliest[i] with capacity < M.
    # We can use a min-heap of (cycle, count) where count < M. But we need cycle >= earliest[i].
    
    # Since earliest[i] can vary, let's use a balanced BST. In Python, we can use sortedcontainers, but not available.
    # Let's use a segment tree if T is small, or a different method.
    
    # Given the problem likely has reasonable T, let's use a dict + heap approach.
    
    # We'll maintain:
    # - count[c] = number of operations assigned to cycle c
    # - a min-heap of cycles that have count[c] < M
    
    # When assigning node i:
    #   we need the smallest cycle c >= earliest[i] with count[c] < M.
    #   We can pop from heap cycles < earliest[i] and push them to a "pending" structure? No, they might still be usable later if earliest[j] <= c.
    
    # Actually, since we process in topo order, and earliest is non-decreasing in topo order? Let's check.
    # In topo order, for edge u->v, earliest[v] >= earliest[u]+1 > earliest[u]. So yes, earliest is strictly increasing along edges.
    # But topo order doesn't guarantee earliest is non-decreasing for unrelated nodes. E.g., two sources both have earliest=1.
    
    # So we need a data structure that supports: find smallest c >= L with count[c] < M, then increment count[c].
    
    # Let's use a segment tree over cycles 1..T. But T might be large.
    # Given memory limit 256MB and time 5s, and typical constraints, let's assume T is manageable (e.g., up to 1e6 or 1e7).
    # But to be safe, let's use a coordinate compression + segment tree, or a different approach.
    
    # Actually, let's use a simpler greedy with a heap of "available cycle slots":
    # We maintain a min-heap. For each node, we try to find the smallest cycle >= earliest[i].
    # We can keep a heap of (cycle, remaining_capacity). When we need cycle >= L:
    #   - pop all cycles < L, and if they still have capacity, we can't use them now, but we might need them later? No, because earliest is non-decreasing? Not guaranteed.
    
    # Let me think differently. We can use a DSU (disjoint set union) approach:
    # For each cycle c, next_free[c] points to the next cycle >= c with free capacity.
    # When we assign a node to cycle c, if count[c] reaches M, we union c with c+1.
    
    # This is efficient if T is up to 1e7 or so. For larger T, we need coordinate compression.
    
    # Let's implement with a dict-based DSU to handle large T.
    
    parent = {}
    count = {}
    
    def find(x):
        # path compression
        root = x
        while root in parent:
            root = parent[root]
        # compress
        cur = x
        while cur in parent:
            nxt = parent[cur]
            parent[cur] = root
            cur = nxt
        return root
    
    def get_next(x):
        rx = find(x)
        if rx not in count:
            count[rx] = 0
        if count[rx] >= M:
            # union with rx+1
            parent[rx] = rx + 1
            return get_next(x)
        return rx
    
    assign = [0]*(n+1)
    
    for u in topo:
        c = get_next(earliest[u])
        if c > latest[u] or c > T:
            print("NO")
            return
        count[c] = count.get(c, 0) + 1
        if count[c] >= M:
            parent[c] = c + 1
        assign[u] = c
    
    print("YES")
    print(' '.join(str(assign[i]) for i in range(1, n+1)))

solve()