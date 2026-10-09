import sys
import heapq

sys.setrecursionlimit(1_000_000)


def topological_order(n, adj, indeg):
    deg = indeg[:]
    queue = [i for i in range(n) if deg[i] == 0]
    order = []
    p = 0

    while p < len(queue):
        u = queue[p]
        p += 1
        order.append(u)
        for v in adj[u]:
            deg[v] -= 1
            if deg[v] == 0:
                queue.append(v)

    return order if len(order) == n else None


def calculate_bottom(n, adj, topo):
    bottom = [1] * n
    for u in reversed(topo):
        best = 0
        for v in adj[u]:
            if bottom[v] > best:
                best = bottom[v]
        bottom[u] = best + 1
    return bottom


def greedy_schedule(n, M, T, adj, indeg, bottom, mode):
    heap = []

    def key(u):
        if mode == 0:
            return (-bottom[u], -len(adj[u]), u)
        if mode == 1:
            return (-len(adj[u]), -bottom[u], u)
        return (-bottom[u], u)

    deg = indeg[:]
    for u in range(n):
        if deg[u] == 0:
            heapq.heappush(heap, key(u))

    batches = []
    processed = 0

    while heap:
        batch = []
        take = min(M, len(heap))
        for _ in range(take):
            item = heapq.heappop(heap)
            batch.append(item[-1])

        batches.append(batch)
        if len(batches) > T:
            return None

        newly_available = []
        for u in batch:
            processed += 1
            for v in adj[u]:
                deg[v] -= 1
                if deg[v] == 0:
                    newly_available.append(v)

        for v in newly_available:
            heapq.heappush(heap, key(v))

    return batches if processed == n else None


def exact_schedule(n, M, T, adj, bottom):
    full = (1 << n) - 1
    pred = [0] * n
    succ = [0] * n

    for u in range(n):
        sm = 0
        bit_u = 1 << u
        for v in adj[u]:
            sm |= 1 << v
            pred[v] |= bit_u
        succ[u] = sm

    memo = set()
    path = []

    def dfs(done, rounds_left):
        if done == full:
            return True
        if rounds_left == 0:
            return False

        state = (done, rounds_left)
        if state in memo:
            return False

        remaining = full ^ done
        remaining_count = remaining.bit_count()
        if remaining_count > M * rounds_left:
            memo.add(state)
            return False

        available_mask = 0
        mandatory_mask = 0
        deadline_counts = {}

        x = remaining
        while x:
            bit = x & -x
            x -= bit
            u = bit.bit_length() - 1

            b = bottom[u]
            if b > rounds_left:
                memo.add(state)
                return False
            deadline_counts[b] = deadline_counts.get(b, 0) + 1

            if pred[u] & remaining == 0:
                available_mask |= bit
                if b == rounds_left:
                    mandatory_mask |= bit

        cumulative = 0
        for b in sorted(deadline_counts, reverse=True):
            cumulative += deadline_counts[b]
            available_rounds = rounds_left - b + 1
            if cumulative > M * available_rounds:
                memo.add(state)
                return False

        available_count = available_mask.bit_count()
        if available_count == 0:
            memo.add(state)
            return False

        take = min(M, available_count)
        mandatory_count = mandatory_mask.bit_count()
        if mandatory_count > take:
            memo.add(state)
            return False

        if available_count <= M:
            selected = available_mask
            path.append(selected)
            if dfs(done | selected, rounds_left - 1):
                return True
            path.pop()
            memo.add(state)
            return False

        optional_mask = available_mask ^ mandatory_mask
        need = take - mandatory_count

        groups_dict = {}
        x = optional_mask
        while x:
            bit = x & -x
            x -= bit
            u = bit.bit_length() - 1
            groups_dict.setdefault(succ[u], []).append(bit)

        groups = []
        for sm, bits in groups_dict.items():
            first = bits[0].bit_length() - 1
            prefix = [0]
            cur = 0
            for bit in bits:
                cur |= bit
                prefix.append(cur)
            groups.append((bottom[first], sm.bit_count(), len(bits), prefix))

        groups.sort(key=lambda g: (-g[0], -g[1], -g[2]))
        suffix_capacity = [0] * (len(groups) + 1)
        for i in range(len(groups) - 1, -1, -1):
            suffix_capacity[i] = suffix_capacity[i + 1] + groups[i][2]

        def choose_group(i, left, chosen):
            if left == 0:
                selected = mandatory_mask | chosen
                path.append(selected)
                if dfs(done | selected, rounds_left - 1):
                    return True
                path.pop()
                return False

            if i == len(groups) or suffix_capacity[i] < left:
                return False

            size = groups[i][2]
            prefixes = groups[i][3]
            low = max(0, left - suffix_capacity[i + 1])
            high = min(size, left)

            for count in range(high, low - 1, -1):
                if choose_group(i + 1, left - count, chosen | prefixes[count]):
                    return True
            return False

        if choose_group(0, need, 0):
            return True

        memo.add(state)
        return False

    if dfs(0, T):
        result = []
        for mask in path:
            batch = []
            while mask:
                bit = mask & -mask
                mask -= bit
                batch.append(bit.bit_length() - 1)
            result.append(batch)
        return result

    return None


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n, M, T, m = data[:4]
    if M <= 0 or T <= 0 or n > M * T:
        print("NO")
        return

    adj = [[] for _ in range(n)]
    rev = [[] for _ in range(n)]
    indeg = [0] * n
    outdeg = [0] * n

    p = 4
    for _ in range(m):
        a = data[p] - 1
        b = data[p + 1] - 1
        p += 2
        adj[a].append(b)
        rev[b].append(a)
        indeg[b] += 1
        outdeg[a] += 1

    topo = topological_order(n, adj, indeg)
    if topo is None:
        print("NO")
        return

    bottom = calculate_bottom(n, adj, topo)
    if max(bottom, default=0) > T:
        print("NO")
        return

    reverse_topo = topo[::-1]
    reverse_bottom = calculate_bottom(n, rev, reverse_topo)

    for mode in range(3):
        batches = greedy_schedule(n, M, T, adj, indeg, bottom, mode)
        if batches is not None:
            answer = [0] * n
            for r, batch in enumerate(batches, 1):
                for u in batch:
                    answer[u] = r
            print("YES")
            print(*answer)
            return

    for mode in range(3):
        batches = greedy_schedule(n, M, T, rev, outdeg, reverse_bottom, mode)
        if batches is not None:
            batches.reverse()
            answer = [0] * n
            for r, batch in enumerate(batches, 1):
                for u in batch:
                    answer[u] = r
            print("YES")
            print(*answer)
            return

    source_count = sum(d == 0 for d in indeg)
    sink_count = sum(d == 0 for d in outdeg)

    if source_count <= sink_count:
        batches = exact_schedule(n, M, T, adj, bottom)
        reversed_orientation = False
    else:
        batches = exact_schedule(n, M, T, rev, reverse_bottom)
        reversed_orientation = True

    if batches is None:
        print("NO")
        return

    if reversed_orientation:
        batches.reverse()

    answer = [0] * n
    for r, batch in enumerate(batches, 1):
        for u in batch:
            answer[u] = r

    print("YES")
    print(*answer)


if __name__ == "__main__":
    main()