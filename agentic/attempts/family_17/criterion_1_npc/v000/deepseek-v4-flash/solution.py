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
        a = int(next(it))
        b = int(next(it))
        c = int(next(it))
        triples.append((a - 1, b - 1, c - 1))  # 0-based
    
    n_elem = 3 * q
    # Build element -> list of triple indices
    elem_to_triples = [[] for _ in range(n_elem)]
    for idx, (a, b, c) in enumerate(triples):
        elem_to_triples[a].append(idx)
        elem_to_triples[b].append(idx)
        elem_to_triples[c].append(idx)
    
    full_mask = (1 << n_elem) - 1
    chosen = []
    
    # Recursive backtracking with MRV
    def dfs(remaining_mask):
        if remaining_mask == 0:
            return True
        # Find uncovered element with smallest number of available triples
        # We'll iterate over set bits
        temp = remaining_mask
        best_elem = -1
        best_count = float('inf')
        # Get first few bits to test
        while temp:
            lsb = temp & -temp
            elem = (lsb.bit_length() - 1)
            cnt = 0
            # count triples fully inside remaining
            for idx in elem_to_triples[elem]:
                a, b, c = triples[idx]
                if (remaining_mask >> a) & 1 and (remaining_mask >> b) & 1 and (remaining_mask >> c) & 1:
                    cnt += 1
            if cnt < best_count:
                best_count = cnt
                best_elem = elem
                if cnt == 0:
                    break
            temp -= lsb
        
        if best_count == 0:
            return False
        
        # Try triples for best_elem
        for idx in elem_to_triples[best_elem]:
            a, b, c = triples[idx]
            if (remaining_mask >> a) & 1 and (remaining_mask >> b) & 1 and (remaining_mask >> c) & 1:
                # Use this triple
                chosen.append((a + 1, b + 1, c + 1))
                new_mask = remaining_mask & ~((1 << a) | (1 << b) | (1 << c))
                if dfs(new_mask):
                    return True
                chosen.pop()
        return False
    
    if dfs(full_mask):
        print("YES")
        for tri in chosen:
            print(*tri)
    else:
        print("NO")

if __name__ == "__main__":
    solve()