import sys
from collections import deque

sys.setrecursionlimit(1_000_000)

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    it = iter(data)
    n = next(it)
    M = next(it)
    T = next(it)
    m = next(it)

    if M <= 0 or T <= 0:
        print("YES" if n == 0 else "NO")
        return

    predecessors = [[] for _ in range(n)]
    successors = [[] for _ in range(n)]
    indegree = [0] * n

    for _ in range(m):
        a = next(it) - 1
        b = next(it) - 1
        successors[a].append(b)
        predecessors[b].append(a)
        indegree[b] += 1

    if n > M * T:
        print("NO")
        return

    queue = deque(i for i in range(n) if indegree[i] == 0)
    topo = []

    while queue:
        v = queue.popleft()
        topo.append(v)
        for w in successors[v]:
            indegree[w] -= 1
            if indegree[w] == 0:
                queue.append(w)

    if len(topo) != n:
        print("NO")
        return

    if n == 0:
        print("YES")
        return

    full_mask = (1 << n) - 1
    assignment = [0] * n
    failed = set()

    def solve(rem, slots):
        if rem == 0:
            return True
        if slots <= 0:
            return False

        count = rem.bit_count()
        if count > slots * M:
            return False

        state = (rem, slots)
        if state in failed:
            return False

        earliest = [0] * n
        max_earliest = 0

        for v in topo:
            if not ((rem >> v) & 1):
                continue
            best = 1
            for p in predecessors[v]:
                if (rem >> p) & 1:
                    value = earliest[p] + 1
                    if value > best:
                        best = value
            earliest[v] = best
            if best > max_earliest:
                max_earliest = best

        if max_earliest > slots:
            failed.add(state)
            return False

        to_sink = [0] * n
        deadlines = []
        release_levels = []
        sinks = []

        for v in reversed(topo):
            if not ((rem >> v) & 1):
                continue
            best = 1
            is_sink = True
            for w in successors[v]:
                if (rem >> w) & 1:
                    is_sink = False
                    value = to_sink[w] + 1
                    if value > best:
                        best = value
            to_sink[v] = best

            if earliest[v] + best - 1 > slots:
                failed.add(state)
                return False

            deadlines.append(slots - best + 1)
            release_levels.append(earliest[v])

            if is_sink:
                sinks.append(v)

        deadlines.sort()
        for i, deadline in enumerate(deadlines, 1):
            if i > deadline * M:
                failed.add(state)
                return False

        release_levels.sort(reverse=True)
        for i, release in enumerate(release_levels, 1):
            if i > (slots - release + 1) * M:
                failed.add(state)
                return False

        take_total = min(M, len(sinks))

        groups_map = {}
        for v in sinks:
            key = tuple(p for p in predecessors[v] if (rem >> p) & 1)
            groups_map.setdefault(key, []).append(v)

        groups = list(groups_map.values())
        groups.sort(
            key=lambda g: (earliest[g[0]], len(predecessors[g[0]]), len(g)),
            reverse=True
        )

        lower = []
        suffix_capacity = [0] * (len(groups) + 1)

        for group in groups:
            if earliest[group[0]] == slots:
                lower.append(len(group))
            else:
                lower.append(0)

        for i in range(len(groups) - 1, -1, -1):
            suffix_capacity[i] = suffix_capacity[i + 1] + len(groups[i])

        if sum(lower) > take_total:
            failed.add(state)
            return False

        chosen_masks = []

        def generate(group_index, need, mask):
            if group_index == len(groups):
                if need == 0:
                    yield mask
                return

            group = groups[group_index]
            minimum = lower[group_index]
            maximum = min(len(group), need)

            minimum = max(minimum, need - suffix_capacity[group_index + 1])
            if minimum > maximum:
                return

            prefix_masks = [0]
            current = 0
            for v in group:
                current |= 1 << v
                prefix_masks.append(current)

            for amount in range(maximum, minimum - 1, -1):
                yield from generate(
                    group_index + 1,
                    need - amount,
                    mask | prefix_masks[amount]
                )

        for selected in generate(0, take_total, 0):
            bits = selected
            chosen_masks.clear()

            while bits:
                bit = bits & -bits
                v = bit.bit_length() - 1
                assignment[v] = slots
                chosen_masks.append(v)
                bits ^= bit

            if solve(rem ^ selected, slots - 1):
                return True

            for v in chosen_masks:
                assignment[v] = 0

        failed.add(state)
        return False

    if solve(full_mask, T):
        print("YES " + " ".join(map(str, assignment)))
    else:
        print("NO")

if __name__ == "__main__":
    main()