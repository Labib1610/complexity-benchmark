import sys
import heapq
import itertools
import time

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
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

    heap = [i for i in range(n) if indeg[i] == 0]
    heapq.heapify(heap)
    topo = []
    deg = indeg[:]
    while heap:
        u = heapq.heappop(heap)
        topo.append(u)
        for v in adj[u]:
            deg[v] -= 1
            if deg[v] == 0:
                heapq.heappush(heap, v)

    if len(topo) != n:
        print("NO")
        return

    bottom = [1] * n
    for u in reversed(topo):
        if adj[u]:
            bottom[u] = 1 + max(bottom[v] for v in adj[u])

    if max(bottom) > T:
        print("NO")
        return

    if M == 1:
        if n > T:
            print("NO")
            return
        answer = [0] * n
        for i, u in enumerate(topo, 1):
            answer[u] = i
        print("YES")
        print(*answer)
        return

    if T >= n:
        answer = [0] * n
        for i, u in enumerate(topo, 1):
            answer[u] = i
        print("YES")
        print(*answer)
        return

    reach_count = [0] * n
    if n <= 1800:
        reach = [0] * n
        for u in reversed(topo):
            mask = 0
            for v in adj[u]:
                mask |= reach[v] | (1 << v)
            reach[u] = mask
            reach_count[u] = mask.bit_count()
    else:
        reach_count = [len(adj[u]) for u in range(n)]

    def greedy_schedule(g, initial_indeg, btm, secondary, mode):
        d = initial_indeg[:]
        ready = []

        def key(u):
            if mode == 0:
                return (-btm[u], -secondary[u], -len(g[u]), u)
            if mode == 1:
                return (-secondary[u], -btm[u], -len(g[u]), u)
            if mode == 2:
                return (-btm[u], -len(g[u]), -secondary[u], -u)
            if mode == 3:
                h = (u * 11995408973635179863 + 10150724397891781847) & ((1 << 64) - 1)
                return (-btm[u], h, u)
            h = (u * 6364136223846793005 + 1442695040888963407) & ((1 << 64) - 1)
            return (-secondary[u], h, u)

        for u in range(n):
            if d[u] == 0:
                heapq.heappush(ready, key(u))

        assignment = [0] * n
        room = 0
        done = 0

        while ready:
            room += 1
            if room > T:
                return None
            batch = []
            for _ in range(min(M, len(ready))):
                item = heapq.heappop(ready)
                u = item[-1]
                batch.append(u)
                assignment[u] = room
            done += len(batch)
            for u in batch:
                for v in g[u]:
                    d[v] -= 1
                    if d[v] == 0:
                        heapq.heappush(ready, key(v))

        return assignment if done == n else None

    for mode in range(5):
        ans = greedy_schedule(adj, indeg, bottom, reach_count, mode)
        if ans is not None:
            print("YES")
            print(*ans)
            return

    rindeg = [len(adj[u]) for u in range(n)]
    rtopo = list(reversed(topo))
    rbottom = [1] * n
    for u in reversed(rtopo):
        if radj[u]:
            rbottom[u] = 1 + max(rbottom[v] for v in radj[u])

    rreach_count = [0] * n
    if n <= 1800:
        rreach = [0] * n
        for u in reversed(rtopo):
            mask = 0
            for v in radj[u]:
                mask |= rreach[v] | (1 << v)
            rreach[u] = mask
            rreach_count[u] = mask.bit_count()
    else:
        rreach_count = [len(radj[u]) for u in range(n)]

    for mode in range(5):
        rev_ans = greedy_schedule(radj, rindeg, rbottom, rreach_count, mode)
        if rev_ans is not None:
            used = max(rev_ans)
            ans = [used - rev_ans[u] + 1 for u in range(n)]
            print("YES")
            print(*ans)
            return

    start_time = time.monotonic()
    deadline_time = start_time + 4.65
    timed_out = False

    def exact_schedule(graph, predecessors, btm, secondary):
        nonlocal timed_out
        if n > 62:
            return None

        pred_mask = [0] * n
        for u in range(n):
            mask = 0
            for v in predecessors[u]:
                mask |= 1 << v
            pred_mask[u] = mask

        all_mask = (1 << n) - 1
        failed = set()
        path = []

        def dfs(state, used):
            nonlocal timed_out
            if time.monotonic() > deadline_time:
                timed_out = True
                return False
            if state == all_mask:
                return True

            key_state = (state, used)
            if key_state in failed:
                return False

            slots = T - used
            remaining_count = n - state.bit_count()
            if slots <= 0 or remaining_count > slots * M:
                failed.add(key_state)
                return False

            remaining = []
            available = []
            inv = all_mask ^ state
            x = inv
            while x:
                bit = x & -x
                u = bit.bit_length() - 1
                remaining.append(u)
                if pred_mask[u] & inv == 0:
                    available.append(u)
                x -= bit

            if not available:
                failed.add(key_state)
                return False

            ordered_bottom = sorted((btm[u] for u in remaining), reverse=True)
            for j, value in enumerate(ordered_bottom, 1):
                latest = slots - value + 1
                if latest <= 0 or j > M * latest:
                    failed.add(key_state)
                    return False

            mandatory = [u for u in available if btm[u] == slots]
            if len(mandatory) > M:
                failed.add(key_state)
                return False

            available.sort(key=lambda u: (-btm[u], -secondary[u], -len(graph[u]), u))

            if len(available) <= M:
                choices = [tuple(available)]
            else:
                mandatory_set = set(mandatory)
                optional = [u for u in available if u not in mandatory_set]
                take = M - len(mandatory)
                if take < 0 or take > len(optional):
                    failed.add(key_state)
                    return False
                choices = (
                    tuple(mandatory) + comb
                    for comb in itertools.combinations(optional, take)
                )

            for batch in choices:
                new_state = state
                for u in batch:
                    new_state |= 1 << u
                path.append(batch)
                if dfs(new_state, used + 1):
                    return True
                path.pop()
                if timed_out:
                    return False

            failed.add(key_state)
            return False

        if dfs(0, 0):
            assignment = [0] * n
            for room, batch in enumerate(path, 1):
                for u in batch:
                    assignment[u] = room
            return assignment
        return None

    orientations = [
        (adj, radj, bottom, reach_count, False),
        (radj, adj, rbottom, rreach_count, True),
    ]
    orientations.sort(key=lambda x: sum(1 for u in range(n) if not x[1][u]))

    for graph, predecessors, btm, secondary, reverse_result in orientations:
        ans = exact_schedule(graph, predecessors, btm, secondary)
        if ans is not None:
            if reverse_result:
                used = max(ans)
                ans = [used - ans[u] + 1 for u in range(n)]
            print("YES")
            print(*ans)
            return
        if timed_out:
            break

    print("NO")

if __name__ == "__main__":
    main()