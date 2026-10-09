import sys
import heapq

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

    if n == 0:
        print("YES")
        print()
        return

    if M <= 0 or T <= 0 or n > M * T:
        print("NO")
        return

    succ_sets = [set() for _ in range(n)]
    pred_sets = [set() for _ in range(n)]

    for _ in range(m):
        a = next(it) - 1
        b = next(it) - 1
        if b not in succ_sets[a]:
            succ_sets[a].add(b)
            pred_sets[b].add(a)

    succ = [list(x) for x in succ_sets]
    pred = [list(x) for x in pred_sets]
    indeg = [len(x) for x in pred]
    outdeg = [len(x) for x in succ]

    # Topological order and cycle detection.
    q = [i for i in range(n) if indeg[i] == 0]
    topo = []
    head = 0
    tmp_indeg = indeg[:]
    while head < len(q):
        v = q[head]
        head += 1
        topo.append(v)
        for w in succ[v]:
            tmp_indeg[w] -= 1
            if tmp_indeg[w] == 0:
                q.append(w)

    if len(topo) != n:
        print("NO")
        return

    # Longest path lengths from a source and to a sink, measured in vertices.
    top = [1] * n
    for v in topo:
        nv = top[v] + 1
        for w in succ[v]:
            if top[w] < nv:
                top[w] = nv

    bottom = [1] * n
    for v in reversed(topo):
        best = 1
        for w in succ[v]:
            val = bottom[w] + 1
            if val > best:
                best = val
        bottom[v] = best

    if max(bottom) > T:
        print("NO")
        return

    latest = [T - bottom[v] + 1 for v in range(n)]

    def forward_schedule(mode):
        deg = indeg[:]
        heap = []

        def key(v):
            if mode == 0:
                return (-bottom[v], -outdeg[v], v)
            if mode == 1:
                return (-outdeg[v], -bottom[v], v)
            if mode == 2:
                return (-bottom[v], top[v], v)
            return (-top[v], -bottom[v], v)

        for v in range(n):
            if deg[v] == 0:
                heapq.heappush(heap, key(v))

        ans = [0] * n
        done_count = 0
        cycle = 1

        while heap:
            batch = []
            for _ in range(min(M, len(heap))):
                item = heapq.heappop(heap)
                v = item[-1]
                batch.append(v)

            for v in batch:
                ans[v] = cycle
                done_count += 1

            for v in batch:
                for w in succ[v]:
                    deg[w] -= 1
                    if deg[w] == 0:
                        heapq.heappush(heap, key(w))

            cycle += 1

        if done_count == n and cycle - 1 <= T:
            return ans
        return None

    def backward_schedule():
        deg = outdeg[:]
        heap = []
        for v in range(n):
            if deg[v] == 0:
                heapq.heappush(heap, (-top[v], -len(pred[v]), v))

        ans = [0] * n
        cycle = T
        done_count = 0

        while heap:
            if cycle < 1:
                return None

            batch = []
            for _ in range(min(M, len(heap))):
                _, _, v = heapq.heappop(heap)
                batch.append(v)

            for v in batch:
                ans[v] = cycle
                done_count += 1

            for v in batch:
                for p in pred[v]:
                    deg[p] -= 1
                    if deg[p] == 0:
                        heapq.heappush(heap, (-top[p], -len(pred[p]), p))

            cycle -= 1

        return ans if done_count == n else None

    modes = 4 if n + m <= 500_000 else 2
    for mode in range(modes):
        answer = forward_schedule(mode)
        if answer is not None:
            print("YES")
            print(*answer)
            return

    answer = backward_schedule()
    if answer is not None:
        print("YES")
        print(*answer)
        return

    # Exact search. It is only reached when the polynomial-time list schedules
    # did not find a feasible assignment.
    pred_mask = [0] * n
    succ_mask = [0] * n
    for v in range(n):
        pm = 0
        for p in pred[v]:
            pm |= 1 << p
        pred_mask[v] = pm

        sm = 0
        for w in succ[v]:
            sm |= 1 << w
        succ_mask[v] = sm

    all_mask = (1 << n) - 1
    batches = []
    solution_batches = None
    best_time = {}

    def dfs(done, cycle):
        nonlocal solution_batches

        if done == all_mask:
            solution_batches = batches[:]
            return True
        if cycle > T:
            return False

        old = best_time.get(done)
        if old is not None and old <= cycle:
            return False
        best_time[done] = cycle

        remaining_count = n - done.bit_count()
        if remaining_count > M * (T - cycle + 1):
            return False

        available = []
        deadlines = []
        urgent_mask = 0
        urgent_count = 0

        remaining = all_mask ^ done
        x = remaining
        while x:
            bit = x & -x
            v = bit.bit_length() - 1
            x -= bit

            d = latest[v]
            if d < cycle:
                return False
            deadlines.append(d)

            if pred_mask[v] & remaining == 0:
                available.append(v)
                if d == cycle:
                    urgent_mask |= bit
                    urgent_count += 1
            elif d == cycle:
                return False

        if not available or urgent_count > M:
            return False

        deadlines.sort()
        for i, d in enumerate(deadlines, 1):
            if i > M * (d - cycle + 1):
                return False

        if len(available) <= M:
            chosen = 0
            batch = []
            for v in available:
                chosen |= 1 << v
                batch.append(v)
            batches.append(batch)
            if dfs(done | chosen, cycle + 1):
                return True
            batches.pop()
            return False

        need = M - urgent_count
        optional_groups = {}

        for v in available:
            bit = 1 << v
            if urgent_mask & bit:
                continue
            optional_groups.setdefault(succ_mask[v], []).append(v)

        groups = []
        for vertices in optional_groups.values():
            vertices.sort()
            vertices.sort(key=lambda v: (-bottom[v], -outdeg[v], v))
            groups.append(vertices)

        groups.sort(
            key=lambda g: (-bottom[g[0]], -outdeg[g[0]], g[0])
        )

        suffix_sizes = [0] * (len(groups) + 1)
        for i in range(len(groups) - 1, -1, -1):
            suffix_sizes[i] = suffix_sizes[i + 1] + len(groups[i])

        urgent_vertices = []
        x = urgent_mask
        while x:
            bit = x & -x
            urgent_vertices.append(bit.bit_length() - 1)
            x -= bit

        def choose_groups(index, left, chosen_mask, chosen_vertices):
            if left == 0:
                batch = urgent_vertices + chosen_vertices
                batches.append(batch)
                if dfs(done | urgent_mask | chosen_mask, cycle + 1):
                    return True
                batches.pop()
                return False

            if index == len(groups) or suffix_sizes[index] < left:
                return False

            group = groups[index]
            low = max(0, left - suffix_sizes[index + 1])
            high = min(len(group), left)

            # Try taking more jobs from higher-priority groups first.
            mask_prefix = 0
            prefix_masks = [0]
            for v in group:
                mask_prefix |= 1 << v
                prefix_masks.append(mask_prefix)

            for take in range(high, low - 1, -1):
                if choose_groups(
                    index + 1,
                    left - take,
                    chosen_mask | prefix_masks[take],
                    chosen_vertices + group[:take]
                ):
                    return True
            return False

        return choose_groups(0, need, 0, [])

    if dfs(0, 1):
        ans = [0] * n
        for cycle, batch in enumerate(solution_batches, 1):
            for v in batch:
                ans[v] = cycle
        print("YES")
        print(*ans)
    else:
        print("NO")

if __name__ == "__main__":
    main()