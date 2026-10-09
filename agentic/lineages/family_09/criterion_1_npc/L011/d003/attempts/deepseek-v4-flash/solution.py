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

    # Split vertices into two halves
    half1 = n // 2
    half2 = n - half1

    # Enumerate independent sets in first half
    ind1 = []  # list of (mask, size)
    for mask in range(1 << half1):
        ok = True
        for i in range(half1):
            if mask >> i & 1:
                if adj[i] & mask:
                    ok = False
                    break
        if ok:
            ind1.append((mask, mask.bit_count()))

    # Enumerate independent sets in second half
    ind2_by_size = [[] for _ in range(half2 + 1)]
    for mask in range(1 << half2):
        ok = True
        for i in range(half2):
            if mask >> i & 1:
                if (adj[half1 + i] >> half1) & mask:
                    ok = False
                    break
        if ok:
            ind2_by_size[mask.bit_count()].append(mask)

    # For each first-half independent set, compute allowed second-half mask
    for mask1, size1 in ind1:
        need = k - size1
        if need < 0 or need > half2:
            continue
        # allowed vertices in second half: not adjacent to any in mask1
        allowed = 0
        for i in range(half1):
            if mask1 >> i & 1:
                allowed |= adj[i] >> half1
        allowed = ((1 << half2) - 1) & ~allowed
        # Check if any independent set of size 'need' is subset of allowed
        for mask2 in ind2_by_size[need]:
            if mask2 & ~allowed == 0:
                # Found solution
                res = []
                for i in range(half1):
                    if mask1 >> i & 1:
                        res.append(i + 1)
                for i in range(half2):
                    if mask2 >> i & 1:
                        res.append(half1 + i + 1)
                print("YES")
                print(" ".join(map(str, res)))
                return

    print("NO")

if __name__ == "__main__":
    solve()