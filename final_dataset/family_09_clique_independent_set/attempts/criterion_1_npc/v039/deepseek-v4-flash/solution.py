import sys
from collections import defaultdict

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
    
    # Split vertices into two halves
    half = n // 2
    left_size = half
    right_size = n - half
    
    # Enumerate all independent sets in left half
    left_sets = []  # list of (mask, size)
    for mask in range(1 << left_size):
        ok = True
        for i in range(left_size):
            if mask & (1 << i):
                # check if any neighbor in left half is also in mask
                if adj[i] & mask & ((1 << left_size) - 1):
                    ok = False
                    break
        if ok:
            left_sets.append((mask, bin(mask).count('1')))
    
    # Enumerate all independent sets in right half
    right_sets = []  # list of (mask, size)
    for mask in range(1 << right_size):
        ok = True
        for i in range(right_size):
            if mask & (1 << i):
                # map to original index
                orig = left_size + i
                # check neighbors in right half
                if adj[orig] & (mask << left_size) & (((1 << n) - 1) ^ ((1 << left_size) - 1)):
                    ok = False
                    break
        if ok:
            right_sets.append((mask, bin(mask).count('1')))
    
    # For each left set, we need a right set that is compatible
    # Compatibility: no edge between left chosen and right chosen
    # Precompute for each left mask the forbidden right mask
    left_forbidden = []
    for mask, _ in left_sets:
        forbid = 0
        for i in range(left_size):
            if mask & (1 << i):
                # neighbors in right half
                forbid |= (adj[i] >> left_size)
        left_forbidden.append(forbid)
    
    # Group right sets by size
    right_by_size = defaultdict(list)
    for mask, sz in right_sets:
        right_by_size[sz].append(mask)
    
    # For each left set, try to find a right set of size k - left_size
    for idx, (lmask, lsz) in enumerate(left_sets):
        need = k - lsz
        if need < 0 or need > right_size:
            continue
        forbid = left_forbidden[idx]
        for rmask in right_by_size.get(need, []):
            if (rmask & forbid) == 0:
                # Found solution
                ans = []
                for i in range(left_size):
                    if lmask & (1 << i):
                        ans.append(i + 1)
                for j in range(right_size):
                    if rmask & (1 << j):
                        ans.append(left_size + j + 1)
                print("YES")
                print(" ".join(map(str, ans)))
                return
    
    print("NO")

if __name__ == "__main__":
    solve()