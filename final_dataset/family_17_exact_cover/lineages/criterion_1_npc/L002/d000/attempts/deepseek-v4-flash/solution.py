import sys

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
        mask = (1 << a) | (1 << b) | (1 << c)
        triples.append((mask, (a+1, b+1, c+1)))
    
    # For each operator, list indices of triples containing it
    op_to_triples = [[] for _ in range(n)]
    for idx, (mask, _) in enumerate(triples):
        m = mask
        while m:
            lsb = m & -m
            op = (lsb.bit_length() - 1)
            op_to_triples[op].append(idx)
            m ^= lsb
    
    full_mask = (1 << n) - 1
    chosen = []
    
    # Recursive backtracking
    def dfs(covered_mask):
        if covered_mask == full_mask:
            return True
        # Find operator with fewest available triples
        best_op = -1
        best_list = None
        for op in range(n):
            if not (covered_mask >> op) & 1:
                # filter triples that don't conflict
                avail = [idx for idx in op_to_triples[op] if (triples[idx][0] & covered_mask) == 0]
                if best_op == -1 or len(avail) < len(best_list):
                    best_op = op
                    best_list = avail
                    if len(best_list) == 0:
                        return False
                    if len(best_list) == 1:
                        break
        # Try each candidate triple
        for idx in best_list:
            mask, vals = triples[idx]
            chosen.append(vals)
            if dfs(covered_mask | mask):
                return True
            chosen.pop()
        return False
    
    if dfs(0):
        print("YES")
        for vals in chosen:
            print(*vals)
    else:
        print("NO")

if __name__ == "__main__":
    solve()