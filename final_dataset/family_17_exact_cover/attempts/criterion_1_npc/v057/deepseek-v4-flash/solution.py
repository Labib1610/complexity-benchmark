import sys
sys.setrecursionlimit(1000000)

def solve():
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    it = iter(input_data)
    q = int(next(it))
    t = int(next(it))
    n = 3 * q
    
    triples = []
    for _ in range(t):
        a = int(next(it)) - 1
        b = int(next(it)) - 1
        c = int(next(it)) - 1
        triples.append((a, b, c))
    
    # For each operator, list indices of triples containing them
    avail = [[] for _ in range(n)]
    for idx, (a, b, c) in enumerate(triples):
        avail[a].append(idx)
        avail[b].append(idx)
        avail[c].append(idx)
    
    # For pruning, sort triple lists by size maybe
    # But we will use MRV on operator availability at each step
    
    chosen = []
    used = [False] * t
    covered = [False] * n
    
    # Precompute triple's members for quick access
    triple_members = [ (a, b, c) for a, b, c in triples ]
    
    def backtrack():
        if len(chosen) == q:
            return True
        # Find uncovered operator with minimal options
        best_op = -1
        best_opts = []
        for op in range(n):
            if not covered[op]:
                opts = [idx for idx in avail[op] if not used[idx]]
                if not opts:
                    return False
                if best_op == -1 or len(opts) < len(best_opts):
                    best_op = op
                    best_opts = opts
                    if len(opts) == 1:
                        break
        if best_op == -1:
            return False
        
        # Sort options maybe by how many new operators they cover
        # But since all triples cover exactly 3 uncovered? Not necessarily—some may overlap with covered
        # Better: choose triples that cover the most uncovered operators
        best_opts.sort(key=lambda idx: -len([x for x in triple_members[idx] if not covered[x]]))
        
        for idx in best_opts:
            a, b, c = triple_members[idx]
            # Check if all three are uncovered
            if covered[a] or covered[b] or covered[c]:
                continue
            # Use this triple
            used[idx] = True
            covered[a] = covered[b] = covered[c] = True
            chosen.append((a+1, b+1, c+1))
            if backtrack():
                return True
            # Backtrack
            chosen.pop()
            covered[a] = covered[b] = covered[c] = False
            used[idx] = False
        return False
    
    if backtrack():
        print("YES")
        for a, b, c in chosen:
            print(a, b, c)
    else:
        print("NO")

if __name__ == "__main__":
    solve()