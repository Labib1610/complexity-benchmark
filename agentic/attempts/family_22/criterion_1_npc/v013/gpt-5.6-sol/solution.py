import sys
import heapq
import itertools
from functools import lru_cache

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n, M, T, m = data[:4]
    adj = [[] for _ in range(n)]
    rev = [[] for _ in range(n)]
    indeg = [0] * n

    p = 4
    for _ in range(m):
        a = data[p] - 1
        b = data[p + 1] - 1
        p += 2
        adj[a].append(b)
        rev[b].append(a)
        indeg[b] += 1

    if n > M * T:
        print("NO")
        return

    # Topological order and cycle detection.
    q = [v for v in range(n) if indeg[v] == 0]
    heapq.heapify(q)
    topo = []
    deg = indeg[:]
    while q:
        v = heapq.heappop(q)
        topo.append(v)
        for w in adj[v]:
            deg[w] -= 1
            if deg[w] == 0:
                heapq.heappush(q, w)

    if len(topo) != n:
        print("NO")
        return

    # Longest path beginning/ending at each vertex.
    bottom = [1] * n
    for v in reversed(topo):
        if adj[v]:
            bottom[v] = 1 + max(bottom[w] for w in adj[v])

    if max(bottom, default=0) > T:
        print("NO")
        return

    top = [1] * n
    for v in topo:
        tv = top[v] + 1
        for w in adj[v]:
            if top[w] < tv:
                top[w] = tv

    if M == 1:
        if n > T:
            print("NO")
            return
        ans = [0] * n
        for i, v in enumerate(topo, 1):
            ans[v] = i
        print("YES")
        print(*ans)
        return

    if M >= n:
        ans = top
        print("YES")
        print(*ans)
        return

    def forward_schedule(priority):
        d = indeg[:]
        heap = []
        for v in range(n):
            if d[v] == 0:
                heapq.heappush(heap, (-priority[v], v))

        ans = [0] * n
        done = 0
        slot = 1

        while heap and slot <= T:
            selected = []
            take = min(M, len(heap))
            for _ in range(take):
                _, v = heapq.heappop(heap)
                selected.append(v)
                ans[v] = slot

            done += len(selected)
            for v in selected:
                for w in adj[v]:
                    d[w] -= 1
                    if d[w] == 0:
                        heapq.heappush(heap, (-priority[w], w))
            slot += 1

        return ans if done == n else None

    def backward_schedule(priority):
        outdeg = [len(adj[v]) for v in range(n)]
        heap = []
        for v in range(n):
            if outdeg[v] == 0:
                heapq.heappush(heap, (-priority[v], v))

        ans = [0] * n
        done = 0
        slot = T

        while heap and slot >= 1:
            selected = []
            take = min(M, len(heap))
            for _ in range(take):
                _, v = heapq.heappop(heap)
                selected.append(v)
                ans[v] = slot

            done += len(selected)
            for v in selected:
                for u in rev[v]:
                    outdeg[u] -= 1
                    if outdeg[u] == 0:
                        heapq.heappush(heap, (-priority[u], u))
            slot -= 1

        return ans if done == n else None

    # Highest-level-first schedules in both directions.
    ans = forward_schedule(bottom)
    if ans is not None:
        print("YES")
        print(*ans)
        return

    ans = backward_schedule(top)
    if ans is not None:
        print("YES")
        print(*ans)
        return

    # Coffman-Graham-style priority order, particularly effective for M = 2.
    if M == 2 or n <= 5000:
        remaining_successors = [len(adj[v]) for v in range(n)]
        cg_heap = []
        labels = [0] * n

        for v in range(n):
            if remaining_successors[v] == 0:
                heapq.heappush(cg_heap, ((), v))

        label = 1
        while cg_heap:
            _, v = heapq.heappop(cg_heap)
            labels[v] = label
            label += 1
            for u in rev[v]:
                remaining_successors[u] -= 1
                if remaining_successors[u] == 0:
                    key = tuple(sorted((labels[w] for w in adj[u]), reverse=True))
                    heapq.heappush(cg_heap, (key, u))

        ans = forward_schedule(labels)
        if ans is not None:
            print("YES")
            print(*ans)
            return

    # Exact search for small instances.
    if n <= 20:
        prereq = [0] * n
        for v in range(n):
            mask = 0
            for u in rev[v]:
                mask |= 1 << u
            prereq[v] = mask

        full = (1 << n) - 1
        choice_at = {}

        @lru_cache(None)
        def dfs(mask, slot):
            if mask == full:
                return True
            if slot > T:
                return False

            remaining_count = n - mask.bit_count()
            remaining_slots = T - slot + 1
            if remaining_count > M * remaining_slots:
                return False

            available = []
            max_bottom = 0
            not_done = full ^ mask
            x = not_done
            while x:
                bit = x & -x
                v = bit.bit_length() - 1
                x -= bit
                if prereq[v] & ~mask == 0:
                    available.append(v)
                    if bottom[v] > max_bottom:
                        max_bottom = bottom[v]

            if not available or max_bottom > remaining_slots:
                return False

            available.sort(key=lambda v: (-bottom[v], -len(adj[v]), v))
            k = min(M, len(available))

            if len(available) <= M:
                add = 0
                for v in available:
                    add |= 1 << v
                if dfs(mask | add, slot + 1):
                    choice_at[(mask, slot)] = add
                    return True
                return False

            for comb in itertools.combinations(available, k):
                add = 0
                for v in comb:
                    add |= 1 << v
                if dfs(mask | add, slot + 1):
                    choice_at[(mask, slot)] = add
                    return True
            return False

        if dfs(0, 1):
            ans = [0] * n
            mask = 0
            slot = 1
            while mask != full:
                add = choice_at[(mask, slot)]
                x = add
                while x:
                    bit = x & -x
                    v = bit.bit_length() - 1
                    x -= bit
                    ans[v] = slot
                mask |= add
                slot += 1
            print("YES")
            print(*ans)
            return

    # Additional deterministic priority trials.
    work = n + m
    if work <= 100000:
        trials = 10
    elif work <= 500000:
        trials = 4
    else:
        trials = 2

    mask64 = (1 << 64) - 1
    for seed in range(1, trials + 1):
        random_key = [0] * n
        z = (0x9E3779B97F4A7C15 * seed) & mask64
        for v in range(n):
            z ^= (z << 13) & mask64
            z ^= z >> 7
            z ^= (z << 17) & mask64
            random_key[v] = z

        if seed & 1:
            priority = [
                bottom[v] * (1 << 64) + random_key[v]
                for v in range(n)
            ]
            ans = forward_schedule(priority)
        else:
            priority = [
                top[v] * (1 << 64) + random_key[v]
                for v in range(n)
            ]
            ans = backward_schedule(priority)

        if ans is not None:
            print("YES")
            print(*ans)
            return

    print("NO")


if __name__ == "__main__":
    main()