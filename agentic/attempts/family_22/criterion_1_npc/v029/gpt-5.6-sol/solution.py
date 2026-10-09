import sys
import heapq

sys.setrecursionlimit(1_000_000)

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n, M, T, m = data[:4]
    pred_mask = [0] * n
    succ_mask = [0] * n

    p = 4
    for _ in range(m):
        a = data[p] - 1
        b = data[p + 1] - 1
        p += 2
        if a != b:
            succ_mask[a] |= 1 << b
            pred_mask[b] |= 1 << a

    succ = [[] for _ in range(n)]
    pred = [[] for _ in range(n)]
    indeg = [0] * n
    outdeg = [0] * n

    for v in range(n):
        mask = succ_mask[v]
        while mask:
            bit = mask & -mask
            u = bit.bit_length() - 1
            succ[v].append(u)
            pred[u].append(v)
            mask ^= bit
        outdeg[v] = len(succ[v])
        indeg[v] = len(pred[v])

    # Coffman-Graham labeling, also detects cycles.
    remaining_out = outdeg[:]
    labels = [0] * n
    label_heap = []

    for v in range(n):
        if remaining_out[v] == 0:
            heapq.heappush(label_heap, ((), v))

    for current_label in range(1, n + 1):
        if not label_heap:
            print("NO")
            return
        _, v = heapq.heappop(label_heap)
        labels[v] = current_label

        for u in pred[v]:
            remaining_out[u] -= 1
            if remaining_out[u] == 0:
                key = tuple(sorted((labels[x] for x in succ[u]), reverse=True))
                heapq.heappush(label_heap, (key, u))

    topo = sorted(range(n), key=lambda x: -labels[x])

    bottom = [1] * n
    for v in reversed(topo):
        if succ[v]:
            bottom[v] = 1 + max(bottom[u] for u in succ[v])

    height = max(bottom, default=0)
    if height > T or n > M * T:
        print("NO")
        return

    def output(schedule):
        print("YES")
        print(" ".join(map(str, schedule)))

    if n == 0:
        print("YES")
        print()
        return

    if T >= n:
        schedule = [0] * n
        for i, v in enumerate(topo, 1):
            schedule[v] = i
        output(schedule)
        return

    if M >= n:
        schedule = [1] * n
        for v in topo:
            if pred[v]:
                schedule[v] = 1 + max(schedule[u] for u in pred[v])
        if max(schedule) <= T:
            output(schedule)
        else:
            print("NO")
        return

    # Coffman-Graham schedule.
    parent = list(range(n + 2))
    occupancy = [0] * (n + 2)

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    cg_schedule = [0] * n
    for v in topo:
        release = 1
        if pred[v]:
            release = 1 + max(cg_schedule[u] for u in pred[v])
        level = find(release)
        cg_schedule[v] = level
        occupancy[level] += 1
        if occupancy[level] == M:
            parent[level] = find(level + 1)

    cg_makespan = max(cg_schedule)
    if cg_makespan <= T:
        output(cg_schedule)
        return

    # Coffman-Graham is optimal for two processors.
    if M <= 2:
        print("NO")
        return

    def list_schedule(mode, seed=0):
        deg = indeg[:]
        ready = []

        def priority(v):
            if mode == 0:
                return (-bottom[v], -outdeg[v], v)
            if mode == 1:
                return (-outdeg[v], -bottom[v], v)
            if mode == 2:
                return (-labels[v], v)
            if mode == 3:
                h = ((v + 1) * 0x9E3779B185EBCA87 + seed) & ((1 << 64) - 1)
                return (-bottom[v], h, v)
            h = ((v + 1) * 0xD6E8FEB86659FD93 + seed) & ((1 << 64) - 1)
            return (h, -bottom[v], v)

        for v in range(n):
            if deg[v] == 0:
                heapq.heappush(ready, (priority(v), v))

        schedule = [0] * n
        done_count = 0
        time_step = 0

        while ready:
            time_step += 1
            batch = []
            for _ in range(min(M, len(ready))):
                _, v = heapq.heappop(ready)
                batch.append(v)
                schedule[v] = time_step

            done_count += len(batch)
            for v in batch:
                for u in succ[v]:
                    deg[u] -= 1
                    if deg[u] == 0:
                        heapq.heappush(ready, (priority(u), u))

        if done_count == n and time_step <= T:
            return schedule
        return None

    for mode in range(3):
        result = list_schedule(mode)
        if result is not None:
            output(result)
            return

    for seed in range(8):
        result = list_schedule(3, seed * 0xA0761D6478BD642F)
        if result is not None:
            output(result)
            return

    for seed in range(4):
        result = list_schedule(4, seed * 0xE7037ED1A0B428DB)
        if result is not None:
            output(result)
            return

    # Exact branch-and-bound search.
    all_mask = (1 << n) - 1
    initial_ready = 0
    for v in range(n):
        if pred_mask[v] == 0:
            initial_ready |= 1 << v

    failed = set()
    answer_batches = []

    def dfs(done, ready_mask, remaining_steps):
        nonlocal answer_batches

        if done == all_mask:
            answer_batches = []
            return True
        if remaining_steps == 0:
            return False

        rem_mask = all_mask ^ done
        rem_count = rem_mask.bit_count()
        if rem_count > remaining_steps * M:
            return False

        # Necessary deadline-density conditions and forced jobs.
        deadline_counts = [0] * (remaining_steps + 1)
        critical = 0
        x = rem_mask
        while x:
            bit = x & -x
            v = bit.bit_length() - 1
            b = bottom[v]
            if b > remaining_steps:
                return False
            latest = remaining_steps - b + 1
            deadline_counts[latest] += 1
            if latest == 1:
                critical |= bit
            x ^= bit

        cumulative = 0
        for t in range(1, remaining_steps + 1):
            cumulative += deadline_counts[t]
            if cumulative > t * M:
                return False

        if critical & ~ready_mask:
            return False
        if critical.bit_count() > M:
            return False

        state = (done, remaining_steps)
        if state in failed:
            return False

        ready_count = ready_mask.bit_count()
        if ready_count == 0:
            failed.add(state)
            return False

        take = min(M, ready_count)

        def advance(batch):
            done2 = done | batch
            ready2 = ready_mask & ~batch

            affected = 0
            y = batch
            while y:
                bit = y & -y
                v = bit.bit_length() - 1
                affected |= succ_mask[v]
                y ^= bit

            affected &= ~done2
            y = affected
            while y:
                bit = y & -y
                v = bit.bit_length() - 1
                if pred_mask[v] & ~done2 == 0:
                    ready2 |= bit
                y ^= bit

            if dfs(done2, ready2, remaining_steps - 1):
                answer_batches.append(batch)
                return True
            return False

        if ready_count <= M:
            if advance(ready_mask):
                return True
            failed.add(state)
            return False

        forced = critical
        need = take - forced.bit_count()
        optional_mask = ready_mask & ~forced

        optional = []
        y = optional_mask
        while y:
            bit = y & -y
            v = bit.bit_length() - 1
            signature = succ_mask[v] & rem_mask
            optional.append((v, signature))
            y ^= bit

        optional.sort(key=lambda z: (-bottom[z[0]], -outdeg[z[0]], z[0]))

        def choose(start, left, chosen):
            if left == 0:
                return advance(forced | chosen)
            if len(optional) - start < left:
                return False

            seen_signatures = set()
            limit = len(optional) - left + 1
            for i in range(start, limit):
                v, sig = optional[i]
                if sig in seen_signatures:
                    continue
                seen_signatures.add(sig)
                if choose(i + 1, left - 1, chosen | (1 << v)):
                    return True
            return False

        if choose(0, need, 0):
            return True

        failed.add(state)
        return False

    if not dfs(0, initial_ready, T):
        print("NO")
        return

    answer_batches.reverse()
    schedule = [0] * n
    for t, batch in enumerate(answer_batches, 1):
        x = batch
        while x:
            bit = x & -x
            v = bit.bit_length() - 1
            schedule[v] = t
            x ^= bit

    output(schedule)

if __name__ == "__main__":
    main()