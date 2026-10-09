import sys
sys.setrecursionlimit(1000000)

def solve():
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
    cap = []
    adj = [[] for _ in range(n)]
    for idx in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        c = int(next(it))
        edges.append((u, v))
        cap.append(c)
        adj[u].append(idx)
    
    # We'll do a DFS per commodity, assigning flows on edges.
    # To reduce search space, we can precompute all simple paths for each commodity.
    # Then try to combine path flows.
    
    # Precompute all simple paths for each commodity
    all_paths = []
    for s, t, d in commodities:
        paths = []
        def dfs(u, path, visited):
            if u == t:
                paths.append(path[:])
                return
            for eidx in adj[u]:
                v = edges[eidx][1]
                if v not in visited:
                    visited.add(v)
                    path.append(eidx)
                    dfs(v, path, visited)
                    path.pop()
                    visited.remove(v)
        dfs(s, [], {s})
        all_paths.append(paths)
    
    # Now we need to select flows on paths for each commodity such that total edge flow <= cap.
    # This is a multi-commodity flow on paths.
    # We'll use backtracking over commodities, trying to assign flow to paths.
    
    edge_flow = [0] * m
    result_flows = [None] * k
    
    def backtrack(ci):
        if ci == k:
            return True
        s, t, d = commodities[ci]
        paths = all_paths[ci]
        # Try to assign d units among paths
        # We'll do recursive assignment of units to paths
        # To speed up, we can use DP or just brute force with pruning.
        # Since d may be large, we need a smarter way.
        # We'll use a recursive function that tries to push flow along paths.
        
        # We'll use a DFS that tries to send flow along each path, respecting remaining capacity.
        # This is like a flow decomposition.
        
        # We'll try to send as much as possible along each path, but need to ensure feasibility.
        # Use recursion with remaining demand.
        
        def assign_paths(pi, remaining, flows):
            if remaining == 0:
                # Check if all paths considered? Actually we can stop early.
                # Save flows
                for pidx, f in flows:
                    for e in paths[pidx]:
                        edge_flow[e] += f
                result_flows[ci] = [0]*m
                for pidx, f in flows:
                    for e in paths[pidx]:
                        result_flows[ci][e] += f
                if backtrack(ci+1):
                    return True
                # revert
                for pidx, f in flows:
                    for e in paths[pidx]:
                        edge_flow[e] -= f
                return False
            if pi == len(paths):
                return False
            # Try to send x units along path pi
            max_possible = min(remaining, min(cap[e] - edge_flow[e] for e in paths[pi]))
            for x in range(max_possible, -1, -1):
                if x == 0:
                    if assign_paths(pi+1, remaining, flows):
                        return True
                else:
                    # check capacity
                    if all(edge_flow[e] + x <= cap[e] for e in paths[pi]):
                        flows.append((pi, x))
                        for e in paths[pi]:
                            edge_flow[e] += x
                        if assign_paths(pi+1, remaining - x, flows):
                            return True
                        for e in paths[pi]:
                            edge_flow[e] -= x
                        flows.pop()
            return False
        
        if assign_paths(0, d, []):
            return True
        return False
    
    if backtrack(0):
        print("YES")
        for i in range(k):
            print(' '.join(str(result_flows[i][j]) for j in range(m)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()