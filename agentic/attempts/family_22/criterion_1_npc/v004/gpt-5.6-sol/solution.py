import sys
import heapq
import itertools

sys.setrecursionlimit(1_000_000)


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if len(data) < 4:
        return

    n, M, T, m = data[:4]
    adj = [[] for _ in range(n)]
    radj = [[] for _ in range(n)]
    indeg = [0] * n

    p = 4
    for _ in range(m):
        a = data[p] - 1
        b = data[p + 1] - 1
        p += 2
        adj[a].append(b)
        radj[b].append(a)
        indeg[b] += 1

    if n == 0:
        print("YES")
        print()
        return

    if M <= 0 or T <= 0 or n > M * T:
        print("NO")
        return

    q = [i for i in range(n) if indeg[i] == 0]
    topo = []
    head = 0
    deg = indeg[:]

    while head < len(q):
        v = q[head]
        head += 1
        topo.append(v)
        for w in adj[v]:
            deg[w] -= 1
            if deg[w] == 0:
                q.append(w)

    if len(topo) != n:
        print("NO")
        return

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

    if T >= n:
        ans = [0] * n
        for i, v in enumerate(topo, 1):
            ans[v] = i
        print("YES")
        print(*ans)
        return

    def bottom_levels(graph, order):
        bottom = [1] * n
        for v in reversed(order):
            best = 0
            for w in graph[v]:
                if bottom[w] > best:
                    best = bottom[w]
            bottom[v] = best + 1
        return bottom

    bottom_orig = bottom_levels(adj, topo)
    if max(bottom_orig) > T:
        print("NO")
        return

    if M >= n:
        earliest = [1] * n
        for v in topo:
            ev = earliest[v] + 1
            for w in adj[v]:
                if earliest[w] < ev:
                    earliest[w] = ev
        print("YES")
        print(*earliest)
        return

    def greedy(graph, reverse_graph, order, mode):
        degree = [len(reverse_graph[v]) for v in range(n)]
        bottom = bottom_levels(graph, order)
        heap = []

        def key(v):
            if mode == 0:
                return (-bottom[v], -len(graph[v]), v)
            if mode == 1:
                return (-len(graph[v]), -bottom[v], v)
            return (-bottom[v], v)

        for v in range(n):
            if degree[v] == 0:
                heapq.heappush(heap, (key(v), v))

        slots = [0] * n
        time = 0
        score = 0
        completed = 0

        while heap:
            time += 1
            score += max(0, len(heap) - M)
            chosen = []
            for _ in range(min(M, len(heap))):
                _, v = heapq.heappop(heap)
                chosen.append(v)
                slots[v] = time
                completed += 1

            newly_ready = []
            for v in chosen:
                for w in graph[v]:
                    degree[w] -= 1
                    if degree[w] == 0:
                        newly_ready.append(w)
            for w in newly_ready:
                heapq.heappush(heap, (key(w), w))

        return slots, time, score, completed == n

    reverse_topo = list(reversed(topo))

    orientation_data = []
    for is_reversed, graph, reverse_graph, order in (
        (False, adj, radj, topo),
        (True, radj, adj, reverse_topo),
    ):
        best_score = None
        for mode in range(3):
            slots, length, score, complete = greedy(
                graph, reverse_graph, order, mode
            )
            if complete and length <= T:
                if is_reversed:
                    ans = [length + 1 - slots[v] for v in range(n)]
                else:
                    ans = slots
                print("YES")
                print(*ans)
                return
            if best_score is None or score < best_score:
                best_score = score
        orientation_data.append(
            (best_score, is_reversed, graph, reverse_graph, order)
        )

    orientation_data.sort(key=lambda x: x[0])
    _, is_reversed, graph, reverse_graph, order = orientation_data[0]

    bottom = bottom_levels(graph, order)
    if max(bottom) > T:
        print("NO")
        return

    predecessor_mask = [0] * n
    for v in range(n):
        mask = 0
        for u in reverse_graph[v]:
            mask |= 1 << u
        predecessor_mask[v] = mask

    latest = [T - bottom[v] + 1 for v in range(n)]
    all_mask = (1 << n) - 1
    failed = set()
    assigned = [0] * n

    def search(done, time):
        if done == all_mask:
            return True
        if time > T:
            return False

        state = (done, time)
        if state in failed:
            return False

        remaining_slots = T - time + 1
        remaining_count = n - done.bit_count()
        if remaining_count > M * remaining_slots:
            failed.add(state)
            return False

        rem = all_mask ^ done
        available = []
        forced = []
        deadline_counts = [0] * remaining_slots
        due_now_total = 0

        x = rem
        while x:
            bit = x & -x
            v = bit.bit_length() - 1
            x ^= bit

            d = latest[v]
            if d < time:
                failed.add(state)
                return False

            deadline_counts[d - time] += 1
            if d == time:
                due_now_total += 1

            if predecessor_mask[v] & done == predecessor_mask[v]:
                available.append(v)
                if d == time:
                    forced.append(v)

        if due_now_total != len(forced):
            failed.add(state)
            return False

        cumulative = 0
        for i, count in enumerate(deadline_counts):
            cumulative += count
            if cumulative > M * (i + 1):
                failed.add(state)
                return False

        if not available:
            failed.add(state)
            return False

        if len(forced) > M:
            failed.add(state)
            return False

        available.sort(
            key=lambda v: (latest[v], -len(graph[v]), -bottom[v], v)
        )

        if len(available) <= M:
            choices = (tuple(available),)
        else:
            forced_set = set(forced)
            candidates = [v for v in available if v not in forced_set]
            need = M - len(forced)
            choices = (
                tuple(forced) + extra
                for extra in itertools.combinations(candidates, need)
            )

        for choice in choices:
            chosen_mask = 0
            for v in choice:
                chosen_mask |= 1 << v
                assigned[v] = time

            if search(done | chosen_mask, time + 1):
                return True

            for v in choice:
                assigned[v] = 0

        failed.add(state)
        return False

    if not search(0, 1):
        print("NO")
        return

    if is_reversed:
        answer = [T + 1 - assigned[v] for v in range(n)]
    else:
        answer = assigned

    print("YES")
    print(*answer)


if __name__ == "__main__":
    main()