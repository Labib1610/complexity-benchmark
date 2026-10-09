import sys
from collections import deque
from itertools import combinations


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    it = iter(input_data)
    n = int(next(it))
    M = int(next(it))
    T = int(next(it))
    m = int(next(it))

    if n > M * T:
        print("NO")
        return

    adj = [[] for _ in range(n + 1)]
    rev_adj = [[] for _ in range(n + 1)]
    in_degree = [0] * (n + 1)

    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u].append(v)
        rev_adj[v].append(u)
        in_degree[v] += 1

    # Cycle check and topological order
    q = deque([i for i in range(1, n + 1) if in_degree[i] == 0])
    topo = []
    while q:
        u = q.popleft()
        topo.append(u)
        for v in adj[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                q.append(v)

    if len(topo) < n:
        print("NO")
        return

    # Compute Earliest Start (ES) and Latest Start (LS)
    ES = [1] * (n + 1)
    for u in topo:
        for v in adj[u]:
            if ES[u] + 1 > ES[v]:
                ES[v] = ES[u] + 1

    LS = [T] * (n + 1)
    for u in reversed(topo):
        for v in adj[u]:
            if LS[v] - 1 < LS[u]:
                LS[u] = LS[v] - 1

    for i in range(1, n + 1):
        if ES[i] > LS[i] or LS[i] < 1 or ES[i] > T:
            print("NO")
            return

    # Height / depth in DAG for heuristic ordering
    height = [0] * (n + 1)
    for u in reversed(topo):
        h = 0
        for v in adj[u]:
            if height[v] + 1 > h:
                h = height[v] + 1
        height[u] = h

    # Reconstruct initial in-degrees
    cur_in_degree = [0] * (n + 1)
    for u in range(1, n + 1):
        for v in adj[u]:
            cur_in_degree[v] += 1

    assignment = [0] * (n + 1)
    scheduled_count = 0

    # Backtracking search hour by hour
    # Since any non-delay schedule is dominant, we always schedule jobs if capacity allows.
    def search(t, available):
        nonlocal scheduled_count
        if scheduled_count == n:
            return True
        if t > T:
            return False

        # Must schedule jobs that have LS[u] == t
        must = []
        optional = []
        for u in available:
            if LS[u] < t:
                return False
            elif LS[u] == t:
                must.append(u)
            else:
                optional.append(u)

        if len(must) > M:
            return False

        needed = len(must) + len(optional)
        if needed <= M:
            choices = [must + optional]
        else:
            # Sort optional by LS ascending, then height descending
            optional.sort(key=lambda x: (LS[x], -height[x]))
            rem_slots = M - len(must)

            # Heuristic: try best subset first, with fallback combinations if small
            # In most cases, taking the top rem_slots is optimal
            # Limit the branching to avoid TLE
            pool = optional[: min(len(optional), rem_slots + 4)]
            combos = list(combinations(pool, rem_slots))
            choices = [[*must, *c] for c in combos]

        for chosen in choices:
            chosen_set = set(chosen)
            next_available = [u for u in available if u not in chosen_set]

            for u in chosen:
                assignment[u] = t
                for v in adj[u]:
                    cur_in_degree[v] -= 1
                    if cur_in_degree[v] == 0:
                        next_available.append(v)

            scheduled_count += len(chosen)

            if search(t + 1, next_available):
                return True

            scheduled_count -= len(chosen)
            for u in chosen:
                assignment[u] = 0
                for v in adj[u]:
                    cur_in_degree[v] += 1

        return False

    initial_available = [i for i in range(1, n + 1) if cur_in_degree[i] == 0]
    if search(1, initial_available):
        print("YES")
        print(*(assignment[i] for i in range(1, n + 1)))
    else:
        print("NO")


if __name__ == "__main__":
    solve()