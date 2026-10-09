import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it)); m = int(next(it)); k = int(next(it))
    adj = [0] * n
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u] |= 1 << v
        adj[v] |= 1 << u

    # split vertices
    n1 = n // 2
    n2 = n - n1
    left_ids = list(range(n1))
    right_ids = list(range(n1, n))

    # map global index to local bit positions
    left_bit = {v: i for i, v in enumerate(left_ids)}
    right_bit = {v: i for i, v in enumerate(right_ids)}

    # adjacency masks within each side and cross masks
    left_adj = [0] * n1
    right_adj = [0] * n2
    cross_left_to_right = [0] * n1  # bits of right side that are adjacent to left vertex

    for i, v in enumerate(left_ids):
        mask = adj[v]
        # within left
        left_adj[i] = sum(1 << left_bit[u] for u in left_ids if (mask >> u) & 1)
        # to right
        cross_left_to_right[i] = sum(1 << right_bit[u] for u in right_ids if (mask >> u) & 1)

    for i, v in enumerate(right_ids):
        mask = adj[v]
        right_adj[i] = sum(1 << right_bit[u] for u in right_ids if (mask >> u) & 1)

    # generate independent subsets for left side
    left_subsets = []  # (mask_left, size, forbidden_right_mask)
    def dfs_left(idx, cur_mask, forbid_right):
        if idx == n1:
            left_subsets.append((cur_mask, cur_mask.bit_count(), forbid_right))
            return
        # option: skip vertex idx
        dfs_left(idx + 1, cur_mask, forbid_right)
        # option: take if not adjacent to already taken
        if not (cur_mask & left_adj[idx]):
            dfs_left(idx + 1,
                     cur_mask | (1 << idx),
                     forbid_right | cross_left_to_right[idx])

    dfs_left(0, 0, 0)

    # generate independent subsets for right side, store by size
    right_by_size = [[] for _ in range(n2 + 1)]
    def dfs_right(idx, cur_mask):
        if idx == n2:
            right_by_size[cur_mask.bit_count()].append(cur_mask)
            return
        dfs_right(idx + 1, cur_mask)
        if not (cur_mask & right_adj[idx]):
            dfs_right(idx + 1, cur_mask | (1 << idx))

    dfs_right(0, 0)

    full_right_mask = (1 << n2) - 1

    for maskL, szL, forbidR in left_subsets:
        need = k - szL
        if need < 0:
            continue
        if need > n2:
            continue
        allowed = full_right_mask & ~forbidR
        # iterate over right subsets of required size and check subset of allowed
        for maskR in right_by_size[need]:
            if maskR & ~allowed == 0:
                # construct answer
                ans = []
                for i in range(n1):
                    if maskL >> i & 1:
                        ans.append(left_ids[i] + 1)
                for i in range(n2):
                    if maskR >> i & 1:
                        ans.append(right_ids[i] + 1)
                print("YES")
                print(' '.join(map(str, ans)))
                return
    print("NO")

if __name__ == "__main__":
    solve()