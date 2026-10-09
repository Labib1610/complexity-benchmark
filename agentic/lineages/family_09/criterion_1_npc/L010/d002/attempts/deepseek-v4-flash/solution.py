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

    # For first half, enumerate all independent sets
    size1 = 1 << n1
    indep1 = []
    for mask in range(size1):
        ok = True
        for i in range(n1):
            if mask & (1 << i):
                if adj[i] & mask:
                    ok = False
                    break
        if ok:
            indep1.append(mask)

    # For second half, enumerate all independent sets
    size2 = 1 << n2
    indep2 = []
    for mask in range(size2):
        ok = True
        for i in range(n2):
            if mask & (1 << i):
                if adj[n1 + i] & (mask << n1):
                    ok = False
                    break
        if ok:
            indep2.append(mask)

    # For each independent set in first half, find compatible sets in second half
    # Precompute for each mask in first half, which vertices in second half are forbidden
    forbidden = [0] * size1
    for mask in range(size1):
        f = 0
        for i in range(n1):
            if mask & (1 << i):
                f |= (adj[i] >> n1)
        forbidden[mask] = f

    # For each independent set in second half, store its size and mask
    # We want to find if there exists mask1 in indep1 and mask2 in indep2
    # such that (mask1 & forbidden[mask2]) == 0 and popcount(mask1)+popcount(mask2) == k
    # Actually forbidden[mask1] is for mask1, so we need mask2 & forbidden[mask1] == 0

    # Group indep2 by size
    from collections import defaultdict
    by_size = defaultdict(list)
    for mask in indep2:
        by_size[bin(mask).count("1")].append(mask)

    # For each mask1, we need mask2 with size = k - popcount(mask1) and mask2 & forbidden[mask1] == 0
    for mask1 in indep1:
        cnt1 = bin(mask1).count("1")
        need = k - cnt1
        if need < 0 or need > n2:
            continue
        for mask2 in by_size.get(need, []):
            if mask2 & forbidden[mask1] == 0:
                # Found solution
                chosen = []
                for i in range(n1):
                    if mask1 & (1 << i):
                        chosen.append(i + 1)
                for i in range(n2):
                    if mask2 & (1 << i):
                        chosen.append(n1 + i + 1)
                print("YES")
                print(" ".join(map(str, chosen)))
                return

    print("NO")

if __name__ == "__main__":
    solve()