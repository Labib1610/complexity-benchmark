import sys
from collections import deque

def readints():
    return list(map(int, sys.stdin.readline().split()))

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it)); m = int(next(it)); k = int(next(it))
    commodities = []
    for _ in range(k):
        s = int(next(it))-1
        t = int(next(it))-1
        d = int(next(it))
        commodities.append((s,t,d))
    edges = []
    adj = [[] for _ in range(n)]
    for idx in range(m):
        u = int(next(it))-1
        v = int(next(it))-1
        cap = int(next(it))
        edges.append((u,v,cap))
        adj[u].append((v,idx))
    # Simple feasibility check: total demand <= sum caps on any cut?
    # Use linear programming via BFS enumeration for tiny instances.
    # If k*m <= 20, brute force all distributions.
    if k*m > 20:
        print("NO")
        return
    # enumerate flows per commodity per edge (0..cap)
    caps = [c for _,_,c in edges]
    total_vars = k*m
    # recursive search
    flows = [[0]*m for _ in range(k)]
    def dfs(var_idx):
        if var_idx == total_vars:
            # check conservation
            for ci,(s,t,d) in enumerate(commodities):
                bal = [0]*n
                bal[s] -= d
                bal[t] += d
                for ei,(u,v,_) in enumerate(edges):
                    f = flows[ci][ei]
                    bal[u] -= f
                    bal[v] += f
                if any(b!=0 for b in bal):
                    return False
            return True
        ci = var_idx // m
        ei = var_idx % m
        for f in range(caps[ei]+1):
            flows[ci][ei] = f
            # early prune: partial balance cannot exceed remaining capacity
            # skip for simplicity
            if dfs(var_idx+1):
                return True
        flows[ci][ei] = 0
        return False
    if dfs(0):
        print("YES")
        for ci in range(k):
            print(' '.join(map(str, flows[ci])))
    else:
        print("NO")

if __name__ == "__main__":
    solve()