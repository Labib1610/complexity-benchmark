import sys
from itertools import product

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    k = int(next(it))
    
    commodities = []
    for _ in range(k):
        s = int(next(it)) - 1
        t = int(next(it)) - 1
        d = int(next(it))
        commodities.append((s, t, d))
    
    edges = []
    adj = [[] for _ in range(n)]
    for idx in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        cap = int(next(it))
        edges.append((u, v, cap))
        adj[u].append((v, idx))
    
    # For each commodity, find all simple paths from s to t
    all_paths = []  # list of list of list of edge indices
    for s, t, d in commodities:
        paths = []
        # DFS
        stack = [(s, [])]  # (node, path_edges)
        visited = [False] * n
        # We'll do simple DFS without revisiting nodes
        def dfs(u, path_edges, visited):
            if u == t:
                paths.append(path_edges[:])
                return
            for v, eidx in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    path_edges.append(eidx)
                    dfs(v, path_edges, visited)
                    path_edges.pop()
                    visited[v] = False
        visited[s] = True
        dfs(s, [], visited)
        all_paths.append(paths)
    
    # If any commodity with d>0 has no path -> impossible
    for (s, t, d), paths in zip(commodities, all_paths):
        if d > 0 and not paths:
            print("NO")
            return
    
    # Backtracking over commodities
    # We'll store current usage per edge
    usage = [0] * m
    # Result: for each commodity, a list of flows per edge
    result_flows = [None] * k
    
    # Precompute for each commodity the edge lists for each path
    # Already have all_paths
    
    # Recursive function
    def backtrack(ci):
        if ci == k:
            return True
        s, t, d = commodities[ci]
        paths = all_paths[ci]
        if d == 0:
            result_flows[ci] = [0] * m
            return backtrack(ci + 1)
        
        p = len(paths)
        # Generate all compositions of d into p non-negative integers
        # Use recursion to generate
        def gen_compositions(remaining, parts):
            if parts == 1:
                yield [remaining]
                return
            for x in range(remaining + 1):
                for rest in gen_compositions(remaining - x, parts - 1):
                    yield [x] + rest
        
        for amounts in gen_compositions(d, p):
            # Check capacity
            ok = True
            for amt, path in zip(amounts, paths):
                if amt == 0:
                    continue
                for eidx in path:
                    if usage[eidx] + amt > edges[eidx][2]:
                        ok = False
                        break
                if not ok:
                    break
            if not ok:
                continue
            # Apply
            for amt, path in zip(amounts, paths):
                if amt == 0:
                    continue
                for eidx in path:
                    usage[eidx] += amt
            # Record flows per edge for this commodity
            flow_edge = [0] * m
            for amt, path in zip(amounts, paths):
                if amt == 0:
                    continue
                for eidx in path:
                    flow_edge[eidx] += amt
            result_flows[ci] = flow_edge
            if backtrack(ci + 1):
                return True
            # Undo
            for amt, path in zip(amounts, paths):
                if amt == 0:
                    continue
                for eidx in path:
                    usage[eidx] -= amt
        return False
    
    if not backtrack(0):
        print("NO")
        return
    
    # Output
    print("YES")
    for i in range(k):
        print(' '.join(str(result_flows[i][j]) for j in range(m)))

if __name__ == "__main__":
    main()