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
        triples.append((a, b, c, mask))
    
    # Sort triples by first element, then second, then third
    triples.sort(key=lambda x: (x[0], x[1], x[2]))
    
    # For each position, list of triples that contain it
    by_first = [[] for _ in range(n)]
    for idx, (a, b, c, mask) in enumerate(triples):
        by_first[a].append(idx)
    
    full_mask = (1 << n) - 1
    chosen = []
    
    # Recursive search
    def dfs(covered):
        if covered == full_mask:
            return True
        # Find first uncovered operator
        # Use bit trick to find lowest zero bit
        inv = (~covered) & full_mask
        # lowest set bit
        first = (inv & -inv).bit_length() - 1
        for idx in by_first[first]:
            a, b, c, mask = triples[idx]
            if covered & mask:
                continue
            chosen.append((a+1, b+1, c+1))
            if dfs(covered | mask):
                return True
            chosen.pop()
        return False
    
    if dfs(0):
        print("YES")
        for a, b, c in chosen:
            print(a, b, c)
    else:
        print("NO")

if __name__ == "__main__":
    solve()