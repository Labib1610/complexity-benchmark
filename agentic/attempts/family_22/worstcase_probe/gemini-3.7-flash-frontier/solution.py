import sys
from collections import deque
import itertools

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    iterator = iter(input_data)
    n = int(next(iterator))
    M = int(next(iterator))
    T = int(next(iterator))
    m = int(next(iterator))

    if n > M * T:
        print("NO")
        return

    adj = [[] for _ in range(n + 1)]
    rev_adj = [[] for _ in range(n + 1)]
    in_deg = [0] * (n + 1)
    out_deg = [0] * (n + 1)

    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        adj[u].append(v)
        rev_adj[v].append(u)
        in_deg[v] += 1
        out_deg[u] += 1

    # Topological sort & cycle check
    q = deque([i for i in range(1, n + 1) if in_deg[i] == 0])
    topo_order = []
    temp_in = list(in_deg)
    while q:
        u = q.popleft()
        topo_order.append(u)
        for v in adj[u]:
            temp_in[v] -= 1
            if temp_in[v] == 0:
                q.append(v)

    if len(topo_order) < n:
        print("NO")
        return

    # Earliest (E) and Latest (L) slot calculations
    E = [1] * (n + 1)
    for u in topo_order:
        for v in adj[u]:
            if E[u] + 1 > E[v]:
                E[v] = E[u] + 1

    L = [T] * (n + 1)
    for u in reversed(topo_order):
        for v in rev_adj[u]:
            if L[u] - 1 < L[v]:
                L[v] = L[u] - 1

    for i in range(1, n + 1):
        if E[i] > L[i]:
            print("NO")
            return

    # Interval capacity check
    for t1 in range(1, T + 1):
        for t2 in range(t1, T + 1):
            count = sum(1 for i in range(1, n + 1) if t1 <= E[i] and L[i] <= t2)
            if count > M * (t2 - t1 + 1):
                print("NO")
                return

    # If M >= n, ASAP assignment is always valid
    if M >= n:
        print("YES")
        print(*(E[1:]))
        return

    # Descendant depths for heuristic
    depth = [0] * (n + 1)
    for u in reversed(topo_order):
        d = 0
        for v in adj[u]:
            if depth[v] + 1 > d:
                d = depth[v] + 1
        depth[u] = d

    # Backtracking search
    job_slot = [0] * (n + 1)
    current_in_deg = list(in_deg)
    memo = set()

    def search(slot, scheduled_mask, num_scheduled):
        if num_scheduled == n:
            return True
        if slot > T:
            return False

        state = (slot, scheduled_mask)
        if state in memo:
            return False
        memo.add(state)

        # Check if any unscheduled job has L[u] < slot
        must_schedule = []
        available = []

        for u in range(1, n + 1):
            if not ((scheduled_mask >> u) & 1):
                if L[u] < slot:
                    return False
                if current_in_deg[u] == 0:
                    if L[u] == slot:
                        must_schedule.append(u)
                    else:
                        available.append(u)

        if len(must_schedule) > M:
            return False

        needed = M - len(must_schedule)
        available.sort(key=lambda u: (L[u], -depth[u], u))

        # Form candidate sets
        if len(available) <= needed:
            combos = [tuple(available)]
        else:
            combos = list(itertools.combinations(available, needed))

        for combo in combos:
            chosen = must_schedule + list(combo)
            new_mask = scheduled_mask
            for u in chosen:
                job_slot[u] = slot
                new_mask |= (1 << u)
                for v in adj[u]:
                    current_in_deg[v] -= 1

            if search(slot + 1, new_mask, num_scheduled + len(chosen)):
                return True

            for u in chosen:
                job_slot[u] = 0
                for v in adj[u]:
                    current_in_deg[v] += 1

        return False

    if search(1, 0, 0):
        print("YES")
        print(*(job_slot[1:]))
    else:
        print("NO")

if __name__ == '__main__':
    solve()