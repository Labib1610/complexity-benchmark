import sys

def solve():
    input = sys.stdin.readline
    k, t = map(int, input().split())
    relays = []
    for _ in range(t):
        a, b, c = map(int, input().split())
        relays.append((a-1, b-1, c-1))  # 0-index for bitmask

    # Group by first coordinate
    by_first = [[] for _ in range(k)]
    for idx, (a,b,c) in enumerate(relays):
        by_first[a].append((b,c,idx))

    # For MRV, we need to know which first values are still unassigned
    used_first = 0
    used_second = 0
    used_third = 0
    chosen = [None]*k

    # Precompute for each first value the list of (second, third, relay_index)
    # We'll sort by number of options maybe

    def dfs(mask_first, mask_second, mask_third):
        if mask_first == (1<<k)-1:
            return True
        # Choose the first value with fewest remaining options
        best_val = -1
        best_options = None
        for v in range(k):
            if not (mask_first >> v) & 1:
                opts = []
                for b,c,idx in by_first[v]:
                    if not (mask_second >> b) & 1 and not (mask_third >> c) & 1:
                        opts.append((b,c,idx))
                if best_val == -1 or len(opts) < len(best_options):
                    best_val = v
                    best_options = opts
                    if len(opts) == 0:
                        break
        if not best_options:
            return False
        # Try each option
        for b,c,idx in best_options:
            chosen[best_val] = relays[idx]
            if dfs(mask_first | (1<<best_val), mask_second | (1<<b), mask_third | (1<<c)):
                return True
        return False

    if dfs(0,0,0):
        print("YES")
        for a,b,c in chosen:
            print(a+1, b+1, c+1)
    else:
        print("NO")

if __name__ == "__main__":
    solve()