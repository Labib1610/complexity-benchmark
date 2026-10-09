import sys
import time
import heapq
import itertools
import random

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

    adj = [[] for _ in range(n)]
    rev = [[] for _ in range(n)]
    indeg = [0] * n
    outdeg = [0] * n

    p = 4
    valid = True
    for _ in range(m):
        a = data[p] - 1
        b = data[p + 1] - 1
        p += 2
        if not (0 <= a < n and 0 <= b < n) or a == b:
            valid = False
            continue
        adj[a].append(b)
        rev[b].append(a)
        indeg[b] += 1
        outdeg[a] += 1

    if not valid:
        print("NO")
        return

    # Topological ordering and cycle detection.
    deg = indeg[:]
    queue = [i for i in range(n) if deg[i] == 0]
    topo = []
    head = 0
    while head < len(queue):
        u = queue[head]
        head += 1
        topo.append(u)
        for v in adj[u]:
            deg[v] -= 1
            if deg[v] == 0:
                queue.append(v)

    if len(topo) != n:
        print("NO")
        return

    # Longest path lengths toward a sink and from a source.
    rank = [1] * n
    for u in reversed(topo):
        best = 0
        for v in adj[u]:
            if rank[v] > best:
                best = rank[v]
        rank[u] = best + 1

    depth = [1] * n
    for u in topo:
        du = depth[u] + 1
        for v in adj[u]:
            if du > depth[v]:
                depth[v] = du

    if max(rank) > T:
        print("NO")
        return

    if M >= n:
        answer = depth
        if max(answer) <= T:
            print("YES")
            print(*answer)
        else:
            print("NO")
        return

    rng = random.Random(712367821)
    random_key = [rng.randrange(1 << 30) for _ in range(n)]

    def forward_greedy(mode):
        d = indeg[:]
        heap = []

        def key(u):
            if mode == 0:
                return (-rank[u], -outdeg[u], u)
            if mode == 1:
                return (-rank[u], -len(adj[u]), random_key[u])
            if mode == 2:
                return (-outdeg[u], -rank[u], u)
            if mode == 3:
                return (-rank[u], random_key[u], u)
            return (-depth[u], -rank[u], u)

        for u in range(n):
            if d[u] == 0:
                heapq.heappush(heap, (key(u), u))

        ans = [0] * n
        done_count = 0
        cycle = 0

        while heap:
            cycle += 1
            selected = []
            for _ in range(min(M, len(heap))):
                selected.append(heapq.heappop(heap)[1])

            for u in selected:
                ans[u] = cycle
                done_count += 1

            newly = []
            for u in selected:
                for v in adj[u]:
                    d[v] -= 1
                    if d[v] == 0:
                        newly.append(v)
            for v in newly:
                heapq.heappush(heap, (key(v), v))

            if cycle > T:
                return None

        return ans if done_count == n else None

    def backward_greedy(mode):
        d = outdeg[:]
        heap = []

        def key(u):
            if mode == 0:
                return (-depth[u], -indeg[u], u)
            if mode == 1:
                return (-depth[u], random_key[u], u)
            return (-indeg[u], -depth[u], u)

        for u in range(n):
            if d[u] == 0:
                heapq.heappush(heap, (key(u), u))

        batches = []
        done_count = 0
        while heap:
            selected = []
            for _ in range(min(M, len(heap))):
                selected.append(heapq.heappop(heap)[1])
            batches.append(selected)
            done_count += len(selected)

            newly = []
            for u in selected:
                for v in rev[u]:
                    d[v] -= 1
                    if d[v] == 0:
                        newly.append(v)
            for v in newly:
                heapq.heappush(heap, (key(v), v))

            if len(batches) > T:
                return None

        if done_count != n:
            return None

        k = len(batches)
        ans = [0] * n
        for j, batch in enumerate(batches):
            cycle = k - j
            for u in batch:
                ans[u] = cycle
        return ans

    for mode in range(5):
        ans = forward_greedy(mode)
        if ans is not None:
            print("YES")
            print(*ans)
            return

    for mode in range(3):
        ans = backward_greedy(mode)
        if ans is not None:
            print("YES")
            print(*ans)
            return

    # Exact branch-and-bound search.
    pred_mask = [0] * n
    for u in range(n):
        mask = 0
        for v in rev[u]:
            mask |= 1 << v
        pred_mask[u] = mask

    all_mask = (1 << n) - 1
    horizon = min(T, n)
    path = []
    failed = set()
    start_time = time.monotonic()
    deadline = start_time + 4.75
    calls = 0

    class Timeout(Exception):
        pass

    def dfs(done, slots):
        nonlocal calls
        calls += 1
        if (calls & 1023) == 0 and time.monotonic() > deadline:
            raise Timeout

        if done == all_mask:
            return True
        if slots == 0:
            return False
        if done in failed:
            return False

        remaining_mask = all_mask ^ done
        remaining_count = remaining_mask.bit_count()
        if remaining_count > M * slots:
            failed.add(done)
            return False

        available = []
        counts = [0] * (slots + 2)
        mandatory = []

        x = remaining_mask
        while x:
            bit = x & -x
            u = bit.bit_length() - 1
            x -= bit

            r = rank[u]
            if r > slots:
                failed.add(done)
                return False
            counts[r] += 1
            if pred_mask[u] & remaining_mask == 0:
                available.append(u)
                if r == slots:
                    mandatory.append(u)

        if not available:
            failed.add(done)
            return False

        # Cumulative deadline-capacity conditions.
        cumulative = 0
        restriction = 1
        for r in range(slots, 0, -1):
            cumulative += counts[r]
            capacity = M * (slots - r + 1)
            if cumulative > capacity:
                failed.add(done)
                return False
            if cumulative == capacity:
                restriction = max(restriction, r)

        mandatory_set = set(mandatory)
        if len(mandatory) > M:
            failed.add(done)
            return False

        take = min(M, len(available))
        if len(available) <= M:
            batches = [tuple(available)]
        else:
            allowed = [u for u in available if rank[u] >= restriction]
            if len(allowed) < take:
                failed.add(done)
                return False
            if any(u not in allowed for u in mandatory):
                failed.add(done)
                return False

            optional = [u for u in allowed if u not in mandatory_set]
            optional.sort(key=lambda u: (-rank[u], -outdeg[u], u))
            need = take - len(mandatory)
            if need < 0 or need > len(optional):
                failed.add(done)
                return False
            batches = (
                tuple(mandatory) + comb
                for comb in itertools.combinations(optional, need)
            )

        for batch in batches:
            new_done = done
            for u in batch:
                new_done |= 1 << u
            path.append(batch)
            if dfs(new_done, slots - 1):
                return True
            path.pop()

        failed.add(done)
        return False

    try:
        found = dfs(0, horizon)
    except Timeout:
        found = False

    if found:
        ans = [0] * n
        for cycle, batch in enumerate(path, 1):
            for u in batch:
                ans[u] = cycle
        print("YES")
        print(*ans)
    else:
        print("NO")

if __name__ == "__main__":
    sys.setrecursionlimit(1_000_000)
    main()