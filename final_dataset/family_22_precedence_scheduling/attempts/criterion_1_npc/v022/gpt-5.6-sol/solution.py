import sys
import heapq
import itertools

sys.setrecursionlimit(1_000_000)

def topological_data(n, graph, indegree):
    deg = indegree[:]
    heap = [i for i in range(n) if deg[i] == 0]
    heapq.heapify(heap)
    order = []

    while heap:
        u = heapq.heappop(heap)
        order.append(u)
        for v in graph[u]:
            deg[v] -= 1
            if deg[v] == 0:
                heapq.heappush(heap, v)

    if len(order) != n:
        return None, None

    depth = [1] * n
    for u in reversed(order):
        if graph[u]:
            depth[u] = 1 + max(depth[v] for v in graph[u])

    return order, depth


def greedy_schedule(n, M, T, graph, indegree, depth, mode):
    deg = indegree[:]

    def priority(u):
        if mode == 0:
            return (-depth[u], -len(graph[u]), u)
        if mode == 1:
            return (-depth[u], len(graph[u]), u)
        if mode == 2:
            return (-depth[u], -len(graph[u]), -u)
        if mode == 3:
            return (-len(graph[u]), -depth[u], u)
        if mode == 4:
            return (-depth[u], u)
        return (-depth[u], -sum(depth[v] for v in graph[u]), u)

    available = []
    for u in range(n):
        if deg[u] == 0:
            heapq.heappush(available, (priority(u), u))

    assignment = [0] * n
    shipped = 0
    day = 1

    while shipped < n and day <= T:
        batch = []
        for _ in range(min(M, len(available))):
            _, u = heapq.heappop(available)
            batch.append(u)

        if not batch:
            return None

        newly_available = []
        for u in batch:
            assignment[u] = day
            shipped += 1
            for v in graph[u]:
                deg[v] -= 1
                if deg[v] == 0:
                    newly_available.append(v)

        for v in newly_available:
            heapq.heappush(available, (priority(v), v))

        day += 1

    return assignment if shipped == n else None


def exact_schedule(n, M, T, graph, predecessors, depth):
    all_done = (1 << n) - 1
    failed = set()
    batches = []

    out_degree = [len(graph[u]) for u in range(n)]

    def dfs(done, day):
        if done == all_done:
            return True
        if day > T:
            return False

        key = (done, day)
        if key in failed:
            return False

        remaining_count = n - done.bit_count()
        remaining_days = T - day + 1
        if remaining_count > remaining_days * M:
            failed.add(key)
            return False

        remaining_depths = [
            depth[u] for u in range(n) if not ((done >> u) & 1)
        ]
        remaining_depths.sort(reverse=True)
        for i, d in enumerate(remaining_depths):
            if d > remaining_days - i // M:
                failed.add(key)
                return False

        available = []
        mandatory = []
        for u in range(n):
            if (done >> u) & 1:
                continue
            if predecessors[u] & ~done == 0:
                available.append(u)
                if depth[u] == remaining_days:
                    mandatory.append(u)

        if not available or len(mandatory) > M:
            failed.add(key)
            return False

        target_size = min(M, len(available))
        mandatory_set = set(mandatory)
        optional = [u for u in available if u not in mandatory_set]
        slots = target_size - len(mandatory)

        optional.sort(key=lambda u: (-depth[u], -out_degree[u], u))

        if slots < 0 or slots > len(optional):
            failed.add(key)
            return False

        if slots == 0:
            candidates = [()]
        elif slots == len(optional):
            candidates = [tuple(optional)]
        else:
            preferred = tuple(optional[:slots])

            def candidate_generator():
                yield preferred
                for comb in itertools.combinations(optional, slots):
                    if comb != preferred:
                        yield comb

            candidates = candidate_generator()

        mandatory_mask = 0
        for u in mandatory:
            mandatory_mask |= 1 << u

        for chosen in candidates:
            batch_mask = mandatory_mask
            batch = mandatory[:]
            for u in chosen:
                batch_mask |= 1 << u
                batch.append(u)

            batches.append(batch)
            if dfs(done | batch_mask, day + 1):
                return True
            batches.pop()

        failed.add(key)
        return False

    if not dfs(0, 1):
        return None

    assignment = [0] * n
    for day, batch in enumerate(batches, 1):
        for u in batch:
            assignment[u] = day
    return assignment


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n, M, T, m = data[:4]
    if n > M * T:
        print("NO")
        return

    graph = [[] for _ in range(n)]
    reverse_graph = [[] for _ in range(n)]
    indegree = [0] * n
    reverse_indegree = [0] * n
    predecessors = [0] * n
    reverse_predecessors = [0] * n

    p = 4
    seen_edges = set()
    for _ in range(m):
        a = data[p] - 1
        b = data[p + 1] - 1
        p += 2
        if (a, b) in seen_edges:
            continue
        seen_edges.add((a, b))
        graph[a].append(b)
        reverse_graph[b].append(a)
        indegree[b] += 1
        reverse_indegree[a] += 1
        predecessors[b] |= 1 << a
        reverse_predecessors[a] |= 1 << b

    order, depth = topological_data(n, graph, indegree)
    if order is None or max(depth, default=0) > T:
        print("NO")
        return

    reverse_order, reverse_depth = topological_data(
        n, reverse_graph, reverse_indegree
    )

    for mode in range(6):
        answer = greedy_schedule(n, M, T, graph, indegree, depth, mode)
        if answer is not None:
            print("YES")
            print(*answer)
            return

        reverse_answer = greedy_schedule(
            n, M, T, reverse_graph, reverse_indegree, reverse_depth, mode
        )
        if reverse_answer is not None:
            answer = [T + 1 - d for d in reverse_answer]
            print("YES")
            print(*answer)
            return

    original_sources = sum(d == 0 for d in indegree)
    reverse_sources = sum(d == 0 for d in reverse_indegree)

    if reverse_sources < original_sources:
        reverse_answer = exact_schedule(
            n, M, T, reverse_graph, reverse_predecessors, reverse_depth
        )
        if reverse_answer is None:
            print("NO")
            return
        answer = [T + 1 - d for d in reverse_answer]
    else:
        answer = exact_schedule(n, M, T, graph, predecessors, depth)
        if answer is None:
            print("NO")
            return

    print("YES")
    print(*answer)


if __name__ == "__main__":
    main()