import sys
import heapq
import itertools
import time

sys.setrecursionlimit(1_000_000)


def topological_order(n, succ, indeg):
    deg = indeg[:]
    heap = [i for i in range(n) if deg[i] == 0]
    heapq.heapify(heap)
    order = []

    while heap:
        u = heapq.heappop(heap)
        order.append(u)
        for v in succ[u]:
            deg[v] -= 1
            if deg[v] == 0:
                heapq.heappush(heap, v)

    return order if len(order) == n else None


def calculate_height(n, succ, order):
    height = [1] * n
    for u in reversed(order):
        if succ[u]:
            height[u] = 1 + max(height[v] for v in succ[u])
    return height


def list_schedule(n, M, T, succ, indeg, height, mode):
    degree = [len(x) for x in succ]
    remaining = indeg[:]
    available = []
    assignment = [0] * n

    def priority(u):
        h = height[u]
        d = degree[u]
        if mode == 0:
            return (-h, -d, u)
        if mode == 1:
            return (-h, d, u)
        if mode == 2:
            return (-d, -h, u)
        if mode == 3:
            return (-(h * (n + 1) + d), u)
        if mode == 4:
            mixed = ((u + 1) * 0x9E3779B1) & 0xFFFFFFFF
            return (-h, mixed, u)
        mixed = ((u + 7) * 0x85EBCA6B) & 0xFFFFFFFF
        return (-(3 * h + min(d, 3)), mixed, u)

    for u in range(n):
        if remaining[u] == 0:
            heapq.heappush(available, priority(u))

    done = 0
    cycle = 0

    while done < n:
        if not available:
            return None

        cycle += 1
        if cycle > T:
            return None

        batch = []
        for _ in range(min(M, len(available))):
            item = heapq.heappop(available)
            u = item[-1]
            batch.append(u)

        for u in batch:
            assignment[u] = cycle

        newly_available = []
        for u in batch:
            for v in succ[u]:
                remaining[v] -= 1
                if remaining[v] == 0:
                    newly_available.append(v)

        for v in newly_available:
            heapq.heappush(available, priority(v))

        done += len(batch)

    return assignment


def exact_schedule(n, M, T, pred, succ, height, deadline_time):
    full = (1 << n) - 1
    pred_mask = [0] * n
    succ_mask = [0] * n

    for u in range(n):
        pm = 0
        for v in pred[u]:
            pm |= 1 << v
        pred_mask[u] = pm

        sm = 0
        for v in succ[u]:
            sm |= 1 << v
        succ_mask[u] = sm

    failed = set()
    batches = []
    calls = 0
    timed_out = False

    def dfs(done, cycle):
        nonlocal calls, timed_out

        if done == full:
            return True
        if cycle >= T:
            return False

        calls += 1
        if (calls & 1023) == 0 and time.perf_counter() > deadline_time:
            timed_out = True
            return False

        state = (done, cycle)
        if state in failed:
            return False

        remaining_count = n - done.bit_count()
        remaining_cycles = T - cycle

        if remaining_count > remaining_cycles * M:
            failed.add(state)
            return False

        available = []
        deadlines = []

        for u in range(n):
            bit = 1 << u
            if done & bit:
                continue

            h = height[u]
            if h > remaining_cycles:
                failed.add(state)
                return False

            deadlines.append(remaining_cycles - h + 1)
            if pred_mask[u] & ~done == 0:
                available.append(u)

        deadlines.sort()
        for count, d in enumerate(deadlines, 1):
            if count > d * M:
                failed.add(state)
                return False

        if not available:
            failed.add(state)
            return False

        available.sort(
            key=lambda u: (
                -height[u],
                -succ_mask[u].bit_count(),
                -len(succ[u]),
                u
            )
        )

        if len(available) <= M:
            batch_mask = 0
            for u in available:
                batch_mask |= 1 << u
            batches.append(batch_mask)
            if dfs(done | batch_mask, cycle + 1):
                return True
            batches.pop()
            if not timed_out:
                failed.add(state)
            return False

        mandatory = [u for u in available if height[u] == remaining_cycles]
        if len(mandatory) > M:
            failed.add(state)
            return False

        mandatory_mask = 0
        mandatory_set = set(mandatory)
        for u in mandatory:
            mandatory_mask |= 1 << u

        optional = [u for u in available if u not in mandatory_set]
        choose = M - len(mandatory)

        if choose < 0 or choose > len(optional):
            failed.add(state)
            return False

        for combination in itertools.combinations(optional, choose):
            batch_mask = mandatory_mask
            for u in combination:
                batch_mask |= 1 << u

            batches.append(batch_mask)
            if dfs(done | batch_mask, cycle + 1):
                return True
            batches.pop()

            if timed_out:
                return False

        failed.add(state)
        return False

    if not dfs(0, 0):
        return None

    assignment = [0] * n
    for cycle, mask in enumerate(batches, 1):
        while mask:
            bit = mask & -mask
            u = bit.bit_length() - 1
            assignment[u] = cycle
            mask ^= bit

    return assignment


def main():
    start_time = time.perf_counter()
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

    succ = [[] for _ in range(n)]
    pred = [[] for _ in range(n)]
    indeg = [0] * n

    seen = set()
    pos = 4
    for _ in range(m):
        a = data[pos] - 1
        b = data[pos + 1] - 1
        pos += 2

        edge = a * n + b
        if edge in seen:
            continue
        seen.add(edge)

        succ[a].append(b)
        pred[b].append(a)
        indeg[b] += 1

    order = topological_order(n, succ, indeg)
    if order is None:
        print("NO")
        return

    height = calculate_height(n, succ, order)
    if max(height) > T:
        print("NO")
        return

    modes = range(6 if n <= 5000 else 3)

    for mode in modes:
        answer = list_schedule(n, M, T, succ, indeg, height, mode)
        if answer is not None:
            print("YES")
            print(*answer)
            return

    reverse_succ = pred
    reverse_pred = succ
    reverse_indeg = [len(reverse_pred[u]) for u in range(n)]
    reverse_order = list(reversed(order))
    reverse_height = calculate_height(n, reverse_succ, reverse_order)

    for mode in modes:
        reverse_answer = list_schedule(
            n, M, T, reverse_succ, reverse_indeg, reverse_height, mode
        )
        if reverse_answer is not None:
            used = max(reverse_answer)
            answer = [used + 1 - reverse_answer[u] for u in range(n)]
            print("YES")
            print(*answer)
            return

    deadline_time = start_time + 4.85

    if n <= 90:
        original_sources = sum(1 for x in indeg if x == 0)
        reverse_sources = sum(1 for x in reverse_indeg if x == 0)

        if reverse_sources < original_sources:
            reverse_answer = exact_schedule(
                n, M, T, reverse_pred, reverse_succ,
                reverse_height, deadline_time
            )
            if reverse_answer is not None:
                used = max(reverse_answer)
                answer = [used + 1 - reverse_answer[u] for u in range(n)]
                print("YES")
                print(*answer)
                return
        else:
            answer = exact_schedule(
                n, M, T, pred, succ, height, deadline_time
            )
            if answer is not None:
                print("YES")
                print(*answer)
                return

    print("NO")


if __name__ == "__main__":
    main()