import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    k = int(data[0])
    t = int(data[1])
    triples = []
    idx = 2
    for _ in range(t):
        x = int(data[idx]); y = int(data[idx+1]); z = int(data[idx+2])
        idx += 3
        triples.append((x, y, z))
    
    # Build adjacency: conflict if share x, y, or z
    # We need independent set of size k in conflict graph
    # k <= 22, use meet-in-the-middle or backtracking with pruning
    
    # Precompute conflicts as bitmask
    n = t
    conflict = [0]*n
    for i in range(n):
        xi, yi, zi = triples[i]
        mask = 0
        for j in range(n):
            if i == j:
                continue
            xj, yj, zj = triples[j]
            if xi == xj or yi == yj or zi == zj:
                mask |= (1 << j)
        conflict[i] = mask
    
    # Try greedy + backtracking
    # Sort by degree (number of conflicts)
    order = sorted(range(n), key=lambda i: bin(conflict[i]).count('1'))
    
    best = []
    best_mask = 0
    
    # Use recursive backtracking with pruning
    def backtrack(pos, count, mask, chosen):
        nonlocal best, best_mask
        if count == k:
            best = chosen[:]
            best_mask = mask
            return True
        if pos == n:
            return False
        remaining = n - pos
        if count + remaining < k:
            return False
        # Upper bound: count + remaining
        for i in range(pos, n):
            if count + (n - i) < k:
                return False
            if (mask & conflict[order[i]]) == 0:
                # Check if this node conflicts with any already chosen
                # conflict[order[i]] already includes all conflicts
                chosen.append(order[i])
                if backtrack(i+1, count+1, mask | (1 << order[i]), chosen):
                    return True
                chosen.pop()
        return False
    
    if backtrack(0, 0, 0, []):
        print("YES")
        for idx2 in best:
            x, y, z = triples[idx2]
            print(f"{x} {y} {z}")
    else:
        print("NO")

solve()