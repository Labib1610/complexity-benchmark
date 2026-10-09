import sys

def solve():
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    n, m, B = map(int, input_data[:3])
    edges = []
    idx = 3
    for _ in range(m):
        u = int(input_data[idx]) - 1
        v = int(input_data[idx+1]) - 1
        idx += 2
        edges.append((u, v))
    
    # adjacency list for faster cost computation
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    
    # Precompute edge list for cost calculation
    # We'll use backtracking
    phase = [-1] * n
    used = [False] * (n + 1)
    
    # We'll compute cost incrementally
    # When we assign a phase to a node, we can compute cost with already assigned neighbors
    # But since we assign one by one, we can compute partial cost when both endpoints are assigned.
    
    # We'll store partial cost
    current_cost = 0
    
    # For pruning, we can compute a lower bound: for each unassigned edge, min possible contribution is 1 (if adjacent phases)
    # But simple pruning with current_cost > B is enough for small n.
    
    result = None
    
    def backtrack(pos):
        nonlocal current_cost, result
        if current_cost > B:
            return
        if pos == n:
            result = phase[:]
            return True
        
        # Try phases in some order (maybe 1..n)
        for p in range(1, n+1):
            if not used[p]:
                # assign
                phase[pos] = p
                used[p] = True
                # compute added cost with already assigned neighbors
                added = 0
                for nb in adj[pos]:
                    if phase[nb] != -1:
                        added += abs(p - phase[nb])
                current_cost += added
                if current_cost <= B:
                    if backtrack(pos + 1):
                        return True
                current_cost -= added
                used[p] = False
                phase[pos] = -1
        return False
    
    if backtrack(0):
        print("YES")
        print(" ".join(str(x) for x in result))
    else:
        print("NO")

if __name__ == "__main__":
    solve()