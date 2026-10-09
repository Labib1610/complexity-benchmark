import sys
sys.setrecursionlimit(10000)

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    q = int(next(it))
    t = int(next(it))
    N = 3 * q
    triples = []
    for _ in range(t):
        a = int(next(it)); b = int(next(it)); c = int(next(it))
        triples.append((a, b, c))
    
    # Build for each number list of triple indices
    triples_for_num = [[] for _ in range(N+1)]
    triple_masks = []
    for idx, (a,b,c) in enumerate(triples):
        mask = (1 << a) | (1 << b) | (1 << c)
        triple_masks.append(mask)
        triples_for_num[a].append(idx)
        triples_for_num[b].append(idx)
        triples_for_num[c].append(idx)
    
    # Precompute candidate triples for each number (those where all numbers are in set)
    # We can filter on the fly.
    
    full_mask = (1 << (N+1)) - 2
    chosen = []
    
    def rec(uncovered):
        if uncovered == 0:
            return True
        # pick number with fewest candidates
        best_num = -1
        best_list = None
        # iterate over set bits
        m = uncovered
        while m:
            bit = m & -m
            num = bit.bit_length() - 1
            # filter candidates
            cand = [idx for idx in triples_for_num[num] if (triple_masks[idx] & uncovered) == triple_masks[idx]]
            if not cand:
                return False
            if best_num == -1 or len(cand) < len(best_list):
                best_num = num
                best_list = cand
                if len(best_list) == 1:
                    # can't get better
                    break
            m -= bit
        
        for idx in best_list:
            mask = triple_masks[idx]
            if (mask & uncovered) == mask:
                chosen.append(idx)
                if rec(uncovered & ~mask):
                    return True
                chosen.pop()
        return False
    
    if rec(full_mask):
        print("YES")
        out_lines = []
        for idx in chosen:
            a,b,c = triples[idx]
            out_lines.append(f"{a} {b} {c}")
        print("\n".join(out_lines))
    else:
        print("NO")

if __name__ == "__main__":
    solve()