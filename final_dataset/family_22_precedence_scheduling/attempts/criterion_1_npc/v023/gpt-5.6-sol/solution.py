import sys
import heapq
import itertools

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

    adj = [[] for _ in range(n)]
    radj = [[] for _ in range(n)]
    indeg = [0] * n
    outdeg = [0] * n
    pred_mask = [0] * n

    pos = 4
    for _ in range(m):
        a = data[pos] - 1
        b = data[pos + 1] - 1
        pos += 2
        adj[a].append(b)
        radj[b].append(a)
        indeg[b] += 1
        outdeg[a] += 1
        pred_mask[b] |= 1 << a

    # Topological sorting and cycle detection.
    q = [i for i in range(n) if indeg[i] == 0]
    heapq.heapify(q)
    topo = []
    deg = indeg[:]

    while q:
        u = heapq.heappop(q)
        topo.append(u)
        for v in adj[u]:
            deg[v] -= 1
            if deg[v] == 0:
                heapq.heappush(q, v)

    if len(topo) != n:
        print("NO")
        return

    # With at least n phases, any topological ordering works.
    if T >= n:
        ans = [0] * n
        for phase, u in enumerate(topo, 1):
            ans[u] = phase
        print("YES")
        print(*ans)
        return

    head = [1] * n
    for u in topo:
        hu = head[u] + 1
        for v in adj[u]:
            if hu > head[v]:
                head[v] = hu

    tail = [1] * n
    for u in reversed(topo):
        best = 1
        for v in adj[u]:
            cand = tail[v] + 1
            if cand > best:
                best = cand
        tail[u] = best

    if max(head) > T:
        print("NO")
        return

    # Necessary deadline and release-time density conditions.
    tails_sorted = sorted(tail, reverse=True)
    for j, value in enumerate(tails_sorted, 1):
        if j > M * (T - value + 1):
            print("NO")
            return

    heads_sorted = sorted(head, reverse=True)
    for j, value in enumerate(heads_sorted, 1):
        if j > M * (T - value + 1):
            print("NO")
            return

    if M >= n:
        print("YES")
        print(*head)
        return

    def random_value(i, seed):
        x = (i + 1) ^ (seed * 0x9E3779B9)
        x = (x ^ (x >> 16)) * 0x85EBCA6B
        x = (x ^ (x >> 13)) * 0xC2B2AE35
        return (x ^ (x >> 16)) & 0xFFFFFFFF

    def forward_greedy(mode, seed=0):
        d = indeg[:]
        heap = []

        def key(i):
            r = random_value(i, seed)
            if mode == 0:
                return (-tail[i], -outdeg[i], i)
            if mode == 1:
                return (-outdeg[i], -tail[i], i)
            if mode == 2:
                return (-tail[i], -r, i)
            return (-r, -tail[i], i)

        for i in range(n):
            if d[i] == 0:
                heapq.heappush(heap, (key(i), i))

        ans = [0] * n
        done = 0
        phase = 1

        while heap and done < n and phase <= T:
            selected = []
            for _ in range(min(M, len(heap))):
                _, u = heapq.heappop(heap)
                selected.append(u)
                ans[u] = phase
                done += 1

            for u in selected:
                for v in adj[u]:
                    d[v] -= 1
                    if d[v] == 0:
                        heapq.heappush(heap, (key(v), v))
            phase += 1

        return ans if done == n else None

    def backward_greedy(mode, seed=0):
        d = outdeg[:]
        heap = []

        def key(i):
            r = random_value(i, seed)
            if mode == 0:
                return (-head[i], -indeg[i], i)
            if mode == 1:
                return (-indeg[i], -head[i], i)
            if mode == 2:
                return (-head[i], -r, i)
            return (-r, -head[i], i)

        for i in range(n):
            if d[i] == 0:
                heapq.heappush(heap, (key(i), i))

        ans = [0] * n
        done = 0
        phase = T

        while heap and done < n and phase >= 1:
            selected = []
            for _ in range(min(M, len(heap))):
                _, u = heapq.heappop(heap)
                selected.append(u)
                ans[u] = phase
                done += 1

            for u in selected:
                for v in radj[u]:
                    d[v] -= 1
                    if d[v] == 0:
                        heapq.heappush(heap, (key(v), v))
            phase -= 1

        return ans if done == n else None

    attempts = [(0, 0), (1, 0)]
    random_attempts = 8 if n <= 20000 else 3
    for seed in range(1, random_attempts + 1):
        attempts.append((2, seed))
        attempts.append((3, seed))

    for mode, seed in attempts:
        ans = forward_greedy(mode, seed)
        if ans is not None:
            print("YES")
            print(*ans)
            return

        ans = backward_greedy(mode, seed)
        if ans is not None:
            print("YES")
            print(*ans)
            return

    # Exact branch-and-bound search by phases.
    sys.setrecursionlimit(max(10000, T + 100))
    all_mask = (1 << n) - 1
    tail_order = sorted(range(n), key=lambda x: (-tail[x], -outdeg[x], x))
    answer = [0] * n
    failed = set()

    def dfs(mask, phase):
        if mask == all_mask:
            return True
        if phase > T:
            return False

        state = (mask, phase)
        if state in failed:
            return False

        remaining_count = n - mask.bit_count()
        R = T - phase + 1
        if remaining_count > M * R:
            failed.add(state)
            return False

        # All remaining tasks have deadlines determined by their longest
        # successor chains. Check cumulative deadline capacities.
        cnt = 0
        for u in tail_order:
            if not ((mask >> u) & 1):
                value = tail[u]
                if value > R:
                    failed.add(state)
                    return False
                cnt += 1
                if cnt > M * (R - value + 1):
                    failed.add(state)
                    return False

        available = []
        rem = all_mask ^ mask
        bits = rem
        while bits:
            lsb = bits & -bits
            u = lsb.bit_length() - 1
            bits -= lsb
            if pred_mask[u] & ~mask == 0:
                available.append(u)

        if not available:
            failed.add(state)
            return False

        forced = [u for u in available if tail[u] == R]
        if len(forced) > M:
            failed.add(state)
            return False

        if len(available) <= M:
            selected = available
            new_mask = mask
            for u in selected:
                new_mask |= 1 << u
                answer[u] = phase

            if dfs(new_mask, phase + 1):
                return True

            for u in selected:
                answer[u] = 0
            failed.add(state)
            return False

        forced_set = set(forced)
        optional = [u for u in available if u not in forced_set]
        optional.sort(key=lambda u: (-tail[u], -outdeg[u], u))
        need = M - len(forced)

        for extra in itertools.combinations(optional, need):
            selected = forced + list(extra)
            new_mask = mask
            for u in selected:
                new_mask |= 1 << u
                answer[u] = phase

            if dfs(new_mask, phase + 1):
                return True

            for u in selected:
                answer[u] = 0

        failed.add(state)
        if len(failed) > 800000:
            failed.clear()
            failed.add(state)
        return False

    if dfs(0, 1):
        print("YES")
        print(*answer)
    else:
        print("NO")

if __name__ == "__main__":
    main()