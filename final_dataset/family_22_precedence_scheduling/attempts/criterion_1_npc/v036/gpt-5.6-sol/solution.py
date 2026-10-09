import sys
import heapq
import itertools

sys.setrecursionlimit(1_000_000)


def build_topological(n, succ, indeg):
    deg = indeg[:]
    q = [i for i in range(n) if deg[i] == 0]
    heapq.heapify(q)
    order = []

    while q:
        u = heapq.heappop(q)
        order.append(u)
        for v in succ[u]:
            deg[v] -= 1
            if deg[v] == 0:
                heapq.heappush(q, v)

    return order if len(order) == n else None


def compute_tail(n, succ, topo):
    tail = [1] * n
    for u in reversed(topo):
        best = 0
        for v in succ[u]:
            if tail[v] > best:
                best = tail[v]
        tail[u] = best + 1
    return tail


def greedy_schedule(n, M, T, succ, pred, topo, mode):
    tail = compute_tail(n, succ, topo)
    indeg = [len(pred[i]) for i in range(n)]

    def key(v):
        if mode == 0:
            return (-tail[v], -len(succ[v]), v)
        if mode == 1:
            return (-len(succ[v]), -tail[v], v)
        return (-tail[v], len(pred[v]), v)

    heap = []
    for v in range(n):
        if indeg[v] == 0:
            heapq.heappush(heap, (key(v), v))

    assignment = [0] * n
    completed = 0
    stage = 1

    while heap:
        if stage > T:
            return None

        batch = []
        for _ in range(min(M, len(heap))):
            _, u = heapq.heappop(heap)
            batch.append(u)

        for u in batch:
            assignment[u] = stage
            completed += 1

        for u in batch:
            for v in succ[u]:
                indeg[v] -= 1
                if indeg[v] == 0:
                    heapq.heappush(heap, (key(v), v))

        stage += 1

    if completed == n:
        return assignment
    return None


def exact_schedule(n, M, T, succ, pred, topo):
    tail = compute_tail(n, succ, topo)
    if max(tail, default=0) > T:
        return None

    pred_mask = [0] * n
    for v in range(n):
        mask = 0
        for u in pred[v]:
            mask |= 1 << u
        pred_mask[v] = mask

    latest = [T - tail[v] + 1 for v in range(n)]
    deadline_order = sorted(range(n), key=lambda v: latest[v])
    priority = sorted(
        range(n),
        key=lambda v: (latest[v], -tail[v], -len(succ[v]), v)
    )
    priority_rank = [0] * n
    for i, v in enumerate(priority):
        priority_rank[v] = i

    full_mask = (1 << n) - 1
    assignment = [0] * n
    failed = set()

    def deadline_capacity_ok(done, stage):
        count = 0
        i = 0
        while i < n:
            d = latest[deadline_order[i]]
            j = i
            while j < n and latest[deadline_order[j]] == d:
                v = deadline_order[j]
                if not ((done >> v) & 1):
                    count += 1
                j += 1

            if count:
                if d < stage:
                    return False
                if count > M * (d - stage + 1):
                    return False
            i = j
        return True

    def dfs(done, stage):
        if done == full_mask:
            return True
        if stage > T:
            return False

        state = (done, stage)
        if state in failed:
            return False

        remaining = n - done.bit_count()
        if remaining > M * (T - stage + 1):
            failed.add(state)
            return False

        if not deadline_capacity_ok(done, stage):
            failed.add(state)
            return False

        available = []
        forced = []

        for v in range(n):
            if (done >> v) & 1:
                continue
            if pred_mask[v] & ~done == 0:
                available.append(v)
                if latest[v] == stage:
                    forced.append(v)

        if not available or len(forced) > M:
            failed.add(state)
            return False

        if len(available) <= M:
            batches = (tuple(available),)
        else:
            forced_set = set(forced)
            candidates = [v for v in available if v not in forced_set]
            candidates.sort(key=lambda v: priority_rank[v])
            need = M - len(forced)

            if need < 0 or need > len(candidates):
                failed.add(state)
                return False

            batches = (
                tuple(forced) + comb
                for comb in itertools.combinations(candidates, need)
            )

        for batch in batches:
            new_done = done
            for v in batch:
                new_done |= 1 << v
                assignment[v] = stage

            if dfs(new_done, stage + 1):
                return True

            for v in batch:
                assignment[v] = 0

        failed.add(state)
        return False

    if dfs(0, 1):
        return assignment
    return None


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

    succ = [[] for _ in range(n)]
    pred = [[] for _ in range(n)]
    seen = set()

    p = 4
    for _ in range(m):
        a = data[p] - 1
        b = data[p + 1] - 1
        p += 2
        if not (0 <= a < n and 0 <= b < n):
            print("NO")
            return
        edge = (a, b)
        if edge not in seen:
            seen.add(edge)
            succ[a].append(b)
            pred[b].append(a)

    topo = build_topological(n, succ, [len(pred[i]) for i in range(n)])
    if topo is None:
        print("NO")
        return

    reverse_succ = [lst[:] for lst in pred]
    reverse_pred = [lst[:] for lst in succ]
    reverse_topo = list(reversed(topo))

    for mode in range(3):
        ans = greedy_schedule(n, M, T, succ, pred, topo, mode)
        if ans is not None:
            print("YES")
            print(*ans)
            return

        rev = greedy_schedule(
            n, M, T, reverse_succ, reverse_pred, reverse_topo, mode
        )
        if rev is not None:
            ans = [T + 1 - x for x in rev]
            print("YES")
            print(*ans)
            return

    forward_sources = sum(1 for v in range(n) if not pred[v])
    reverse_sources = sum(1 for v in range(n) if not succ[v])

    if forward_sources <= reverse_sources:
        ans = exact_schedule(n, M, T, succ, pred, topo)
        if ans is not None:
            print("YES")
            print(*ans)
            return
    else:
        rev = exact_schedule(
            n, M, T, reverse_succ, reverse_pred, reverse_topo
        )
        if rev is not None:
            ans = [T + 1 - x for x in rev]
            print("YES")
            print(*ans)
            return

    print("NO")


if __name__ == "__main__":
    main()