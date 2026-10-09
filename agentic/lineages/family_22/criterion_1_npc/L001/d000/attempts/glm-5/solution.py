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
    
    # Compute longest path to each node (minimum required serving number)
    topo = []
    q = deque([i for i in range(n) if indeg[i] == 0])
    while q:
        u = q.popleft()
        topo.append(u)
        for v in adj[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)
    
    if len(topo) != n:
        print("NO")
        return
    
    min_serving = [1] * n
    for u in topo:
        for v in adj[u]:
            if min_serving[v] < min_serving[u] + 1:
                min_serving[v] = min_serving[u] + 1
    
    if max(min_serving) > T:
        print("NO")
        return
    
    # Binary search for maximum valid serving number
    lo, hi = 1, T
    best = -1
    best_assign = None
    
    while lo <= hi:
        mid = (lo + hi) // 2
        # Check if we can assign with max serving <= mid
        assign = [min_serving[i] for i in range(n)]
        changed = True
        while changed:
            changed = False
            for u in range(n):
                for v in adj[u]:
                    if assign[v] < assign[u] + 1:
                        assign[v] = assign[u] + 1
                        changed = True
                    if assign[v] > mid:
                        break
                else:
                    continue
                break
            else:
                continue
            break
        
        if max(assign) > mid:
            lo = mid + 1
            continue
        
        # Check capacity constraints
        cnt = [0] * (mid + 1)
        valid = True
        for x in assign:
            cnt[x] += 1
            if cnt[x] > M:
                valid = False
                break
        
        if valid:
            best = mid
            best_assign = assign[:]
            hi = mid - 1
        else:
            lo = mid + 1
    
    if best == -1:
        print("NO")
        return
    
    # Greedy assignment to minimize serving numbers
    assign = best_assign[:]
    # Sort by (serving number, node index) for deterministic processing
    nodes = sorted(range(n), key=lambda x: (assign[x], x))
    
    for u in nodes:
        # Try to move u to an earlier serving if possible
        target = 1
        if u > 0:
            target = assign[nodes[nodes.index(u) - 1]] if nodes.index(u) > 0 else 1
        
        original = assign[u]
        for s in range(original - 1, 0, -1):
            # Check if we can move to serving s
            # Check precedence constraints
            ok = True
            for v in adj[u]:
                if assign[v] <= s:
                    ok = False
                    break
            if not ok:
                break
            
            # Check reverse precedence
            for v in range(n):
                if v != u and assign[v] == s:
                    # Check if v must come after u
                    pass  # We need to check if there's a path from u to v
            
            # Check capacity
            cnt = [0] * (best + 1)
            for i in range(n):
                if i == u:
                    cnt[s] += 1
                else:
                    cnt[assign[i]] += 1
            if cnt[s] > M:
                continue
            
            # Check if moving u to s violates any precedence
            # We need to ensure all predecessors of u are in servings < s
            # and all successors of u are in servings > s
            # Predecessors check
            pred_ok = True
            for v in range(n):
                if v != u and assign[v] < original:
                    # Check if v is a predecessor of u
                    # We need to check if there's a path from v to u
                    # Since we're moving u earlier, we need to ensure v is still before u
                    pass
            
            # For simplicity, just check direct constraints
            temp_assign = assign[:]
            temp_assign[u] = s
            valid = True
            for a in range(n):
                for b in adj[a]:
                    if temp_assign[a] >= temp_assign[b]:
                        valid = False
                        break
                if not valid:
                    break
            
            if valid:
                cnt = [0] * (best + 1)
                for x in temp_assign:
                    cnt[x] += 1
                if all(c <= M for c in cnt[1:]):
                    assign = temp_assign
                    break
    
    print("YES")
    print(' '.join(map(str, assign)))

if __name__ == "__main__":
    solve()