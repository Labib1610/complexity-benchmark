import sys

def solve():
    input = sys.stdin.readline
    k, t = map(int, input().split())
    # For each worker, store list of (equipment, schedule) as bitmask pairs
    worker_options = [[] for _ in range(k)]
    for _ in range(t):
        x, y, z = map(int, input().split())
        x -= 1
        y -= 1
        z -= 1
        worker_options[x].append((y, z))
    
    # Precompute for each worker a list of (eq_mask, sch_mask)
    # where eq_mask has bit y set, sch_mask has bit z set
    options = []
    for w in range(k):
        opts = []
        for y, z in worker_options[w]:
            opts.append((1 << y, 1 << z))
        options.append(opts)
    
    # We'll do backtracking with MRV
    used_eq = 0
    used_sch = 0
    assignment = [None] * k
    full_mask = (1 << k) - 1
    
    # Order workers by number of options initially
    order = sorted(range(k), key=lambda w: len(options[w]))
    
    def dfs(idx):
        nonlocal used_eq, used_sch
        if idx == k:
            return True
        w = order[idx]
        # Try options for this worker
        for eq_mask, sch_mask in options[w]:
            if (used_eq & eq_mask) == 0 and (used_sch & sch_mask) == 0:
                used_eq |= eq_mask
                used_sch |= sch_mask
                assignment[w] = (eq_mask, sch_mask)
                if dfs(idx + 1):
                    return True
                used_eq &= ~eq_mask
                used_sch &= ~sch_mask
        return False
    
    if dfs(0):
        print("YES")
        for w in range(k):
            eq_mask, sch_mask = assignment[w]
            # find bit positions
            y = (eq_mask.bit_length() - 1) + 1
            z = (sch_mask.bit_length() - 1) + 1
            print(w + 1, y, z)
    else:
        print("NO")

if __name__ == "__main__":
    solve()