import sys
import itertools

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    it = iter(data)
    n = next(it)
    cap = next(it)
    T = next(it)
    edge_count = next(it)

    if n == 0:
        print("YES")
        print()
        return

    if cap <= 0 or T <= 0 or n > cap * T:
        print("NO")
        return

    graph = [[] for _ in range(n)]
    prereq = [0] * n
    indegree = [0] * n

    seen_edges = set()
    for _ in range(edge_count):
        a = next(it) - 1
        b = next(it) - 1
        key = a * n + b
        if key in seen_edges:
            continue
        seen_edges.add(key)
        graph[a].append(b)
        prereq[b] |= 1 << a
        indegree[b] += 1

    # Topological order and cycle detection.
    queue = [i for i in range(n) if indegree[i] == 0]
    topo = []
    head = 0
    while head < len(queue):
        u = queue[head]
        head += 1
        topo.append(u)
        for v in graph[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                queue.append(v)

    if len(topo) != n:
        print("NO")
        return

    # Longest path beginning at each vertex, including the vertex itself.
    height = [1] * n
    for u in reversed(topo):
        if graph[u]:
            height[u] = 1 + max(height[v] for v in graph[u])

    if max(height) > T:
        print("NO")
        return

    full_mask = (1 << n) - 1

    def available_vertices(mask):
        result = []
        remaining = full_mask ^ mask
        while remaining:
            bit = remaining & -remaining
            v = bit.bit_length() - 1
            if prereq[v] & ~mask == 0:
                result.append(v)
            remaining ^= bit
        return result

    # First try a longest-path-priority list schedule.
    mask = 0
    greedy_terms = []
    while mask != full_mask:
        avail = available_vertices(mask)
        if not avail:
            break
        avail.sort(key=lambda v: (height[v], len(graph[v])), reverse=True)
        chosen = avail[:cap]
        chosen_mask = 0
        for v in chosen:
            chosen_mask |= 1 << v
        greedy_terms.append(chosen_mask)
        mask |= chosen_mask

    if mask == full_mask and len(greedy_terms) <= T:
        answer = [0] * n
        for term, chosen_mask in enumerate(greedy_terms, 1):
            x = chosen_mask
            while x:
                bit = x & -x
                answer[bit.bit_length() - 1] = term
                x ^= bit
        print("YES")
        print(*answer)
        return

    sys.setrecursionlimit(max(1000000, n + 100))
    failed = {}
    path = []

    def dfs(mask, remaining_terms):
        if mask == full_mask:
            return True
        if remaining_terms == 0:
            return False

        old_failed = failed.get(mask)
        if old_failed is not None and old_failed >= remaining_terms:
            return False

        unscheduled_count = n - mask.bit_count()
        if unscheduled_count > remaining_terms * cap:
            failed[mask] = max(failed.get(mask, -1), remaining_terms)
            return False

        # Every remaining task has deadline remaining_terms-height[v]+1
        # relative to the current term. Check cumulative capacity by deadlines.
        deadline_count = [0] * (remaining_terms + 1)
        mandatory_mask = 0
        remaining_mask = full_mask ^ mask
        x = remaining_mask
        feasible = True

        while x:
            bit = x & -x
            v = bit.bit_length() - 1
            deadline = remaining_terms - height[v] + 1
            if deadline <= 0:
                feasible = False
                break
            deadline_count[deadline] += 1
            if deadline == 1:
                mandatory_mask |= bit
            x ^= bit

        if not feasible:
            failed[mask] = max(failed.get(mask, -1), remaining_terms)
            return False

        cumulative = 0
        saturated_deadline = 0
        for d in range(1, remaining_terms + 1):
            cumulative += deadline_count[d]
            if cumulative > d * cap:
                failed[mask] = max(failed.get(mask, -1), remaining_terms)
                return False
            if saturated_deadline == 0 and cumulative == d * cap:
                saturated_deadline = d

        avail = available_vertices(mask)
        if not avail:
            failed[mask] = max(failed.get(mask, -1), remaining_terms)
            return False

        avail_mask = 0
        for v in avail:
            avail_mask |= 1 << v

        if mandatory_mask & ~avail_mask:
            failed[mask] = max(failed.get(mask, -1), remaining_terms)
            return False

        take_count = min(cap, len(avail))

        # If the first d terms are saturated by tasks whose deadlines are at
        # most d, no other task may consume a slot in the current term.
        if saturated_deadline:
            allowed = [
                v for v in avail
                if remaining_terms - height[v] + 1 <= saturated_deadline
            ]
            if len(avail) < cap or len(allowed) < take_count:
                failed[mask] = max(failed.get(mask, -1), remaining_terms)
                return False
        else:
            allowed = avail

        mandatory = [v for v in allowed if mandatory_mask & (1 << v)]
        if len(mandatory) > take_count:
            failed[mask] = max(failed.get(mask, -1), remaining_terms)
            return False

        mandatory_set = set(mandatory)
        optional = [v for v in allowed if v not in mandatory_set]
        optional.sort(key=lambda v: (height[v], len(graph[v])), reverse=True)

        need = take_count - len(mandatory)
        if need > len(optional):
            failed[mask] = max(failed.get(mask, -1), remaining_terms)
            return False

        base_mask = 0
        for v in mandatory:
            base_mask |= 1 << v

        for combination in itertools.combinations(optional, need):
            chosen_mask = base_mask
            for v in combination:
                chosen_mask |= 1 << v

            path.append(chosen_mask)
            if dfs(mask | chosen_mask, remaining_terms - 1):
                return True
            path.pop()

        failed[mask] = max(failed.get(mask, -1), remaining_terms)
        return False

    if not dfs(0, T):
        print("NO")
        return

    answer = [0] * n
    for term, chosen_mask in enumerate(path, 1):
        x = chosen_mask
        while x:
            bit = x & -x
            answer[bit.bit_length() - 1] = term
            x ^= bit

    print("YES")
    print(*answer)

if __name__ == "__main__":
    main()