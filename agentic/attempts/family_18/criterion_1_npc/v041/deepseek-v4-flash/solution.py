import sys

sys.setrecursionlimit(10000000)

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    B = int(next(it))
    edges = []
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        edges.append((u, v))
        adj[u].append(v)
        adj[v].append(u)
    
    # If n small enough, we can use backtracking
    # Let's try all permutations for n <= 10; for bigger, try heuristic
    # But we can still attempt backtracking if n<=12 or so; if fails quickly?
    # We'll use recursion with pruning.

    pos = [-1] * n
    used = [False] * (n + 1)  # bay indices 1..n
    best_perm = None

    # Precompute edge list for quick cost computation
    # When placing artifact idx at position p, we can add cost for edges to already placed ones

    def backtrack(idx, cost):
        nonlocal best_perm
        if cost > B:
            return
        if idx == n:
            if cost <= B:
                best_perm = pos[:]
            return
        # Try placing artifact idx at some bay
        # Heuristic: try to place near already placed neighbors to reduce cost
        # We'll try all unused bays
        for bay in range(1, n + 1):
            if used[bay]:
                continue
            # compute added cost
            added = 0
            for nb in adj[idx]:
                if pos[nb] != -1:
                    added += abs(pos[nb] - bay)
            if cost + added > B:
                continue
            # place
            pos[idx] = bay
            used[bay] = True
            backtrack(idx + 1, cost + added)
            used[bay] = False
            pos[idx] = -1
            if best_perm is not None:
                return
    
    backtrack(0, 0)
    
    if best_perm is not None:
        print("YES")
        print(" ".join(str(x) for x in best_perm))
    else:
        print("NO")

if __name__ == "__main__":
    solve()