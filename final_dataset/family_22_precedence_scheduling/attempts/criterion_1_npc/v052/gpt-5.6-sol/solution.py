import sys
from collections import deque

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n, M, T, m = data[:4]
    if n == 0:
        print("YES")
        print()
        return
    if M <= 0 or T <= 0 or n > M * T:
        print("NO")
        return

    preds = [0] * n
    succ_masks = [0] * n
    succ = [[] for _ in range(n)]
    indeg = [0] * n

    p = 4
    for _ in range(m):
        a = data[p] - 1
        b = data[p + 1] - 1
        p += 2
        bit_a = 1 << a
        if preds[b] & bit_a:
            continue
        preds[b] |= bit_a
        succ_masks[a] |= 1 << b
        succ[a].append(b)
        indeg[b] += 1

    q = deque(i for i in range(n) if indeg[i] == 0)
    topo = []
    deg = indeg[:]
    while q:
        v = q.popleft()
        topo.append(v)
        for w in succ[v]:
            deg[w] -= 1
            if deg[w] == 0:
                q.append(w)

    if len(topo) != n:
        print("NO")
        return

    tail = [1] * n
    for v in reversed(topo):
        if succ[v]:
            tail[v] = 1 + max(tail[w] for w in succ[v])

    if max(tail) > T:
        print("NO")
        return

    latest = [T - tail[v] + 1 for v in range(n)]
    deadline_order = sorted(
        range(n),
        key=lambda v: (latest[v], -len(succ[v]), v)
    )

    all_mask = (1 << n) - 1
    failed = set()
    path = []

    sys.setrecursionlimit(max(1000, n + 100))

    def dfs(done, shift):
        if done == all_mask:
            return True
        if shift > T or done in failed:
            return False

        # Necessary capacity condition for all remaining operation deadlines.
        count = 0
        for v in deadline_order:
            if not ((done >> v) & 1):
                count += 1
                if latest[v] < shift + (count - 1) // M:
                    failed.add(done)
                    return False

        available = []
        forced_mask = 0
        remaining_count = n - done.bit_count()

        for v in range(n):
            if (done >> v) & 1:
                continue
            if preds[v] & ~done == 0:
                available.append(v)
                if latest[v] == shift:
                    forced_mask |= 1 << v
            elif latest[v] <= shift:
                failed.add(done)
                return False

        if not available:
            failed.add(done)
            return False

        capacity = min(M, remaining_count)
        forced_count = forced_mask.bit_count()
        if forced_count > capacity:
            failed.add(done)
            return False

        if len(available) <= capacity:
            chosen = 0
            for v in available:
                chosen |= 1 << v
            path.append(chosen)
            if dfs(done | chosen, shift + 1):
                return True
            path.pop()
            failed.add(done)
            return False

        candidates = [v for v in available if not ((forced_mask >> v) & 1)]
        need = capacity - forced_count
        candidates.sort(key=lambda v: (latest[v], -len(succ[v]), v))

        # Available operations with identical successor sets are interchangeable.
        groups_map = {}
        group_order = []
        for v in candidates:
            key = succ_masks[v]
            if key not in groups_map:
                groups_map[key] = []
                group_order.append(key)
            groups_map[key].append(v)

        groups = [groups_map[key] for key in group_order]
        suffix = [0] * (len(groups) + 1)
        for i in range(len(groups) - 1, -1, -1):
            suffix[i] = suffix[i + 1] + len(groups[i])

        def choose_groups(index, left, selected_mask):
            if left == 0:
                chosen = forced_mask | selected_mask
                path.append(chosen)
                if dfs(done | chosen, shift + 1):
                    return True
                path.pop()
                return False

            if index == len(groups) or suffix[index] < left:
                return False

            group = groups[index]
            maximum = min(len(group), left)
            minimum = max(0, left - suffix[index + 1])

            prefix_mask = 0
            prefix_masks = [0]
            for v in group:
                prefix_mask |= 1 << v
                prefix_masks.append(prefix_mask)

            for take in range(maximum, minimum - 1, -1):
                if choose_groups(
                    index + 1,
                    left - take,
                    selected_mask | prefix_masks[take]
                ):
                    return True
            return False

        if choose_groups(0, need, 0):
            return True

        failed.add(done)
        return False

    if not dfs(0, 1):
        print("NO")
        return

    assignment = [0] * n
    for shift, mask in enumerate(path, 1):
        while mask:
            bit = mask & -mask
            v = bit.bit_length() - 1
            assignment[v] = shift
            mask ^= bit

    print("YES")
    print(*assignment)

if __name__ == "__main__":
    main()