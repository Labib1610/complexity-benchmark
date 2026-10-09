import sys
import sys
sys.setrecursionlimit(1000000)

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    B = int(next(it))
    
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u].append(v)
        adj[v].append(u)
    
    # BFS to get order (distance from root, breaking ties by node index)
    root = 1
    for i in range(1, n + 1):
        if len(adj[i]) > len(adj[root]):
            root = i
    
    vis = [False] * (n + 1)
    q = []
    vis[root] = True
    q.append(root)
    order = []
    head = 0
    while head < len(q):
        u = q[head]
        head += 1
        order.append(u)
        children = []
        for v in adj[u]:
            if not vis[v]:
                vis[v] = True
                children.append(v)
        children.sort()
        for v in children:
            q.append(v)
    
    size = [0] * (n + 1)
    idx = [0] * (n + 1)
    for i, u in enumerate(order):
        idx[u] = i
    
    # Compute sizes (we only need correct relative order for centroid decomp heuristic)
    # For path lengths, the heuristic used centers smaller subtrees.
    # The code uses size array only for comparison, so we need to fill it.
    # We can compute sizes bottom-up.
    # Build parent relationship from BFS order
    parent = [0] * (n + 1)
    parent[root] = 0
    for u in order:
        for v in adj[u]:
            if parent[v] == 0 and v != root:
                parent[v] = u
    
    # Compute sizes bottom-up (reverse of order)
    for u in reversed(order):
        size[u] = 1
        for v in adj[u]:
            if parent[v] == u:
                size[u] += size[v]
    
    # Recursive greedy positioning
    slots = [0] * (n + 1)
    def dfs(u, L, R):
        slots[u] = L
        avail_start = L + 1
        for v in adj[u]:
            if parent[v] == u:
                sz = size[v]
                # Limit interval size
                max_width = min(2 * sz, R - avail_start + 1)
                target_end = avail_start + max_width - 1
                dfs(v, avail_start, target_end)
                # Re-center v at the middle of its interval
                pos_v = slots[v]
                start_v = pos_v - (sz - 1)
                end_v = pos_v + (sz - 1)
                mid = (start_v + end_v) // 2
                slots[v] = start_v + (mid - start_v)
                avail_start = end_v + 1
    
    dfs(root, 1, n)
    
    # Validate and output
    used = [False] * (n + 1)
    for u in range(1, n + 1):
        p = slots[u]
        if p < 1 or p > n or used[p]:
            print("NO")
            return
        used[p] = True
    
    total = 0
    for u in range(1, n + 1):
        for v in adj[u]:
            if u < v:
                total += abs(slots[u] - slots[v])
    
    if total <= B:
        print("YES")
        print(' '.join(map(str, slots[1:])))
    else:
        print("NO")

if __name__ == "__main__":
    solve()