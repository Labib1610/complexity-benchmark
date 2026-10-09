import sys

def solve():
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    it = iter(input_data)
    k = int(next(it))
    t = int(next(it))
    
    # candidates grouped by a
    by_a = [[] for _ in range(k+1)]
    for _ in range(t):
        a = int(next(it))
        b = int(next(it))
        c = int(next(it))
        by_a[a].append((b, c))
    
    # We need to pick exactly one from each a group (since a must be 1..k each once)
    # If any a group is empty, impossible
    for a in range(1, k+1):
        if not by_a[a]:
            print("NO")
            return
    
    # Sort groups maybe by size for better pruning
    order = list(range(1, k+1))
    order.sort(key=lambda x: len(by_a[x]))
    
    used_b = 0
    used_c = 0
    chosen = [None] * (k+1)  # chosen[a] = (b, c)
    
    def dfs(idx):
        nonlocal used_b, used_c
        if idx == k:
            return True
        a = order[idx]
        for b, c in by_a[a]:
            if (used_b >> (b-1)) & 1:
                continue
            if (used_c >> (c-1)) & 1:
                continue
            # choose
            used_b |= (1 << (b-1))
            used_c |= (1 << (c-1))
            chosen[a] = (b, c)
            if dfs(idx+1):
                return True
            # backtrack
            used_b ^= (1 << (b-1))
            used_c ^= (1 << (c-1))
            chosen[a] = None
        return False
    
    if dfs(0):
        print("YES")
        for a in range(1, k+1):
            b, c = chosen[a]
            print(a, b, c)
    else:
        print("NO")

if __name__ == "__main__":
    solve()