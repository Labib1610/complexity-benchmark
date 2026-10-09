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
    left_n = n // 2
    right_n = n - left_n

    # Precompute for left half: mask -> (size, valid)
    left_size = 1 << left_n
    left_valid = [False] * left_size
    left_count = [0] * left_size
    for mask in range(left_size):
        ok = True
        cnt = 0
        for i in range(left_n):
            if mask & (1 << i):
                cnt += 1
                # check conflict with other selected in left
                if (adj[i] & mask & ~(1 << i)):
                    ok = False
                    break
        left_valid[mask] = ok
        left_count[mask] = cnt

    # Precompute for right half: mask -> (size, valid)
    right_size = 1 << right_n
    right_valid = [False] * right_size
    right_count = [0] * right_size
    for mask in range(right_size):
        ok = True
        cnt = 0
        for i in range(right_n):
            if mask & (1 << i):
                cnt += 1
                if (adj[left_n + i] & (mask << left_n) & ~(1 << (left_n + i))):
                    ok = False
                    break
        right_valid[mask] = ok
        right_count[mask] = cnt

    # For each valid right mask, store max size for each size? Actually we need exact size.
    # We'll store for each size the mask (or just existence)
    right_by_size = defaultdict(list)
    for mask in range(right_size):
        if right_valid[mask]:
            right_by_size[right_count[mask]].append(mask)

    # Try all valid left masks
    for lmask in range(left_size):
        if not left_valid[lmask]:
            continue
        need = k - left_count[lmask]
        if need < 0 or need > right_n:
            continue
        # Check compatibility: for each selected left vertex, it must not conflict with selected right vertices
        # We can precompute forbidden right mask for each left mask
        forbidden = 0
        for i in range(left_n):
            if lmask & (1 << i):
                # right vertices adjacent to i
                forbidden |= (adj[i] >> left_n)
        # We need a right mask that is valid, has size need, and has no overlap with forbidden
        for rmask in right_by_size.get(need, []):
            if (rmask & forbidden) == 0:
                # Found solution
                res = []
                for i in range(left_n):
                    if lmask & (1 << i):
                        res.append(i + 1)
                for j in range(right_n):
                    if rmask & (1 << j):
                        res.append(left_n + j + 1)
                print("YES")
                print(" ".join(map(str, res)))
                return

    print("NO")

if __name__ == "__main__":
    solve()