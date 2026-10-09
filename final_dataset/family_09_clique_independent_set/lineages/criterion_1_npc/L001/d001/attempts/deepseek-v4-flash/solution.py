import sys

def solve():
    input = sys.stdin.readline
    n, m, k = map(int, input().split())
    adj = [0] * n
    for _ in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        adj[u] |= 1 << v
        adj[v] |= 1 << u

    # Split into two halves
    n1 = n // 2
    n2 = n - n1
    left = list(range(n1))
    right = list(range(n1, n))

    # Enumerate independent sets in left half
    left_sets = []  # (mask, size)
    for mask in range(1 << n1):
        ok = True
        for i in range(n1):
            if mask >> i & 1:
                if adj[left[i]] & mask:
                    ok = False
                    break
        if ok:
            left_sets.append((mask, bin(mask).count('1')))

    # Enumerate independent sets in right half
    right_sets = []  # (mask, size)
    for mask in range(1 << n2):
        ok = True
        for i in range(n2):
            if mask >> i & 1:
                if adj[right[i]] & (mask << n1):
                    ok = False
                    break
        if ok:
            right_sets.append((mask, bin(mask).count('1')))

    # For each left set, find a right set with no cross conflicts
    # Precompute for each left mask the allowed right masks
    # We'll just check compatibility directly
    for lmask, lsize in left_sets:
        need = k - lsize
        if need < 0 or need > n2:
            continue
        # Build forbidden right mask from left set
        forbidden = 0
        for i in range(n1):
            if lmask >> i & 1:
                forbidden |= adj[left[i]] >> n1
        for rmask, rsize in right_sets:
            if rsize == need and (rmask & forbidden) == 0:
                # Found solution
                ans = []
                for i in range(n1):
                    if lmask >> i & 1:
                        ans.append(left[i] + 1)
                for i in range(n2):
                    if rmask >> i & 1:
                        ans.append(right[i] + 1)
                print("YES")
                print(" ".join(map(str, ans)))
                return
    print("NO")

if __name__ == "__main__":
    solve()