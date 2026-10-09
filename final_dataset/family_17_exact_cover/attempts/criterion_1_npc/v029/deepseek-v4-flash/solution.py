import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    q = int(data[0])
    t = int(data[1])
    groups = []
    idx = 2
    for _ in range(t):
        a = int(data[idx]) - 1
        b = int(data[idx+1]) - 1
        c = int(data[idx+2]) - 1
        idx += 3
        mask = (1 << a) | (1 << b) | (1 << c)
        groups.append(mask)
    
    full_mask = (1 << (3*q)) - 1
    n = len(groups)
    
    # Precompute groups containing each operator for fast lookup
    by_op = [[] for _ in range(3*q)]
    for i, mask in enumerate(groups):
        m = mask
        while m:
            lsb = m & -m
            op = (lsb.bit_length() - 1)
            by_op[op].append(i)
            m -= lsb
    
    used = 0
    chosen = []
    
    # Precompute the lowest zero bit for any used mask from 0..full_mask? That's too large,
    # but we can just compute each time with bit operations — negligible overhead.
    
    def backtrack(used_mask, chosen_list):
        if used_mask == full_mask:
            return True
        # Find first unused operator
        # using bit trick: ~used_mask & full_mask gives zero bits, then find lowest set bit
        free = ~used_mask & full_mask
        # lowest set bit:
        op = (free & -free).bit_length() - 1
        # try groups containing op
        for gid in by_op[op]:
            mask = groups[gid]
            if used_mask & mask:
                continue
            chosen_list.append(gid)
            if backtrack(used_mask | mask, chosen_list):
                return True
            chosen_list.pop()
        return False
    
    if backtrack(0, chosen):
        print("YES")
        for gid in chosen:
            mask = groups[gid]
            nums = [i+1 for i in range(3*q) if (mask >> i) & 1]
            print(*nums)
    else:
        print("NO")

if __name__ == "__main__":
    solve()