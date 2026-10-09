import sys
from collections import deque
import itertools

# Increase recursion depth just in case
sys.setrecursionlimit(200000)

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    M = int(input_data[1])
    T = int(input_data[2])
    m = int(input_data[3])
    
    if n > M * T:
        print("NO")
        return
    
    adj = [[] for _ in range(n + 1)]
    rev_adj = [[] for _ in range(n + 1)]
    in_deg_orig = [0] * (n + 1)
    
    idx = 4
    for _ in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx + 1])
        idx += 2
        adj[u].append(v)
        rev_adj[v].append(u)
        in_deg_orig[v] += 1
        
    # Check for cycles and compute topological order
    in_d = list(in_deg_orig)
    q = deque([i for i in range(1, n + 1) if in_d[i] == 0])
    topo = []
    while q:
        u = q.popleft()
        topo.append(u)
        for v in adj[u]:
            in_d[v] -= 1
            if in_d[v] == 0:
                q.append(v)
                
    if len(topo) < n:
        print("NO")
        return
    
    # Compute E(u): earliest section
    E = [1] * (n + 1)
    for u in topo:
        for v in adj[u]:
            if E[u] + 1 > E[v]:
                E[v] = E[u] + 1
                
    # Compute L(u): latest section
    # height to sink
    height = [0] * (n + 1)
    for u in reversed(topo):
        for v in adj[u]:
            if height[v] + 1 > height[u]:
                height[u] = height[v] + 1
                
    L = [T - height[u] for u in range(n + 1)]
    
    for i in range(1, n + 1):
        if E[i] > L[i] or E[i] > T or L[i] < 1:
            print("NO")
            return

    # Check interval capacity bounds
    for t1 in range(1, T + 1):
        for t2 in range(t1, T + 1):
            cnt = sum(1 for i in range(1, n + 1) if E[i] >= t1 and L[i] <= t2)
            if cnt > (t2 - t1 + 1) * M:
                print("NO")
                return

    # Backtracking search
    ans = [0] * (n + 1)
    in_degree = list(in_deg_orig)
    placed_count = 0
    
    # Priority score for sorting candidates
    def priority(u):
        return (L[u], -height[u], -len(adj[u]))

    def backtrack(t):
        nonlocal placed_count
        if placed_count == n:
            return True
        if t > T:
            return False
        
        # Available nodes: unplaced with in_degree == 0
        available = [u for u in range(1, n + 1) if ans[u] == 0 and in_degree[u] == 0]
        
        required = []
        candidates = []
        for u in available:
            if L[u] == t:
                required.append(u)
            else:
                candidates.append(u)
                
        if len(required) > M:
            return False
        
        needed = M - len(required)
        candidates.sort(key=priority)
        
        if len(candidates) <= needed:
            choices = [candidates]
        else:
            # Generate combinations of candidates, but try the top ones first
            # Usually taking the most urgent first is sufficient
            # Limit candidate pool to a reasonable size if huge to avoid combinatorial explosion
            pool_size = min(len(candidates), needed + 5)
            pool = candidates[:pool_size]
            choices = list(itertools.combinations(pool, needed))
            
        for choice in choices:
            batch = required + list(choice)
            
            # Place batch
            for u in batch:
                ans[u] = t
                for v in adj[u]:
                    in_degree[v] -= 1
            placed_count += len(batch)
            
            if backtrack(t + 1):
                return True
            
            # Unplace batch
            placed_count -= len(batch)
            for u in batch:
                ans[u] = 0
                for v in adj[u]:
                    in_degree[v] += 1
                    
        return False

    if backtrack(1):
        print("YES")
        print(*(ans[1:]))
    else:
        print("NO")

if __name__ == '__main__':
    solve()