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

    # Split vertices into two halves
    n1 = n // 2
    n2 = n - n1
    left = list(range(n1))
    right = list(range(n1, n))

    # Enumerate independent sets in left half
    left_sets = [[] for _ in range(n1 + 1)]  # list of (mask, size)
    for mask in range(1 << n1):
        ok = True
        size = 0
        for i in range(n1):
            if mask & (1 << i):
                size += 1
                if adj[left[i]] & mask:
                    ok = False
                    break
        if ok:
            left_sets[size].append(mask)

    # Enumerate independent sets in right half
    right_sets = [[] for _ in range(n2 + 1)]
    for mask in range(1 << n2):
        ok = True
        size = 0
        for i in range(n2):
            if mask & (1 << i):
                size += 1
                if adj[right[i]] & (mask << n1):
                    ok = False
                    break
        if ok:
            right_sets[size].append(mask)

    # Try to combine
    for s1 in range(k + 1):
        s2 = k - s1
        if s1 > n1 or s2 > n2:
            continue
        for mask1 in left_sets[s1]:
            # Build conflict mask from left set to right half
            conflict = 0
            for i in range(n1):
                if mask1 & (1 << i):
                    conflict |= (adj[left[i]] >> n1)
            # Need right mask with no overlap with conflict
            allowed = ((1 << n2) - 1) & ~conflict
            # Check if any right set of size s2 is subset of allowed
            for mask2 in right_sets[s2]:
                if mask2 & ~allowed == 0:
                    # Found
                    ans = []
                    for i in range(n1):
                        if mask1 & (1 << i):
                            ans.append(left[i] + 1)
                    for i in range(n2):
                        if mask2 & (1 << i):
                            ans.append(right[i] + 1)
                    print("YES")
                    print(" ".join(map(str, ans)))
                    return
    print("NO")

if __name__ == "__main__":
    solve()