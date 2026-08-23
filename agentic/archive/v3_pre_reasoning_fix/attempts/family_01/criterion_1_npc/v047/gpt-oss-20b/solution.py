import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    neighbors_mask = [0] * n
    neighbors_list = [[] for _ in range(n)]

    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        if u == v:
            continue
        neighbors_mask[u] |= (1 << v)
        neighbors_mask[v] |= (1 << u)
        neighbors_list[u].append(v)
        neighbors_list[v].append(u)

    color = [0] * n
    avail = [0b111] * n
    color_mask = [0, 0, 0, 0]  # 1-indexed
    colored_mask = 0

    sys.setrecursionlimit(1000000)

    def dfs(idx: int) -> bool:
        nonlocal colored_mask

        if idx == n:
            return True

        # early pruning: any uncolored vertex with no available colors
        for j in range(idx, n):
            if ((colored_mask >> j) & 1) == 0 and avail[j] == 0:
                return False

        v = idx
        for c in (1, 2, 3):
            if neighbors_mask[v] & color_mask[c]:
                continue

            # assign color c to vertex v
            color[v] = c
            color_mask[c] |= (1 << v)
            pre_colored_mask = colored_mask
            colored_mask |= (1 << v)

            changes = []
            conflict = False
            for u in neighbors_list[v]:
                if (pre_colored_mask >> u) & 1:
                    continue
                prev_avail = avail[u]
                new_avail = prev_avail & ~(1 << (c - 1))
                if new_avail == 0:
                    conflict = True
                    break
                avail[u] = new_avail
                changes.append((u, prev_avail))

            if not conflict and dfs(idx + 1):
                return True

            # backtrack
            for u, prev in changes:
                avail[u] = prev
            colored_mask = pre_colored_mask
            color_mask[c] &= ~(1 << v)
            color[v] = 0

        return False

    if dfs(0):
        print("YES")
        print(' '.join(str(color[i]) for i in range(n)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()