import sys
import heapq
import random
import time
from itertools import combinations


def output_yes(ans):
    sys.stdout.write("YES\n")
    sys.stdout.write(" ".join(map(str, ans[1:])) + "\n")
    raise SystemExit


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if len(data) < 4:
        return

    n, M, T, m = data[:4]
    graph = [[] for _ in range(n)]
    rev = [[] for _ in range(n)]
    indeg = [0] * n

    p = 4
    for _ in range(m):
        u = data[p] - 1
        v = data[p + 1] - 1
        p += 2
        graph[u].append(v)
        rev[v].append(u)
        indeg[v] += 1

    if M <= 0 or T <= 0 or n > M * T:
        print("NO")
        return

    # Topological sorting and cycle detection.
    q = [i for i in range(n) if indeg[i] == 0]
    topo = []
    head = 0
    indeg_work = indeg[:]
    while head < len(q):
        u = q[head]
        head += 1
        topo.append(u)
        for v in graph[u]:
            indeg_work[v] -= 1
            if indeg_work[v] == 0:
                q.append(v)

    if len(topo) != n:
        print("NO")
        return

    # Longest path from each vertex to a sink.
    bottom = [1] * n
    for u in reversed(topo):
        best = 0
        for v in graph[u]:
            if bottom[v] > best:
                best = bottom[v]
        bottom[u] = best + 1

    if max(bottom, default=0) > T:
        print("NO")
        return

    # Longest path from a source to each vertex.
    top = [1] * n
    for u in topo:
        nu = top[u] + 1
        for v in graph[u]:
            if nu > top[v]:
                top[v] = nu

    def forward_schedule(noise=0.0, seed=0):
        rng = random.Random(seed)
        deg = indeg[:]
        heap = []

        def key(v):
            r = rng.random() if noise else 0.0
            return (-(bottom[v] + noise * r), -len(graph[v]), v)

        for v in range(n):
            if deg[v] == 0:
                heapq.heappush(heap, key(v))

        ans = [0] * (n + 1)
        done = 0
        day = 1

        while heap:
            selected = []
            take = min(M, len(heap))
            for _ in range(take):
                selected.append(heapq.heappop(heap)[2])

            if day > T:
                return None

            newly = []
            for u in selected:
                ans[u + 1] = day
                done += 1
                for v in graph[u]:
                    deg[v] -= 1
                    if deg[v] == 0:
                        newly.append(v)

            for v in newly:
                heapq.heappush(heap, key(v))
            day += 1

        return ans if done == n else None

    def backward_schedule(noise=0.0, seed=0):
        rng = random.Random(seed)
        outdeg = [len(graph[v]) for v in range(n)]
        heap = []

        def key(v):
            r = rng.random() if noise else 0.0
            return (-(top[v] + noise * r), -len(rev[v]), v)

        for v in range(n):
            if outdeg[v] == 0:
                heapq.heappush(heap, key(v))

        ans = [0] * (n + 1)
        done = 0
        day = T

        while heap:
            selected = []
            take = min(M, len(heap))
            for _ in range(take):
                selected.append(heapq.heappop(heap)[2])

            if day < 1:
                return None

            newly = []
            for u in selected:
                ans[u + 1] = day
                done += 1
                for v in rev[u]:
                    outdeg[v] -= 1
                    if outdeg[v] == 0:
                        newly.append(v)

            for v in newly:
                heapq.heappush(heap, key(v))
            day -= 1

        return ans if done == n else None

    ans = forward_schedule()
    if ans is not None:
        output_yes(ans)

    ans = backward_schedule()
    if ans is not None:
        output_yes(ans)

    # Coffman-Graham labeling and scheduling.
    out_remaining = [len(graph[v]) for v in range(n)]
    labels = [0] * n
    label_heap = []
    for v in range(n):
        if out_remaining[v] == 0:
            heapq.heappush(label_heap, ((), v))

    for lab in range(1, n + 1):
        if not label_heap:
            break
        _, u = heapq.heappop(label_heap)
        labels[u] = lab
        for pnode in rev[u]:
            out_remaining[pnode] -= 1
            if out_remaining[pnode] == 0:
                signature = tuple(sorted((labels[x] for x in graph[pnode]), reverse=True))
                heapq.heappush(label_heap, (signature, pnode))

    if all(labels):
        order = sorted(range(n), key=lambda x: labels[x], reverse=True)
        assigned = [0] * n
        capacity = [0] * (n + 2)
        parent = list(range(n + 3))

        def find(x):
            y = x
            while parent[y] != y:
                y = parent[y]
            while parent[x] != x:
                z = parent[x]
                parent[x] = y
                x = z
            return y

        valid = True
        max_day = 0
        for u in order:
            required = 1
            for pre in rev[u]:
                d = assigned[pre] + 1
                if d > required:
                    required = d
            day = find(required)
            if day > T:
                valid = False
                break
            assigned[u] = day
            capacity[day] += 1
            if day > max_day:
                max_day = day
            if capacity[day] == M:
                parent[day] = find(day + 1)

        if valid and max_day <= T:
            ans = [0] + assigned
            output_yes(ans)

    # Additional randomized list schedules.
    trials = 10 if n <= 20000 else 3
    noises = (0.35, 0.9, 2.0, 5.0)
    for trial in range(trials):
        noise = noises[trial % len(noises)]
        ans = forward_schedule(noise, 9176 + trial * 1009)
        if ans is not None:
            output_yes(ans)
        ans = backward_schedule(noise, 19391 + trial * 1013)
        if ans is not None:
            output_yes(ans)

    # Exact search for moderate instances, with a time guard.
    if n <= 70:
        pred_mask = [0] * n
        for v in range(n):
            mask = 0
            for u in rev[v]:
                mask |= 1 << u
            pred_mask[v] = mask

        full_mask = (1 << n) - 1
        exact_ans = [0] * n
        failed = set()
        deadline = time.perf_counter() + 3.5

        class SearchTimeout(Exception):
            pass

        def dfs(day, done_mask):
            if time.perf_counter() > deadline:
                raise SearchTimeout

            if done_mask == full_mask:
                return True
            if day > T:
                return False

            state = (day, done_mask)
            if state in failed:
                return False

            remaining_days = T - day + 1
            remaining_count = n - done_mask.bit_count()
            if remaining_count > remaining_days * M:
                failed.add(state)
                return False

            available = []
            mandatory = []
            for v in range(n):
                bit = 1 << v
                if done_mask & bit:
                    continue
                if bottom[v] > remaining_days:
                    failed.add(state)
                    return False
                if pred_mask[v] & ~done_mask == 0:
                    available.append(v)
                    if bottom[v] == remaining_days:
                        mandatory.append(v)

            if not available:
                failed.add(state)
                return False

            k = min(M, len(available))
            if len(mandatory) > k:
                failed.add(state)
                return False

            mandatory_set = set(mandatory)
            optional = [v for v in available if v not in mandatory_set]
            optional.sort(key=lambda v: (-bottom[v], -len(graph[v]), v))
            mandatory.sort(key=lambda v: (-bottom[v], -len(graph[v]), v))
            choose_count = k - len(mandatory)

            if choose_count == 0:
                choices = [()]
            elif choose_count == len(optional):
                choices = [tuple(optional)]
            else:
                choices = combinations(optional, choose_count)

            for extra in choices:
                selected = mandatory + list(extra)
                new_mask = done_mask
                for v in selected:
                    new_mask |= 1 << v
                    exact_ans[v] = day

                if dfs(day + 1, new_mask):
                    return True

                for v in selected:
                    exact_ans[v] = 0

            failed.add(state)
            return False

        try:
            if dfs(1, 0):
                output_yes([0] + exact_ans)
        except SearchTimeout:
            pass

    print("NO")


if __name__ == "__main__":
    main()