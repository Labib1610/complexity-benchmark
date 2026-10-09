import sys

def solve():
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    it = iter(input_data)
    q = int(next(it))
    t = int(next(it))
    triples = []
    for _ in range(t):
        a = int(next(it)) - 1
        b = int(next(it)) - 1
        c = int(next(it)) - 1
        triples.append((a, b, c))
    
    n = 3 * q
    # Sort triples by first element for better pruning
    triples.sort(key=lambda x: (x[0], x[1], x[2]))
    
    # Precompute adjacency: for each atom, list of triple indices
    adj = [[] for _ in range(n)]
    for idx, (a, b, c) in enumerate(triples):
        adj[a].append(idx)
        adj[b].append(idx)
        adj[c].append(idx)
    
    used = [False] * t
    chosen = []
    full_mask = (1 << n) - 1
    
    # Recursive backtracking
    def dfs(mask):
        if mask == full_mask:
            return True
        # Find first uncovered atom
        # Use bit trick to find lowest zero bit
        # Since n <= 600, we can loop
        first = 0
        while first < n and (mask >> first) & 1:
            first += 1
        if first == n:
            return mask == full_mask
        # Try triples covering this atom
        for idx in adj[first]:
            if used[idx]:
                continue
            a, b, c = triples[idx]
            if (mask >> a) & 1 or (mask >> b) & 1 or (mask >> c) & 1:
                continue
            used[idx] = True
            chosen.append((a, b, c))
            new_mask = mask | (1 << a) | (1 << b) | (1 << c)
            if dfs(new_mask):
                return True
            chosen.pop()
            used[idx] = False
        return False
    
    if dfs(0):
        print("YES")
        for a, b, c in chosen:
            print(a + 1, b + 1, c + 1)
    else:
        print("NO")

if __name__ == "__main__":
    solve()