import sys

def solve():
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    B = int(next(it))
    
    edges = []
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        edges.append((u, v))
    
    # Precompute adjacency for faster cost calculation
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    
    # We'll do backtracking with pruning
    best_perm = None
    found = False
    
    # We'll try to place modules one by one into positions 0..n-1
    # perm[pos] = module at that position
    perm = [-1] * n
    used = [False] * n
    
    # Precompute edge list for cost calculation
    edge_list = edges
    
    def current_cost():
        # Compute cost for current partial placement
        # Only count edges where both endpoints are placed
        pos_of = [-1] * n
        for i, mod in enumerate(perm):
            if mod != -1:
                pos_of[mod] = i
        cost = 0
        for u, v in edge_list:
            if pos_of[u] != -1 and pos_of[v] != -1:
                cost += abs(pos_of[u] - pos_of[v])
        return cost
    
    def dfs(pos, cost_so_far):
        nonlocal found, best_perm
        if found:
            return
        if cost_so_far > B:
            return
        if pos == n:
            # All placed
            if cost_so_far <= B:
                found = True
                best_perm = perm[:]
            return
        
        # Try placing each unused module at this position
        for mod in range(n):
            if not used[mod]:
                # Place
                perm[pos] = mod
                used[mod] = True
                # Compute new cost incrementally
                new_cost = cost_so_far
                # Only edges to already placed modules
                for neighbor in adj[mod]:
                    if used[neighbor]:
                        # neighbor is placed somewhere
                        # find its position
                        for p in range(pos):
                            if perm[p] == neighbor:
                                new_cost += abs(pos - p)
                                break
                dfs(pos + 1, new_cost)
                # Backtrack
                used[mod] = False
                perm[pos] = -1
                if found:
                    return
    
    dfs(0, 0)
    
    if found:
        # Output positions: bay position of module i (1-indexed)
        # best_perm[pos] = module at position pos
        # We need output: for module 1..n, its bay position
        result = [0] * n
        for bay, mod in enumerate(best_perm):
            result[mod] = bay + 1
        print("YES")
        print(" ".join(map(str, result)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()