import sys

def solve():
    input = sys.stdin.readline
    k, t = map(int, input().split())
    triples = []
    for _ in range(t):
        x, y, z = map(int, input().split())
        triples.append((x-1, y-1, z-1))
    
    # Group by time slot
    by_time = [[] for _ in range(k)]
    for x, y, z in triples:
        by_time[z].append((x, y))
    
    # For each time slot, we need to pick a distinct (specialist, machine) pair
    # We'll do backtracking over time slots, using bitmasks for specialists and machines.
    
    used_spec = 0
    used_mach = 0
    chosen = [None] * k
    
    # Precompute for each time slot the list of (spec_mask, mach_mask) pairs
    time_options = []
    for z in range(k):
        opts = []
        for x, y in by_time[z]:
            opts.append((1 << x, 1 << y, x, y))
        time_options.append(opts)
    
    # Sort time slots by number of options (smallest first) for pruning
    order = sorted(range(k), key=lambda z: len(time_options[z]))
    
    def dfs(idx):
        if idx == k:
            return True
        z = order[idx]
        for sm, mm, x, y in time_options[z]:
            if (used_spec & sm) == 0 and (used_mach & mm) == 0:
                chosen[z] = (x, y)
                nonlocal_used_spec = used_spec
                nonlocal_used_mach = used_mach
                # We need to modify outer variables, so use a list or return values
                # Instead, we'll use a mutable container
                # Actually, we can use a list for used masks
                # Let's restructure with lists
                pass
        return False
    
    # Restructure with lists for used masks
    used = [0, 0]  # spec, mach
    chosen = [None] * k
    
    def dfs(idx):
        if idx == k:
            return True
        z = order[idx]
        for sm, mm, x, y in time_options[z]:
            if (used[0] & sm) == 0 and (used[1] & mm) == 0:
                used[0] |= sm
                used[1] |= mm
                chosen[z] = (x, y)
                if dfs(idx+1):
                    return True
                used[0] ^= sm
                used[1] ^= mm
                chosen[z] = None
        return False
    
    if dfs(0):
        print("YES")
        for z in range(k):
            x, y = chosen[z]
            print(x+1, y+1, z+1)
    else:
        print("NO")

if __name__ == "__main__":
    solve()