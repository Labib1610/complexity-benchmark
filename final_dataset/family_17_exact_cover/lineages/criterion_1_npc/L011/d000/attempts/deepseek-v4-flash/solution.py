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
        mask = (1 << a) | (1 << b) | (1 << c)
        triples.append(mask)
    
    n = 3 * q
    full_mask = (1 << n) - 1
    
    # For each operator, list of triple indices containing it
    by_operator = [[] for _ in range(n)]
    for idx, mask in enumerate(triples):
        for i in range(n):
            if mask & (1 << i):
                by_operator[i].append(idx)
    
    chosen = []
    
    def backtrack(covered):
        if covered == full_mask:
            return True
        # find first uncovered operator
        # we can use bit trick: ~covered & full_mask gives uncovered bits
        uncovered = (~covered) & full_mask
        # get lowest set bit
        first = (uncovered & -uncovered).bit_length() - 1
        for idx in by_operator[first]:
            mask = triples[idx]
            if mask & covered:
                continue
            chosen.append(idx)
            if backtrack(covered | mask):
                return True
            chosen.pop()
        return False
    
    if backtrack(0):
        sys.stdout.write("YES\n")
        for idx in chosen:
            mask = triples[idx]
            # extract the three numbers
            nums = []
            for i in range(n):
                if mask & (1 << i):
                    nums.append(str(i + 1))
            sys.stdout.write(" ".join(nums) + "\n")
    else:
        sys.stdout.write("NO\n")

if __name__ == "__main__":
    solve()