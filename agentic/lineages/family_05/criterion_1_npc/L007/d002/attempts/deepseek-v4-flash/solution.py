import sys
sys.setrecursionlimit(1000000)

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    k = int(next(it))
    t = int(next(it))
    
    # For each chassis, store list of (n, i) pairs
    options = [[] for _ in range(k)]
    for _ in range(t):
        c = int(next(it)) - 1
        n = int(next(it)) - 1
        i = int(next(it)) - 1
        options[c].append((n, i))
    
    # Sort chassis by number of options (smallest domain first)
    order = sorted(range(k), key=lambda x: len(options[x]))
    
    # We'll map back to original chassis index
    # We'll store result as list of (c, n, i)
    result = [None] * k
    
    # Precompute for each chassis the list of (n, i) pairs
    # We'll use bitmasks for n and i
    
    # Backtracking function
    def backtrack(idx, used_n, used_i):
        if idx == k:
            return True
        c = order[idx]
        for n, i in options[c]:
            if (used_n >> n) & 1:
                continue
            if (used_i >> i) & 1:
                continue
            result[c] = (c+1, n+1, i+1)
            if backtrack(idx+1, used_n | (1 << n), used_i | (1 << i)):
                return True
        return False
    
    if backtrack(0, 0, 0):
        print("YES")
        for c, n, i in result:
            print(c, n, i)
    else:
        print("NO")

if __name__ == "__main__":
    solve()