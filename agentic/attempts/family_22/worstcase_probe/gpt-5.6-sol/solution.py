import sys
import heapq

sys.setrecursionlimit(1_000_000)


def build_graph(n, edges, reverse=False):
    succ = [[] for _ in range(n)]
    pred = [[] for _ in range(n)]
    succ_mask = [0] * n
    pred_mask = [0] * n

    for a, b in edges:
        if reverse:
            a, b = b, a
        succ[a].append(b)
        pred[b].append(a)
        succ_mask[a] |= 1 << b
        pred_mask[b] |= 1 << a

    indeg = [len(pred[i]) for i in range(n)]
    heap = [i for i in range(n) if indeg[i] == 0]
    heapq.heapify(heap)
    topo = []

    while heap:
        u = heapq.heappop(heap)
        topo.append(u)
        for v in succ[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                heapq.heappush(heap, v)

    if len(topo) != n:
        return None

    depth = [1] * n
    for u in reversed(topo):
        if succ[u]:
            depth[u] = 1 + max(depth[v] for v in succ[u])

    return succ, pred, succ_mask, pred_mask, topo, depth


def greedy_schedule(n, M, graph, mode):
    succ, pred, _, _, _, depth = graph
    indeg = [len(pred[i]) for i in range(n)]
    heap = []

    def key(i):
        if mode == 0:
            return (-depth[i], -len(succ[i]), i)
        if mode == 1:
            return (-len(succ[i]), -depth[i], i)
        if mode == 2:
            return (depth[i], len(succ[i]), i)
        if mode == 3:
            return (i,)
        if mode == 4:
            return (-i,)
        x = (i * 1103515245 + 12345 + mode * 2654435761) & 0x7fffffff
        return (-depth[i], x, i)

    for i in range(n):
        if indeg[i] == 0:
            heapq.heappush(heap, (key(i), i))

    slots = [0] * n
    time_slot = 0
    done = 0
    max_frontier = 0

    while heap:
        time_slot += 1
        max_frontier = max(max_frontier, len(heap))
        batch = []
        for _ in range(min(M, len(heap))):
            _, u = heapq.heappop(heap)
            batch.append(u)

        for u in batch:
            slots[u] = time_slot
            done += 1

        newly_available = []
        for u in batch:
            for v in succ[u]:
                indeg[v] -= 1
                if indeg[v] == 0:
                    newly_available.append(v)

        for v in newly_available:
            heapq.heappush(heap, (key(v), v))

    if done != n:
        return None, 10**18
    return slots, max_frontier


def exact_schedule(n, M, T, graph):
    succ, pred, succ_mask, pred_mask, topo, depth = graph
    all_mask = (1 << n) - 1
    latest = [T - depth[i] + 1 for i in range(n)]

    if any(x < 1 for x in latest):
        return None

    by_latest = sorted(range(n), key=lambda i: latest[i])
    failed = set()
    shift = (T + 2).bit_length()
    path = []

    def dfs(done_mask, t):
        if done_mask == all_mask:
            return True

        remaining_count = n - done_mask.bit_count()
        if t > T or remaining_count > M * (T - t + 1):
            return False

        state_key = (done_mask << shift) | t
        if state_key in failed:
            return False

        count = 0
        for i in by_latest:
            if not ((done_mask >> i) & 1):
                count += 1
                deadline = latest[i]
                if deadline < t or count > M * (deadline - t + 1):
                    failed.add(state_key)
                    return False

        available = []
        forced_total = 0
        forced_available = 0

        not_done = all_mask ^ done_mask
        x = not_done
        while x:
            bit = x & -x
            i = bit.bit_length() - 1
            x ^= bit

            if latest[i] == t:
                forced_total += 1

            if pred_mask[i] & not_done == 0:
                available.append(i)
                if latest[i] == t:
                    forced_available += 1

        if not available:
            failed.add(state_key)
            return False

        if forced_total != forced_available or forced_total > M:
            failed.add(state_key)
            return False

        take = min(M, len(available))

        if len(available) <= M:
            batch_mask = 0
            for i in available:
                batch_mask |= 1 << i
            path.append(available)
            if dfs(done_mask | batch_mask, t + 1):
                return True
            path.pop()
            failed.add(state_key)
            return False

        groups_dict = {}
        for i in available:
            groups_dict.setdefault(succ_mask[i], []).append(i)

        groups = []
        for members in groups_dict.values():
            members.sort()
            members.sort(key=lambda i: (latest[i], -depth[i], i))
            size = len(members)
            minimum = size if latest[members[0]] == t else 0
            prefix = [0]
            mask = 0
            for i in members:
                mask |= 1 << i
                prefix.append(mask)
            groups.append((latest[members[0]], -depth[members[0]],
                           members, prefix, minimum))

        groups.sort(key=lambda g: (g[0], g[1], g[2][0]))
        gcount = len(groups)
        suffix_capacity = [0] * (gcount + 1)
        suffix_minimum = [0] * (gcount + 1)
        for p in range(gcount - 1, -1, -1):
            suffix_capacity[p] = suffix_capacity[p + 1] + len(groups[p][2])
            suffix_minimum[p] = suffix_minimum[p + 1] + groups[p][4]

        chosen_batches = []

        def enumerate_groups(pos, need, chosen_mask):
            if need < suffix_minimum[pos] or need > suffix_capacity[pos]:
                return False
            if pos == gcount:
                if need != 0:
                    return False
                path.append(chosen_batches.copy())
                if dfs(done_mask | chosen_mask, t + 1):
                    return True
                path.pop()
                return False

            _, _, members, prefix, minimum = groups[pos]
            maximum = min(len(members), need - suffix_minimum[pos + 1])
            minimum_here = max(minimum, need - suffix_capacity[pos + 1])

            for c in range(maximum, minimum_here - 1, -1):
                old_len = len(chosen_batches)
                if c:
                    chosen_batches.extend(members[:c])
                if enumerate_groups(pos + 1, need - c,
                                    chosen_mask | prefix[c]):
                    return True
                del chosen_batches[old_len:]
            return False

        if enumerate_groups(0, take, 0):
            return True

        failed.add(state_key)
        if len(failed) > 700_000:
            failed.clear()
        return False

    if not dfs(0, 1):
        return None

    slots = [0] * n
    for t, batch in enumerate(path, 1):
        for i in batch:
            slots[i] = t
    return slots


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if len(data) < 4:
        return

    n, M, T, m = data[:4]
    edges = []
    p = 4
    for _ in range(m):
        a = data[p] - 1
        b = data[p + 1] - 1
        p += 2
        edges.append((a, b))

    if n == 0:
        print("YES")
        print()
        return

    if M <= 0 or T <= 0:
        print("NO")
        return

    original = build_graph(n, edges, False)
    if original is None:
        print("NO")
        return

    if T >= n:
        slots = [0] * n
        for t, u in enumerate(original[4], 1):
            slots[u] = t
        print("YES")
        print(*slots)
        return

    reverse = build_graph(n, edges, True)

    best_orientation = None
    best_frontier = 10**18

    for reversed_flag, graph in ((False, original), (True, reverse)):
        for mode in range(8):
            slots, frontier = greedy_schedule(n, M, graph, mode)
            if slots is not None and max(slots, default=0) <= T:
                if reversed_flag:
                    length = max(slots)
                    slots = [length + 1 - x for x in slots]
                print("YES")
                print(*slots)
                return
            if frontier < best_frontier:
                best_frontier = frontier
                best_orientation = (reversed_flag, graph)

    reversed_flag, graph = best_orientation
    slots = exact_schedule(n, M, T, graph)

    if slots is None:
        print("NO")
        return

    if reversed_flag:
        length = max(slots)
        slots = [length + 1 - x for x in slots]

    print("YES")
    print(*slots)


if __name__ == "__main__":
    main()