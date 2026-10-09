import sys
import heapq
import itertools

sys.setrecursionlimit(1_000_000)


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if len(data) < 4:
        return

    n, M, T, m = data[:4]
    if n == 0:
        print("YES")
        print()
        return
    if M <= 0 or T <= 0 or n > M * T:
        print("NO")
        return

    succ_sets = [set() for _ in range(n)]
    pos = 4
    for _ in range(m):
        a = data[pos] - 1
        b = data[pos + 1] - 1
        pos += 2
        if a != b:
            succ_sets[a].add(b)
        else:
            print("NO")
            return

    succ = [list(s) for s in succ_sets]
    pred = [[] for _ in range(n)]
    indeg = [0] * n
    for u in range(n):
        for v in succ[u]:
            pred[v].append(u)
            indeg[v] += 1

    heap = [v for v in range(n) if indeg[v] == 0]
    heapq.heapify(heap)
    topo = []
    deg = indeg[:]
    while heap:
        u = heapq.heappop(heap)
        topo.append(u)
        for v in succ[u]:
            deg[v] -= 1
            if deg[v] == 0:
                heapq.heappush(heap, v)

    if len(topo) != n:
        print("NO")
        return

    tail = [1] * n
    head = [1] * n
    for u in topo:
        hu = head[u] + 1
        for v in succ[u]:
            if hu > head[v]:
                head[v] = hu

    for u in reversed(topo):
        best = 1
        for v in succ[u]:
            cand = tail[v] + 1
            if cand > best:
                best = cand
        tail[u] = best

    if max(tail) > T:
        print("NO")
        return

    if T >= n:
        ans = [0] * n
        for phase, v in enumerate(topo, 1):
            ans[v] = phase
        print("YES")
        print(*ans)
        return

    if M >= n:
        print("YES")
        print(*head)
        return

    def greedy_schedule(graph, incoming, priority):
        d = [len(incoming[v]) for v in range(n)]
        available = []
        for v in range(n):
            if d[v] == 0:
                heapq.heappush(available, (-priority[v], v))

        assignment = [0] * n
        phase = 1
        completed = 0

        while available:
            chosen = []
            for _ in range(min(M, len(available))):
                _, u = heapq.heappop(available)
                chosen.append(u)
                assignment[u] = phase
                completed += 1

            newly_available = []
            for u in chosen:
                for v in graph[u]:
                    d[v] -= 1
                    if d[v] == 0:
                        newly_available.append(v)

            for v in newly_available:
                heapq.heappush(available, (-priority[v], v))
            phase += 1

        if completed == n and phase - 1 <= T:
            return assignment
        return None

    ans = greedy_schedule(succ, pred, tail)
    if ans is not None:
        print("YES")
        print(*ans)
        return

    reverse_assignment = greedy_schedule(pred, succ, head)
    if reverse_assignment is not None:
        ans = [T + 1 - reverse_assignment[v] for v in range(n)]
        print("YES")
        print(*ans)
        return

    pre_mask = [0] * n
    for v in range(n):
        mask = 0
        for u in pred[v]:
            mask |= 1 << u
        pre_mask[v] = mask

    latest = [T - tail[v] + 1 for v in range(n)]
    exact_deadline = [0] * (T + 1)
    cumulative_deadline = [0] * (T + 1)

    for v in range(n):
        exact_deadline[latest[v]] |= 1 << v

    running = 0
    relevant_deadlines = []
    for d in range(1, T + 1):
        running |= exact_deadline[d]
        cumulative_deadline[d] = running
        if exact_deadline[d]:
            relevant_deadlines.append(d)

    all_mask = (1 << n) - 1
    assignment = [0] * n
    failed = set()

    def dfs(done, phase):
        if done == all_mask:
            return True
        if phase > T:
            return False

        key = (done, phase)
        if key in failed:
            return False

        remaining = all_mask ^ done
        remaining_count = remaining.bit_count()
        phases_left = T - phase + 1
        if remaining_count > M * phases_left:
            failed.add(key)
            return False

        for d in relevant_deadlines:
            if d < phase:
                if remaining & exact_deadline[d]:
                    failed.add(key)
                    return False
                continue
            required = (remaining & cumulative_deadline[d]).bit_count()
            if required > M * (d - phase + 1):
                failed.add(key)
                return False

        available_mask = 0
        temp = remaining
        while temp:
            bit = temp & -temp
            v = bit.bit_length() - 1
            if pre_mask[v] & remaining == 0:
                available_mask |= bit
            temp ^= bit

        if available_mask == 0:
            failed.add(key)
            return False

        overdue = remaining & cumulative_deadline[phase]
        if overdue & ~available_mask:
            failed.add(key)
            return False

        forced_mask = available_mask & exact_deadline[phase]
        forced_count = forced_mask.bit_count()
        capacity = min(M, available_mask.bit_count())

        if forced_count > capacity:
            failed.add(key)
            return False

        choose_count = capacity - forced_count
        optional_mask = available_mask & ~forced_mask
        optional = []
        temp = optional_mask
        while temp:
            bit = temp & -temp
            v = bit.bit_length() - 1
            optional.append(v)
            temp ^= bit

        optional.sort(key=lambda v: (latest[v], -len(succ[v]), v))

        if choose_count == 0:
            combinations = [()]
        elif choose_count == len(optional):
            combinations = [tuple(optional)]
        else:
            combinations = itertools.combinations(optional, choose_count)

        forced_vertices = []
        temp = forced_mask
        while temp:
            bit = temp & -temp
            forced_vertices.append(bit.bit_length() - 1)
            temp ^= bit

        for comb in combinations:
            selected_mask = forced_mask
            selected_vertices = forced_vertices[:]
            for v in comb:
                selected_mask |= 1 << v
                selected_vertices.append(v)

            for v in selected_vertices:
                assignment[v] = phase

            if dfs(done | selected_mask, phase + 1):
                return True

            for v in selected_vertices:
                assignment[v] = 0

        failed.add(key)
        return False

    if dfs(0, 1):
        print("YES")
        print(*assignment)
    else:
        print("NO")


if __name__ == "__main__":
    main()