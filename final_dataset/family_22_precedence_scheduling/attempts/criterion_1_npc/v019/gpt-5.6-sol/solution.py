import sys
import heapq
import itertools
import bisect

sys.setrecursionlimit(1_000_000)


def build_graph(n, edges, reverse=False):
    succ_sets = [set() for _ in range(n)]
    pred_sets = [set() for _ in range(n)]

    for a, b in edges:
        if reverse:
            a, b = b, a
        if b not in succ_sets[a]:
            succ_sets[a].add(b)
            pred_sets[b].add(a)

    succ = [list(x) for x in succ_sets]
    pred = [list(x) for x in pred_sets]
    return succ, pred


def topological_order(n, succ, pred):
    indeg = [len(pred[i]) for i in range(n)]
    heap = [i for i in range(n) if indeg[i] == 0]
    heapq.heapify(heap)
    order = []

    while heap:
        u = heapq.heappop(heap)
        order.append(u)
        for v in succ[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                heapq.heappush(heap, v)

    return order if len(order) == n else None


def compute_depths(n, order, succ, pred):
    from_source = [1] * n
    for u in order:
        du = from_source[u] + 1
        for v in succ[u]:
            if from_source[v] < du:
                from_source[v] = du

    to_sink = [1] * n
    for u in reversed(order):
        best = 1
        for v in succ[u]:
            val = to_sink[v] + 1
            if val > best:
                best = val
        to_sink[u] = best

    return from_source, to_sink


def heuristic_schedule(n, M, succ, pred, bottom, mode):
    indeg = [len(pred[i]) for i in range(n)]
    heap = []

    def key(u):
        if mode == 0:
            return (-bottom[u], -len(succ[u]), u)
        if mode == 1:
            return (-bottom[u], len(succ[u]), u)
        if mode == 2:
            return (-len(succ[u]), -bottom[u], u)
        return (-bottom[u], -len(pred[u]), u)

    for i in range(n):
        if indeg[i] == 0:
            heapq.heappush(heap, (key(i), i))

    times = [0] * n
    slot = 0
    completed = 0

    while heap:
        slot += 1
        chosen = []
        for _ in range(min(M, len(heap))):
            _, u = heapq.heappop(heap)
            chosen.append(u)

        completed += len(chosen)
        newly_available = []
        for u in chosen:
            times[u] = slot
            for v in succ[u]:
                indeg[v] -= 1
                if indeg[v] == 0:
                    newly_available.append(v)

        for v in newly_available:
            heapq.heappush(heap, (key(v), v))

    if completed != n:
        return None, None
    return times, slot


def exact_schedule(n, M, T, succ, pred, order):
    source_depth, bottom = compute_depths(n, order, succ, pred)

    if max(bottom) > T:
        return None

    source_sorted = sorted(source_depth)
    for e in set(source_depth):
        count = n - bisect.bisect_left(source_sorted, e)
        if count > M * (T - e + 1):
            return None

    pred_mask = [0] * n
    for v in range(n):
        mask = 0
        for u in pred[v]:
            mask |= 1 << u
        pred_mask[v] = mask

    all_mask = (1 << n) - 1
    latest = [T - bottom[i] + 1 for i in range(n)]

    groups = {}
    for i, d in enumerate(latest):
        groups[d] = groups.get(d, 0) | (1 << i)

    deadline_values = sorted(groups)
    cumulative_masks = []
    cumulative = 0
    for d in deadline_values:
        cumulative |= groups[d]
        cumulative_masks.append(cumulative)

    for d, mask in zip(deadline_values, cumulative_masks):
        if mask.bit_count() > M * d:
            return None

    rank_order = sorted(
        range(n),
        key=lambda u: (-bottom[u], -len(succ[u]), latest[u], u)
    )
    rank = [0] * n
    for i, u in enumerate(rank_order):
        rank[u] = i

    initial_available = 0
    for i in range(n):
        if pred_mask[i] == 0:
            initial_available |= 1 << i

    best_time = {}

    def dfs(done, available, t):
        if done == all_mask:
            return []

        if t >= T:
            return None

        previous = best_time.get(done)
        if previous is not None and previous <= t:
            return None
        best_time[done] = t

        unfinished = all_mask ^ done
        remaining_slots = T - t

        if unfinished.bit_count() > M * remaining_slots:
            return None

        for d, deadline_mask in zip(deadline_values, cumulative_masks):
            count = (unfinished & deadline_mask).bit_count()
            if d <= t:
                if count:
                    return None
            elif count > M * (d - t):
                return None

        current_deadline_mask = groups.get(t + 1, 0)
        forced = unfinished & current_deadline_mask
        if forced & ~available:
            return None

        forced_count = forced.bit_count()
        if forced_count > M:
            return None

        available_count = available.bit_count()
        if available_count == 0:
            return None

        if available_count <= M:
            candidates = (available,)
        else:
            need = M - forced_count
            optional_mask = available & ~forced
            optional_nodes = []
            x = optional_mask
            while x:
                bit = x & -x
                u = bit.bit_length() - 1
                optional_nodes.append(u)
                x -= bit
            optional_nodes.sort(key=lambda u: rank[u])

            if need < 0 or need > len(optional_nodes):
                return None

            def candidate_generator():
                if need == 0:
                    yield forced
                    return
                for combo in itertools.combinations(optional_nodes, need):
                    mask = forced
                    for u in combo:
                        mask |= 1 << u
                    yield mask

            candidates = candidate_generator()

        for chosen in candidates:
            new_done = done | chosen
            new_available = available & ~chosen

            x = chosen
            while x:
                bit = x & -x
                u = bit.bit_length() - 1
                x -= bit
                for v in succ[u]:
                    vb = 1 << v
                    if not (new_done & vb) and not (new_available & vb):
                        if pred_mask[v] & ~new_done == 0:
                            new_available |= vb

            result = dfs(new_done, new_available, t + 1)
            if result is not None:
                result.append(chosen)
                return result

        return None

    masks = dfs(0, initial_available, 0)
    if masks is None:
        return None

    masks.reverse()
    times = [0] * n
    for slot, mask in enumerate(masks, 1):
        x = mask
        while x:
            bit = x & -x
            u = bit.bit_length() - 1
            times[u] = slot
            x -= bit

    return times


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
        if a == b:
            print("NO")
            return
        edges.append((a, b))

    if n == 0:
        print("YES")
        print()
        return

    if M <= 0 or T <= 0 or n > M * T:
        print("NO")
        return

    succ, pred = build_graph(n, edges, False)
    order = topological_order(n, succ, pred)
    if order is None:
        print("NO")
        return

    if T >= n:
        answer = [0] * n
        for slot, u in enumerate(order, 1):
            answer[u] = slot
        print("YES")
        print(*answer)
        return

    _, bottom = compute_depths(n, order, succ, pred)
    if max(bottom) > T:
        print("NO")
        return

    orientations = [(succ, pred, order, False)]

    rsucc, rpred = build_graph(n, edges, True)
    rorder = topological_order(n, rsucc, rpred)
    orientations.append((rsucc, rpred, rorder, True))

    for osucc, opred, oorder, reversed_orientation in orientations:
        _, obottom = compute_depths(n, oorder, osucc, opred)
        for mode in range(4):
            times, length = heuristic_schedule(
                n, M, osucc, opred, obottom, mode
            )
            if times is not None and length <= T:
                if reversed_orientation:
                    times = [length + 1 - x for x in times]
                print("YES")
                print(*times)
                return

    def initial_branch_score(osucc, opred):
        k = sum(1 for i in range(n) if not opred[i])
        if k <= M:
            return 1
        r = min(M, k - M)
        score = 1
        for i in range(1, r + 1):
            score = score * (k - r + i) // i
            if score > 10**18:
                return 10**18
        return score

    orientations.sort(key=lambda item: initial_branch_score(item[0], item[1]))

    for osucc, opred, oorder, reversed_orientation in orientations:
        times = exact_schedule(n, M, T, osucc, opred, oorder)
        if times is not None:
            if reversed_orientation:
                times = [T + 1 - x for x in times]
            print("YES")
            print(*times)
            return

    print("NO")


if __name__ == "__main__":
    main()