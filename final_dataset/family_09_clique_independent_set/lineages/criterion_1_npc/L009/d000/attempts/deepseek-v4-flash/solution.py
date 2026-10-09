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
    
    # If k is large, we can search for complement (vertex cover) instead
    # But n <= 46, so we can use meet-in-the-middle.
    
    # Split vertices into two halves
    half = n // 2
    left = half
    right = n - half
    
    # Precompute independent sets for left half
    left_sets = []
    for mask in range(1 << left):
        ok = True
        for i in range(left):
            if mask & (1 << i):
                if adj[i] & mask:
                    ok = False
                    break
        if ok:
            left_sets.append(mask)
    
    # For right half, we need to know which left vertices conflict
    right_sets = []
    for mask in range(1 << right):
        ok = True
        for i in range(right):
            if mask & (1 << i):
                if adj[left + i] & (mask << left):
                    ok = False
                    break
        if ok:
            right_sets.append(mask)
    
    # For each right set, compute which left vertices are forbidden
    right_info = []
    for rmask in right_sets:
        forbidden = 0
        for i in range(right):
            if rmask & (1 << i):
                forbidden |= (adj[left + i] & ((1 << left) - 1))
        right_info.append((rmask, forbidden, bin(rmask).count('1')))
    
    # For each left set, find a compatible right set to reach total k
    for lmask in left_sets:
        lsize = bin(lmask).count('1')
        if lsize > k:
            continue
        need = k - lsize
        # Find right set with size == need and no conflict
        for rmask, forbidden, rsize in right_info:
            if rsize == need and (lmask & forbidden) == 0:
                # Found solution
                ans = []
                for i in range(left):
                    if lmask & (1 << i):
                        ans.append(i + 1)
                for i in range(right):
                    if rmask & (1 << i):
                        ans.append(left + i + 1)
                print("YES")
                print(" ".join(map(str, ans)))
                return
    
    print("NO")

if __name__ == "__main__":
    solve()