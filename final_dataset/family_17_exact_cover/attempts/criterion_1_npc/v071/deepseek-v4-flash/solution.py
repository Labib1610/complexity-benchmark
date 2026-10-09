import sys

def solve():
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    q = int(input_data[0])
    t = int(input_data[1])
    triples = []
    idx = 2
    for _ in range(t):
        a = int(input_data[idx]) - 1
        b = int(input_data[idx+1]) - 1
        c = int(input_data[idx+2]) - 1
        idx += 3
        mask = (1 << a) | (1 << b) | (1 << c)
        triples.append((mask, a, b, c))
    
    # Group triples by their smallest element for faster lookup
    by_min = [[] for _ in range(3*q)]
    for mask, a, b, c in triples:
        m = min(a, b, c)
        by_min[m].append((mask, a, b, c))
    
    full_mask = (1 << (3*q)) - 1
    used = 0
    chosen = []
    
    # Precompute the smallest unused number quickly
    # We'll just scan each time; q ≤ 200 so fine.
    
    def backtrack(used, chosen):
        if used == full_mask:
            return True
        # find smallest unused
        # We can use bit trick: ~used & full_mask gives unused bits
        unused = (~used) & full_mask
        # get lowest set bit
        low = unused & -unused
        person = (low.bit_length() - 1)
        for mask, a, b, c in by_min[person]:
            if used & mask == 0:
                chosen.append((a+1, b+1, c+1))
                if backtrack(used | mask, chosen):
                    return True
                chosen.pop()
        return False
    
    if backtrack(0, chosen):
        print("YES")
        for a, b, c in chosen:
            print(a, b, c)
    else:
        print("NO")

if __name__ == "__main__":
    solve()