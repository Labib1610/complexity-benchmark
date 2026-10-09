import sys
import heapq
import itertools
import random

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
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
    p = 4
    for _ in range(m):
        a = data[p] - 1
        b = data[p + 1] - 1
        p += 2
        if 0 <= a < n and 0 <= b < n:
            succ_sets[a].add(b)

    succ = [list(s) for s in succ_sets]
    indeg = [0] * n
    pre = [0] * n
    for u in range(n):
        for v in succ[u]:
            indeg[v] += 1
            pre[v] |= 1 << u

    heap = [i for i in range(n) if indeg[i] == 0]
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

    bottom = [1] * n
    for u in reversed(topo):
        if succ[u]:
            bottom[u] = 1 + max(bottom[v] for v in succ[u])

    if max(bottom) > T:
        print("NO")
        return

    top_depth = [1] * n
    for u in topo:
        du = top_depth[u] + 1
        for v in succ[u]:
            if top_depth[v] < du:
                top_depth[v] = du

    predecessors = [[] for _ in range(n)]
    for u in range(n):
        for v in succ[u]:
            predecessors[v].append(u)

    def forward_schedule(mode, rank):
        d = indeg[:]
        h = []

        def key(v):
            if mode == 0:
                return (-bottom[v], -len(succ[v]), rank[v], v)
            if mode == 1:
                return (-bottom[v], -top_depth[v], rank[v], v)
            if mode == 2:
                return (-len(succ[v]), -bottom[v], rank[v], v)
            return (-top_depth[v], -bottom[v], rank[v], v)

        for v in range(n):
            if d[v] == 0:
                heapq.heappush(h, (key(v), v))

        ans = [0] * n
        shift = 0
        done = 0
        while h:
            shift += 1
            batch = []
            for _ in range(min(M, len(h))):
                batch.append(heapq.heappop(h)[1])
            for u in batch:
                ans[u] = shift
                done += 1
            for u in batch:
                for v in succ[u]:
                    d[v] -= 1
                    if d[v] == 0:
                        heapq.heappush(h, (key(v), v))
        return ans if done == n and shift <= T else None

    def backward_schedule(mode, rank):
        outdeg = [len(succ[u]) for u in range(n)]
        h = []

        def key(v):
            if mode == 0:
                return (-top_depth[v], -len(predecessors[v]), rank[v], v)
            if mode == 1:
                return (-top_depth[v], -bottom[v], rank[v], v)
            return (-len(predecessors[v]), -top_depth[v], rank[v], v)

        for v in range(n):
            if outdeg[v] == 0:
                heapq.heappush(h, (key(v), v))

        reverse_level = [0] * n
        level = 0
        done = 0
        while h:
            level += 1
            batch = []
            for _ in range(min(M, len(h))):
                batch.append(heapq.heappop(h)[1])
            for u in batch:
                reverse_level[u] = level
                done += 1
            for u in batch:
                for v in predecessors[u]:
                    outdeg[v] -= 1
                    if outdeg[v] == 0:
                        heapq.heappush(h, (key(v), v))

        if done != n or level > T:
            return None
        return [level - reverse_level[v] + 1 for v in range(n)]

    identity = list(range(n))
    for mode in range(4):
        result = forward_schedule(mode, identity)
        if result is not None:
            print("YES")
            print(*result)
            return

    for mode in range(3):
        result = backward_schedule(mode, identity)
        if result is not None:
            print("YES")
            print(*result)
            return

    rng = random.Random(712367821)
    attempts = 12 if n <= 5000 else 4
    for _ in range(attempts):
        rank = list(range(n))
        rng.shuffle(rank)
        inv_rank = [0] * n
        for i, v in enumerate(rank):
            inv_rank[v] = i
        for mode in (0, 1, 2):
            result = forward_schedule(mode, inv_rank)
            if result is not None:
                print("YES")
                print(*result)
                return
        result = backward_schedule(0, inv_rank)
        if result is not None:
            print("YES")
            print(*result)
            return

    # Exact exponential search. The underlying general scheduling problem is
    # NP-hard, so this is used after fast list-scheduling attempts fail.
    T_eff = min(T, n)
    all_mask = (1 << n) - 1
    answer = [0] * n
    failed = set()

    order_score = sorted(
        range(n),
        key=lambda v: (-bottom[v], -len(succ[v]), -top_depth[v], v)
    )

    sys.setrecursionlimit(max(1000000, T_eff * 4 + 100))

    def dfs(done, shift):
        if done == all_mask:
            return True
        if shift > T_eff:
            return False

        state = (done, shift)
        if state in failed:
            return False

        remaining_mask = all_mask ^ done
        remaining_count = remaining_mask.bit_count()
        shifts_left = T_eff - shift + 1
        if remaining_count > M * shifts_left:
            failed.add(state)
            return False

        available = []
        critical = []
        for v in order_score:
            bit = 1 << v
            if not (remaining_mask & bit):
                continue
            b = bottom[v]
            if b > shifts_left:
                failed.add(state)
                return False
            is_available = (pre[v] & done) == pre[v]
            if b == shifts_left:
                if not is_available:
                    failed.add(state)
                    return False
                critical.append(v)
            if is_available:
                available.append(v)

        if not available or len(critical) > M:
            failed.add(state)
            return False

        take = min(M, len(available))
        critical_set = set(critical)
        optional = [v for v in available if v not in critical_set]
        need = take - len(critical)

        if need < 0 or need > len(optional):
            failed.add(state)
            return False

        critical_mask = 0
        for v in critical:
            critical_mask |= 1 << v

        if need == 0:
            choices = [()]
        elif need == len(optional):
            choices = [tuple(optional)]
        else:
            choices = itertools.combinations(optional, need)

        for combo in choices:
            selected_mask = critical_mask
            selected = list(critical)
            for v in combo:
                selected_mask |= 1 << v
                selected.append(v)

            for v in selected:
                answer[v] = shift

            if dfs(done | selected_mask, shift + 1):
                return True

        failed.add(state)
        return False

    if dfs(0, 1):
        print("YES")
        print(*answer)
    else:
        print("NO")

if __name__ == "__main__":
    main()