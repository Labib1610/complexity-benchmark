import sys
import math

sys.setrecursionlimit(1_000_000)


def build_graph(n, edges, reverse=False):
    succ = [0] * n
    if reverse:
        for a, b in edges:
            succ[b] |= 1 << a
    else:
        for a, b in edges:
            succ[a] |= 1 << b

    indeg = [0] * n
    adj = [[] for _ in range(n)]
    pre = [0] * n

    for u in range(n):
        mask = succ[u]
        while mask:
            bit = mask & -mask
            v = bit.bit_length() - 1
            adj[u].append(v)
            pre[v] |= 1 << u
            indeg[v] += 1
            mask ^= bit

    queue = [i for i in range(n) if indeg[i] == 0]
    topo = []
    head = 0
    while head < len(queue):
        u = queue[head]
        head += 1
        topo.append(u)
        for v in adj[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                queue.append(v)

    if len(topo) != n:
        return None

    bottom = [1] * n
    for u in reversed(topo):
        best = 0
        for v in adj[u]:
            if bottom[v] > best:
                best = bottom[v]
        bottom[u] = best + 1

    return pre, succ, topo, bottom


def greedy_schedule(n, M, T, graph):
    pre, succ, topo, bottom = graph
    all_mask = (1 << n) - 1
    done = 0
    result = []

    for _ in range(T):
        if done == all_mask:
            return result

        remaining = all_mask ^ done
        available = []
        mask = remaining
        while mask:
            bit = mask & -mask
            v = bit.bit_length() - 1
            if pre[v] & remaining == 0:
                available.append(v)
            mask ^= bit

        if not available:
            return None

        available.sort(key=lambda v: (bottom[v], succ[v].bit_count()), reverse=True)
        chosen = available[:M]
        slot_mask = 0
        for v in chosen:
            slot_mask |= 1 << v
        result.append(slot_mask)
        done |= slot_mask

    return result if done == all_mask else None


def orientation_score(n, M, T, graph):
    pre, succ, topo, bottom = graph
    all_mask = (1 << n) - 1
    done = 0
    score = 0.0

    for _ in range(T):
        if done == all_mask:
            break
        remaining = all_mask ^ done
        available = []
        mask = remaining
        while mask:
            bit = mask & -mask
            v = bit.bit_length() - 1
            if pre[v] & remaining == 0:
                available.append(v)
            mask ^= bit

        a = len(available)
        if a == 0:
            return float("inf")
        if a > M:
            score += math.lgamma(a + 1) - math.lgamma(M + 1) - math.lgamma(a - M + 1)

        available.sort(key=lambda v: (bottom[v], succ[v].bit_count()), reverse=True)
        slot_mask = 0
        for v in available[:M]:
            slot_mask |= 1 << v
        done |= slot_mask

    return score


def exact_schedule(n, M, T, graph):
    pre, succ, topo, bottom = graph
    all_mask = (1 << n) - 1
    max_bottom = max(bottom, default=0)

    exact_level = [0] * (max_bottom + 2)
    for v, b in enumerate(bottom):
        exact_level[b] |= 1 << v

    ge_level = [0] * (max_bottom + 2)
    running = 0
    for b in range(max_bottom, 0, -1):
        running |= exact_level[b]
        ge_level[b] = running

    failed = set()
    memo_limit = 300_000
    path = []

    def feasible_bounds(remaining, rem):
        if remaining.bit_count() > rem * M:
            return False
        if rem < max_bottom and (remaining & ge_level[rem + 1]):
            return False

        upper = min(rem, max_bottom)
        for b in range(1, upper + 1):
            jobs = (remaining & ge_level[b]).bit_count()
            available_slots = rem - b + 1
            if jobs > available_slots * M:
                return False
        return True

    def dfs(done, rem):
        if done == all_mask:
            return True
        if rem == 0:
            return False

        key = (done, rem)
        if key in failed:
            return False

        remaining = all_mask ^ done
        if not feasible_bounds(remaining, rem):
            if len(failed) < memo_limit:
                failed.add(key)
            return False

        available_mask = 0
        available = []
        mask = remaining
        while mask:
            bit = mask & -mask
            v = bit.bit_length() - 1
            if pre[v] & remaining == 0:
                available_mask |= bit
                available.append(v)
            mask ^= bit

        if not available:
            if len(failed) < memo_limit:
                failed.add(key)
            return False

        take = min(M, len(available))
        forced = remaining & exact_level[rem] if rem <= max_bottom else 0
        if forced & ~available_mask or forced.bit_count() > take:
            if len(failed) < memo_limit:
                failed.add(key)
            return False

        if len(available) <= M:
            chosen = available_mask
            path.append(chosen)
            if dfs(done | chosen, rem - 1):
                return True
            path.pop()
            if len(failed) < memo_limit:
                failed.add(key)
            return False

        need = take - forced.bit_count()
        optional = [v for v in available if not ((forced >> v) & 1)]
        optional.sort(key=lambda v: (bottom[v], succ[v].bit_count()), reverse=True)

        groups = []
        group_pos = {}
        for v in optional:
            signature = succ[v]
            idx = group_pos.get(signature)
            if idx is None:
                group_pos[signature] = len(groups)
                groups.append([signature, []])
                idx = len(groups) - 1
            groups[idx][1].append(v)

        suffix_sizes = [0] * (len(groups) + 1)
        for i in range(len(groups) - 1, -1, -1):
            suffix_sizes[i] = suffix_sizes[i + 1] + len(groups[i][1])

        group_prefix_masks = []
        for _, vertices in groups:
            prefixes = [0]
            cur = 0
            for v in vertices:
                cur |= 1 << v
                prefixes.append(cur)
            group_prefix_masks.append(prefixes)

        def generate(i, left, selected_mask):
            if left == 0:
                chosen = forced | selected_mask
                path.append(chosen)
                if dfs(done | chosen, rem - 1):
                    return True
                path.pop()
                return False

            if i == len(groups) or suffix_sizes[i] < left:
                return False

            size = len(groups[i][1])
            maximum = min(size, left)
            minimum = max(0, left - suffix_sizes[i + 1])

            for count in range(maximum, minimum - 1, -1):
                added = group_prefix_masks[i][count]
                if generate(i + 1, left - count, selected_mask | added):
                    return True
            return False

        if generate(0, need, 0):
            return True

        if len(failed) < memo_limit:
            failed.add(key)
        return False

    if dfs(0, T):
        return path[:]
    return None


def masks_to_slots(n, T, masks, reversed_orientation):
    slots = [0] * n
    for t, mask in enumerate(masks, 1):
        actual_t = T + 1 - t if reversed_orientation else t
        while mask:
            bit = mask & -mask
            v = bit.bit_length() - 1
            slots[v] = actual_t
            mask ^= bit
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

    forward = build_graph(n, edges, False)
    if forward is None:
        print("NO")
        return

    pre, succ, topo, bottom = forward
    if max(bottom) > T:
        print("NO")
        return

    if n <= T:
        slots = [0] * n
        for t, v in enumerate(topo, 1):
            slots[v] = t
        print("YES")
        print(*slots)
        return

    greedy = greedy_schedule(n, M, T, forward)
    if greedy is not None:
        slots = masks_to_slots(n, T, greedy, False)
        print("YES")
        print(*slots)
        return

    backward = build_graph(n, edges, True)
    greedy_back = greedy_schedule(n, M, T, backward)
    if greedy_back is not None:
        slots = masks_to_slots(n, T, greedy_back, True)
        print("YES")
        print(*slots)
        return

    score_f = orientation_score(n, M, T, forward)
    score_b = orientation_score(n, M, T, backward)

    if score_b < score_f:
        chosen_graph = backward
        reversed_orientation = True
    else:
        chosen_graph = forward
        reversed_orientation = False

    schedule = exact_schedule(n, M, T, chosen_graph)
    if schedule is None:
        print("NO")
        return

    slots = masks_to_slots(n, T, schedule, reversed_orientation)
    print("YES")
    print(*slots)


if __name__ == "__main__":
    main()