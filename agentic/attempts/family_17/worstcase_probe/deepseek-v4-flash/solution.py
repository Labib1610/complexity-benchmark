import sys

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    q = int(next(it))
    t = int(next(it))
    n = 3 * q
    triples = []
    for _ in range(t):
        a = int(next(it)) - 1
        b = int(next(it)) - 1
        c = int(next(it)) - 1
        triples.append((a, b, c))
    
    # Build mapping from number to triples
    num_to_triples = [[] for _ in range(n)]
    for idx, (a, b, c) in enumerate(triples):
        num_to_triples[a].append(idx)
        num_to_triples[b].append(idx)
        num_to_triples[c].append(idx)
    
    # Precompute bitmask for each triple
    triple_mask = []
    for a, b, c in triples:
        mask = (1 << a) | (1 << b) | (1 << c)
        triple_mask.append(mask)
    
    used = [False] * t
    chosen = []
    cover_count = 0
    
    # For fast removal, we can maintain a list of active triples per number
    # But we'll use a simple backtracking with used array.
    
    # We'll implement recursive search with MRV.
    # To speed up, we can maintain a list of numbers not yet covered.
    # But we can also just scan for the number with fewest available triples.
    
    # We'll use a recursive function.
    # We'll pass the current set of covered numbers as a bitmask? n up to 600, so bitmask not possible.
    # Instead, we'll maintain covered boolean array.
    
    covered = [False] * n
    
    # For each number, we can compute the list of triples that are still available (not used and not conflicting)
    # But we can just filter on the fly.
    
    # To speed up, we can maintain for each number a list of triples that contain it and are still usable.
    # But when we choose a triple, we need to remove all triples that share any number with it.
    # We can do that by marking used.
    
    # We'll implement a recursive function with parameters: current chosen count, covered count.
    
    # We'll use a list of active triples per number, but we need to update it when we choose a triple.
    # Since t <= 20000, we can afford O(t) per recursion if needed, but we need to be careful.
    
    # Let's implement with a "candidate" list per number, but we'll filter using used array.
    
    # MRV: find uncovered number with fewest available triples.
    
    import sys
    sys.setrecursionlimit(1000000)
    
    # We'll store chosen triples as list of indices.
    
    # We'll implement a recursive function.
    # We'll pass the current covered count.
    
    # To speed up, we can maintain a list of uncovered numbers.
    # But we can just scan all numbers each time.
    
    # Let's implement with a simple backtracking.
    
    # We'll also add a check: if cover_count == n, we are done.
    
    # We'll use a "candidate" list for each number: list of triple indices that contain it and are not used.
    # But when we choose a triple, we need to remove all triples that share any number with it.
    # We can do that by marking used, and when we iterate candidates for a number, we skip used triples.
    
    # However, we also need to know which triples are still available for a given number.
    # We can just iterate over all triples containing that number and check if used is False.
    
    # Let's implement.
    
    # We'll also add a heuristic: sort numbers by number of available triples.
    
    # We'll implement a recursive function with memoization? Not needed.
    
    # Let's write the backtracking.
    
    def backtrack():
        nonlocal cover_count
        if cover_count == n:
            return True
        # Find uncovered number with fewest available triples
        best_num = -1
        best_count = float('inf')
        for num in range(n):
            if not covered[num]:
                cnt = 0
                for tidx in num_to_triples[num]:
                    if not used[tidx]:
                        cnt += 1
                        if cnt >= best_count:
                            break
                if cnt < best_count:
                    best_count = cnt
                    best_num = num
                    if cnt == 0:
                        break
        if best_count == 0:
            return False
        # Try each available triple for best_num
        # Sort triples by some heuristic? Maybe by number of conflicts.
        candidates = []
        for tidx in num_to_triples[best_num]:
            if not used[tidx]:
                candidates.append(tidx)
        # Sort candidates by the number of uncovered numbers they cover? They all cover 3, but some may cover already covered? No, they cover exactly 3 numbers, but some may be already covered? Actually, if a triple contains a number already covered, it's not usable because that would overlap. So we only consider triples where all three numbers are uncovered.
        # Wait: we need to ensure that the triple doesn't contain any covered number. Because if it does, it would overlap. So we must filter triples that have all three numbers uncovered.
        # So we need to check that for each candidate triple, all its numbers are uncovered.
        # Let's do that.
        valid_candidates = []
        for tidx in candidates:
            a, b, c = triples[tidx]
            if not covered[a] and not covered[b] and not covered[c]:
                valid_candidates.append(tidx)
        if not valid_candidates:
            return False
        # Sort by some heuristic: maybe by the number of uncovered numbers that become "hard"?
        # We'll just try in order.
        for tidx in valid_candidates:
            a, b, c = triples[tidx]
            # Choose
            used[tidx] = True
            covered[a] = covered[b] = covered[c] = True
            chosen.append(tidx)
            cover_count += 3
            if backtrack():
                return True
            # Undo
            chosen.pop()
            covered[a] = covered[b] = covered[c] = False
            used[tidx] = False
            cover_count -= 3
        return False
    
    if backtrack():
        out = ["YES"]
        for idx in chosen:
            a, b, c = triples[idx]
            out.append(f"{a+1} {b+1} {c+1}")
        sys.stdout.write("\n".join(out))
    else:
        sys.stdout.write("NO")

if __name__ == "__main__":
    solve()