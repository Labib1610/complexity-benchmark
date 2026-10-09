import sys

def solve():
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    it = iter(input_data)
    q = int(next(it))
    t = int(next(it))
    n = 3 * q
    trios = []
    for _ in range(t):
        a = int(next(it)) - 1
        b = int(next(it)) - 1
        c = int(next(it)) - 1
        mask = (1 << a) | (1 << b) | (1 << c)
        trios.append((mask, a, b, c))
    
    # For each operator, list indices of trios containing it
    by_operator = [[] for _ in range(n)]
    for idx, (mask, a, b, c) in enumerate(trios):
        by_operator[a].append(idx)
        by_operator[b].append(idx)
        by_operator[c].append(idx)
    
    full_mask = (1 << n) - 1
    memo = {}
    chosen = []
    
    def dfs(remaining):
        if remaining == 0:
            return True
        if remaining in memo:
            return False
        # find first uncovered operator
        # lowest set bit
        lsb = remaining & -remaining
        op = (lsb.bit_length() - 1)
        for idx in by_operator[op]:
            mask, a, b, c = trios[idx]
            if mask & remaining == mask:  # all three still available
                chosen.append((a+1, b+1, c+1))
                if dfs(remaining ^ mask):
                    return True
                chosen.pop()
        memo[remaining] = False
        return False
    
    if dfs(full_mask):
        print("YES")
        for a, b, c in chosen:
            print(a, b, c)
    else:
        print("NO")

if __name__ == "__main__":
    solve()