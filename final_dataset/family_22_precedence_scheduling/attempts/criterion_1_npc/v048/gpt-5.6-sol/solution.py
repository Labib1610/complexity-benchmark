import sys
import heapq
import itertools
import random
import time

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n, M, T, m = data[:4]
    if M <= 0 or T <= 0 or n > M * T:
        print("NO")
        return

    succ = [[] for _ in range(n)]
    pred = [[] for _ in range(n)]
    pos = 4
    for _ in range(m):
        a = data[pos] - 1
        b = data[pos + 1] - 1
        pos += 2
        succ[a].append(b)
        pred[b].append(a)

    indeg = [len(pred[v]) for v in range(n)]
    heap = [v for v in range(n) if indeg[v] == 0]
    heapq.heapify(heap)
    topo = []

    while heap:
        v = heapq.heappop(heap)
        topo.append(v)
        for u in succ[v]:
            indeg[u] -= 1
            if indeg[u] == 0:
                heapq.heappush(heap, u)

    if len(topo) != n:
        print("NO")
        return

    top_level = [1] * n
    for v in topo:
        nv = top_level[v] + 1
        for u in succ[v]:
            if top_level[u] < nv:
                top_level[u] = nv

    bottom_level = [1] * n
    for v in reversed(topo):
        if succ[v]:
            bottom_level[v] = 1 + max(bottom_level[u] for u in succ[v])

    if max(bottom_level, default=0) > T:
        print("NO")
        return

    def forward_schedule(priority):
        deg = [len(pred[v]) for v in range(n)]
        available = []
        for v in range(n):
            if deg[v] == 0:
                heapq.heappush(available, (priority[v], v))

        answer = [0] * n
        completed = 0
        day = 1

        while available and completed < n and day <= T:
            selected = []
            for _ in range(min(M, len(available))):
                _, v = heapq.heappop(available)
                selected.append(v)

            for v in selected:
                answer[v] = day
                completed += 1

            newly = []
            for v in selected:
                for u in succ[v]:
                    deg[u] -= 1
                    if deg[u] == 0:
                        newly.append(u)
            for u in newly:
                heapq.heappush(available, (priority[u], u))
            day += 1

        return answer if completed == n else None

    def backward_schedule(priority):
        deg = [len(succ[v]) for v in range(n)]
        available = []
        for v in range(n):
            if deg[v] == 0:
                heapq.heappush(available, (priority[v], v))

        answer = [0] * n
        completed = 0
        day = T

        while available and completed < n and day >= 1:
            selected = []
            for _ in range(min(M, len(available))):
                _, v = heapq.heappop(available)
                selected.append(v)

            for v in selected:
                answer[v] = day
                completed += 1

            newly = []
            for v in selected:
                for u in pred[v]:
                    deg[u] -= 1
                    if deg[u] == 0:
                        newly.append(u)
            for u in newly:
                heapq.heappush(available, (priority[u], u))
            day -= 1

        return answer if completed == n else None

    priorities_forward = [
        [(-bottom_level[v], -len(succ[v]), v) for v in range(n)],
        [(-bottom_level[v], -top_level[v], v) for v in range(n)],
        [(-len(succ[v]), -bottom_level[v], v) for v in range(n)],
    ]
    priorities_backward = [
        [(-top_level[v], -len(pred[v]), v) for v in range(n)],
        [(-top_level[v], -bottom_level[v], v) for v in range(n)],
        [(-len(pred[v]), -top_level[v], v) for v in range(n)],
    ]

    for priority in priorities_forward:
        answer = forward_schedule(priority)
        if answer is not None:
            print("YES")
            print(*answer)
            return

    for priority in priorities_backward:
        answer = backward_schedule(priority)
        if answer is not None:
            print("YES")
            print(*answer)
            return

    rng = random.Random(712367821)
    attempts = 24 if n <= 10000 else 6
    for _ in range(attempts):
        noise = [rng.randrange(1 << 30) for _ in range(n)]
        priority = [
            (-bottom_level[v], noise[v], -len(succ[v]), v)
            for v in range(n)
        ]
        answer = forward_schedule(priority)
        if answer is not None:
            print("YES")
            print(*answer)
            return

        priority = [
            (-top_level[v], noise[v], -len(pred[v]), v)
            for v in range(n)
        ]
        answer = backward_schedule(priority)
        if answer is not None:
            print("YES")
            print(*answer)
            return

    if M == 1:
        if n <= T:
            answer = [0] * n
            for day, v in enumerate(topo, 1):
                answer[v] = day
            print("YES")
            print(*answer)
        else:
            print("NO")
        return

    pred_mask = [0] * n
    for v in range(n):
        mask = 0
        for u in pred[v]:
            mask |= 1 << u
        pred_mask[v] = mask

    all_mask = (1 << n) - 1
    failed = set()
    chosen_days = []
    start_time = time.perf_counter()
    calls = 0
    timed_out = False

    order = sorted(
        range(n),
        key=lambda v: (-bottom_level[v], -len(succ[v]), v)
    )

    def necessary(done, day):
        remaining_days = T - day + 1
        remaining_count = n - done.bit_count()
        if remaining_count > remaining_days * M:
            return False

        counts = [0] * (remaining_days + 1)
        for v in range(n):
            if not ((done >> v) & 1):
                level = bottom_level[v]
                if level > remaining_days:
                    return False
                counts[level] += 1

        cumulative = 0
        for level in range(remaining_days, 0, -1):
            cumulative += counts[level]
            available_early_days = remaining_days - level + 1
            if cumulative > available_early_days * M:
                return False
        return True

    def dfs(done, day):
        nonlocal calls, timed_out
        if done == all_mask:
            return True
        if day > T:
            return False

        calls += 1
        if (calls & 1023) == 0 and time.perf_counter() - start_time > 4.65:
            timed_out = True
            return False

        state = (done, day)
        if state in failed:
            return False
        if not necessary(done, day):
            failed.add(state)
            return False

        available = []
        remaining_mask = all_mask ^ done
        for v in order:
            bit = 1 << v
            if remaining_mask & bit and (pred_mask[v] & ~done) == 0:
                available.append(v)

        if not available:
            failed.add(state)
            return False

        take = min(M, len(available))
        if len(available) <= M:
            selected_mask = 0
            for v in available:
                selected_mask |= 1 << v
            chosen_days.append(available)
            if dfs(done | selected_mask, day + 1):
                return True
            chosen_days.pop()
        else:
            for combination in itertools.combinations(available, take):
                selected_mask = 0
                for v in combination:
                    selected_mask |= 1 << v
                chosen_days.append(combination)
                if dfs(done | selected_mask, day + 1):
                    return True
                chosen_days.pop()
                if timed_out:
                    return False

        failed.add(state)
        return False

    sys.setrecursionlimit(max(1000000, T + n + 100))
    if dfs(0, 1):
        answer = [0] * n
        for day, vertices in enumerate(chosen_days, 1):
            for v in vertices:
                answer[v] = day
        print("YES")
        print(*answer)
    else:
        print("NO")

if __name__ == "__main__":
    main()