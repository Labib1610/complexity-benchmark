import sys

def solve():
    input = sys.stdin.readline
    n, m, k = map(int, input().split())
    adj = [0] * n
    for _ in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        adj[u] |= (1 << v)
        adj[v] |= (1 << u)
    
    if k == 0:  # not possible in given constraints but safe
        print("YES")
        print()
        return
    
    left_size = n // 2
    right_size = n - left_size
    
    left_adj = [0] * left_size
    right_adj = [0] * right_size
    
    for i in range(left_size):
        left_adj[i] = adj[i] & ((1 << left_size) - 1)
    for i in range(right_size):
        right_adj[i] = (adj[left_size + i] >> left_size) & ((1 << right_size) - 1)
    
    # Left independent sets
    left_sets = [[] for _ in range(left_size + 1)]
    # mask -> size
    for mask in range(1 << left_size):
        # check independence quickly
        ok = True
        size = 0
        m = mask
        while m:
            bit = m & -m
            i = (bit.bit_length() - 1)
            size += 1
            if mask & left_adj[i]:
                ok = False
                break
            m -= bit
        if ok:
            left_sets[size].append(mask)
    
    # Right independent sets
    right_sets = [[] for _ in range(right_size + 1)]
    for mask in range(1 << right_size):
        ok = True
        size = 0
        m = mask
        while m:
            bit = m & -m
            i = (bit.bit_length() - 1)
            size += 1
            if mask & right_adj[i]:
                ok = False
                break
            m -= bit
        if ok:
            right_sets[size].append(mask)
    
    # Try all left masks
    for lsize in range(min(k, left_size) + 1):
        rsize = k - lsize
        if rsize < 0 or rsize > right_size:
            continue
        for lmask in left_sets[lsize]:
            # allowed right vertices
            allowed = ((1 << right_size) - 1)
            # remove vertices adjacent to chosen left
            mm = lmask
            while mm:
                bit = mm & -mm
                i = (bit.bit_length() - 1)
                # left vertex i has right connections in adj[left_size + i] >> left_size
                allowed &= ~((adj[left_size + i] >> left_size) & ((1 << right_size) - 1))
                mm -= bit
            # Now find a right independent set of size rsize that is subset of allowed
            # maximize chance by checking if any exist
            for rmask in right_sets[rsize]:
                if rmask & ~allowed == 0:
                    # found
                    ans = []
                    mm = lmask
                    while mm:
                        bit = mm & -mm
                        i = (bit.bit_length() - 1)
                        ans.append(i+1)
                        mm -= bit
                    mm = rmask
                    while mm:
                        bit = mm & -mm
                        i = (bit.bit_length() - 1)
                        ans.append(left_size + i + 1)
                        mm -= bit
                    print("YES")
                    print(" ".join(map(str, ans)))
                    return
    print("NO")

if __name__ == "__main__":
    solve()