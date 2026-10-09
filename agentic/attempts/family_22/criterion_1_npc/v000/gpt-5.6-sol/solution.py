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

    graph = [[] for _ in range(n)]
    reverse_graph = [[] for _ in range(n)]
    indegree = [0] * n

    p = 4
    for _ in range(m):
        a = data[p] - 1
        b = data[p + 1] - 1
        p += 2
        graph[a].append(b)
        reverse_graph[b].append(a)
        indegree[b] += 1

    # Topological ordering and cycle detection.
    queue = [i for i in range(n) if indegree[i] == 0]
    heapq.heapify(queue)
    topo = []
    deg = indegree[:]

    while queue:
        u = heapq.heappop(queue)
        topo.append(u)
        for v in graph[u]:
            deg[v] -= 1
            if deg[v] == 0:
                heapq.heappush(queue, v)

    if len(topo) != n:
        print("NO")
        return

    earliest = [1] * n
    for u in topo:
        eu = earliest[u] + 1
        for v in graph[u]:
            if earliest[v] < eu:
                earliest[v] = eu

    if max(earliest) > T:
        print("NO")
        return

    bottom = [1] * n
    for u in reversed(topo):
        best = 0
        for v in graph[u]:
            if bottom[v] > best:
                best = bottom[v]
        bottom[u] = best + 1

    def list_schedule(mode):
        d = indegree[:]
        ready = []

        def priority(u):
            if mode == 0:
                return (-bottom[u], -len(graph[u]), u)
            if mode == 1:
                return (-len(graph[u]), -bottom[u], u)
            return (-earliest[u], -bottom[u], u)

        for i in range(n):
            if d[i] == 0:
                heapq.heappush(ready, priority(i))

        slots = [0] * n
        done = 0
        current_slot = 1

        while ready:
            batch = []
            for _ in range(min(M, len(ready))):
                item = heapq.heappop(ready)
                batch.append(item[-1])

            for u in batch:
                slots[u] = current_slot
                done += 1

            new_ready = []
            for u in batch:
                for v in graph[u]:
                    d[v] -= 1
                    if d[v] == 0:
                        new_ready.append(v)

            for v in new_ready:
                heapq.heappush(ready, priority(v))

            current_slot += 1

        if done == n and current_slot - 1 <= T:
            return slots
        return None

    # Fast attempts; if one succeeds, no exponential search is needed.
    for mode in range(3):
        answer = list_schedule(mode)
        if answer is not None:
            print("YES")
            print(*answer)
            return

    # Exact backward search.
    pred_mask = [0] * n
    succ_mask = [0] * n
    for u in range(n):
        pm = 0
        for v in reverse_graph[u]:
            pm |= 1 << v
        pred_mask[u] = pm

        sm = 0
        for v in graph[u]:
            sm |= 1 << v
        succ_mask[u] = sm

    full_mask = (1 << n) - 1
    answer = [0] * n
    failed = set()

    def dfs(remaining, time_slot):
        if remaining == 0:
            return True
        if time_slot <= 0:
            return False

        count_remaining = remaining.bit_count()
        if count_remaining > M * time_slot:
            return False

        key = (remaining, time_slot)
        if key in failed:
            return False

        sinks = []
        mandatory = []
        level_counts = {}

        x = remaining
        while x:
            bit = x & -x
            u = bit.bit_length() - 1
            x ^= bit

            lv = earliest[u]
            if lv > time_slot:
                failed.add(key)
                return False
            level_counts[lv] = level_counts.get(lv, 0) + 1

            if (succ_mask[u] & remaining) == 0:
                sinks.append(u)
                if lv == time_slot:
                    mandatory.append(u)

        # Jobs with earliest slot >= k must fit in slots k..time_slot.
        cumulative = 0
        for lv in sorted(level_counts, reverse=True):
            cumulative += level_counts[lv]
            if cumulative > M * (time_slot - lv + 1):
                failed.add(key)
                return False

        if not sinks or len(mandatory) > M:
            failed.add(key)
            return False

        take = min(M, len(sinks))
        mandatory_set = set(mandatory)
        optional = [u for u in sinks if u not in mandatory_set]
        need = take - len(mandatory)

        optional.sort(
            key=lambda u: (
                -earliest[u],
                -(pred_mask[u] & remaining).bit_count(),
                -len(reverse_graph[u]),
                u
            )
        )

        if need == 0:
            choices = [()]
        elif need == len(optional):
            choices = [tuple(optional)]
        else:
            choices = itertools.combinations(optional, need)

        mandatory_mask = 0
        for u in mandatory:
            mandatory_mask |= 1 << u

        for choice in choices:
            selected_mask = mandatory_mask
            selected_jobs = mandatory[:]

            for u in choice:
                selected_mask |= 1 << u
                selected_jobs.append(u)

            for u in selected_jobs:
                answer[u] = time_slot

            if dfs(remaining ^ selected_mask, time_slot - 1):
                return True

            for u in selected_jobs:
                answer[u] = 0

        failed.add(key)
        return False

    if dfs(full_mask, T):
        print("YES")
        print(*answer)
    else:
        print("NO")

if __name__ == "__main__":
    main()