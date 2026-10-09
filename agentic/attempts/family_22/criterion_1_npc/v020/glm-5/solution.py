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
    rev_adj = [[] for _ in range(n+1)]
    indeg = [0]*(n+1)
    
    for _ in range(m):
        a = int(next(it))
        b = int(next(it))
        adj[a].append(b)
        rev_adj[b].append(a)
        indeg[b] += 1
    
    # Compute longest chain
    topo = []
    q = deque()
    for i in range(1, n+1):
        if indeg[i] == 0:
            q.append(i)
    
    dp = [1]*(n+1)
    
    while q:
        u = q.popleft()
        topo.append(u)
        for v in adj[u]:
            if dp[u] + 1 > dp[v]:
                dp[v] = dp[u] + 1
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)
    
    if len(topo) != n:
        print("NO")
        return
    
    # Sort by longest chain
    order = sorted(range(1, n+1), key=lambda x: dp[x])
    
    # Build tree
    parent = [0]*(n+1)
    children = [[] for _ in range(n+1)]
    for u in range(1, n+1):
        best = 0
        best_p = 0
        for p in rev_adj[u]:
            if dp[p] > best:
                best = dp[p]
                best_p = p
        if best > 0:
            parent[u] = best_p
            children[best_p].append(u)
    
    # Compute positions via DFS
    pos = [0]*(n+1)
    size = [0]*(n+1)
    
    roots = [u for u in range(1, n+1) if parent[u] == 0]
    stack = []
    for r in reversed(roots):
        stack.append((r, 0))
    
    while stack:
        u, state = stack.pop()
        if state == 0:
            stack.append((u, 1))
            for c in reversed(children[u]):
                stack.append((c, 0))
        else:
            # Determine position
            min_pos = 1
            for p in rev_adj[u]:
                if pos[p] >= min_pos:
                    min_pos = pos[p] + 1
            # Check constraint from parent in tree
            p = parent[u]
            if p > 0:
                if pos[p] >= min_pos:
                    min_pos = pos[p] + 1
            pos[u] = min_pos
            size[pos[u]] += 1
    
    # Check capacity
    for r in range(1, T+1):
        if size[r] > M:
            print("NO")
            return
    
    print("YES")
    print(' '.join(str(pos[i]) for i in range(1, n+1)))

if __name__ == "__main__":
    solve()