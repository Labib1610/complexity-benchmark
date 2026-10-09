import sys
import heapq
from itertools import combinations

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    it = iter(data)
    n = next(it)
    M = next(it)
    T = next(it)
    m = next(it)

    if M <= 0 or T <= 0 or n > M * T:
        print("NO")
        return

    succ = [[] for _ in range(n)]
    pred_mask = [0] * n
    indeg = [0] * n

    for _ in range(m):
        a = next(it) - 1
        b = next(it) - 1
        if (pred_mask[b] >> a) & 1 == 0:
            pred_mask[b] |= 1 << a
            succ[a].append(b)
            indeg[b] += 1

    queue = [v for v in range(n) if indeg[v] == 0]
    topo = []
    head = 0
    while head < len(queue):
        v = queue[head]
        head += 1
        topo.append(v)
        for w in succ[v]:
            indeg[w] -= 1
            if indeg[w] == 0:
                queue.append(w)

    if len(topo) != n:
        print("NO")
        return

    bottom = [1] * n
    descendants = [0] * n
    for v in reversed(topo):
        best = 0
        dm = 0
        for w in succ[v]:
            if bottom[w] > best:
                best = bottom[w]
            dm |= (1 << w) | descendants[w]
        bottom[v] = best + 1
        descendants[v] = dm

    if max(bottom, default=0) > T:
        print("NO")
        return

    # First try the standard critical-path list schedule.
    indeg_now = [pred_mask[v].bit_count() for v in range(n)]
    heap = []
    for v in range(n):
        if indeg_now[v] == 0:
            heapq.heappush(heap, (-bottom[v], -len(succ[v]), v))

    greedy_slot = [0] * n
    completed = 0
    current_time = 1

    while completed < n:
        if not heap:
            print("NO")
            return
        batch = []
        for _ in range(min(M, len(heap))):
            _, _, v = heapq.heappop(heap)
            batch.append(v)
            greedy_slot[v] = current_time

        completed += len(batch)
        newly_available = []
        for v in batch:
            for w in succ[v]:
                indeg_now[w] -= 1
                if indeg_now[w] == 0:
                    newly_available.append(w)
        for w in newly_available:
            heapq.heappush(heap, (-bottom[w], -len(succ[w]), w))
        current_time += 1

    if current_time - 1 <= T:
        print("YES")
        print(*greedy_slot)
        return

    # Exact search over non-delay schedules.
    full_mask = (1 << n) - 1
    answer = [0] * n
    failed = set()

    # Safe dominance relation for moderate n:
    # among simultaneously available tasks, a task whose descendant set
    # contains another's may be scheduled no later.
    dominance = None
    if n <= 400:
        dominance = [0] * n
        for v in range(n):
            dv = descendants[v]
            mask = 0
            for u in range(n):
                if u == v:
                    continue
                du = descendants[u]
                if dv & ~du == 0:
                    if dv != du or u < v:
                        mask |= 1 << u
            dominance[v] = mask

    sys.setrecursionlimit(max(10000, n * 3 + 100))

    def deadline_feasible(done, rem):
        remaining_count = n - done.bit_count()
        if remaining_count > rem * M:
            return False

        counts = {}
        x = full_mask ^ done
        max_b = 0
        while x:
            lb = x & -x
            v = lb.bit_length() - 1
            b = bottom[v]
            if b > rem:
                return False
            counts[b] = counts.get(b, 0) + 1
            if b > max_b:
                max_b = b
            x ^= lb

        cumulative = 0
        for b in sorted(counts, reverse=True):
            cumulative += counts[b]
            slots_until_deadline = rem - b + 1
            if cumulative > slots_until_deadline * M:
                return False
        return True

    def dfs(done, time_slot):
        if done == full_mask:
            return True
        if done in failed:
            return False

        rem = T - time_slot + 1
        if rem <= 0 or not deadline_feasible(done, rem):
            failed.add(done)
            return False

        not_done = full_mask ^ done
        available = []
        x = not_done
        while x:
            lb = x & -x
            v = lb.bit_length() - 1
            if pred_mask[v] & not_done == 0:
                available.append(v)
            x ^= lb

        if not available:
            failed.add(done)
            return False

        take = min(M, len(available))
        available.sort(key=lambda v: (-bottom[v], -descendants[v].bit_count(), v))

        if len(available) <= M:
            selected_options = [tuple(available)]
        else:
            forced_mask = 0
            for v in available:
                if bottom[v] == rem:
                    forced_mask |= 1 << v

            avail_mask = 0
            for v in available:
                avail_mask |= 1 << v

            if dominance is not None:
                changed = True
                while changed:
                    changed = False
                    x = forced_mask
                    add = 0
                    while x:
                        lb = x & -x
                        v = lb.bit_length() - 1
                        add |= dominance[v] & avail_mask
                        x ^= lb
                    new_mask = forced_mask | add
                    if new_mask != forced_mask:
                        forced_mask = new_mask
                        changed = True

            forced = [v for v in available if (forced_mask >> v) & 1]
            if len(forced) > take:
                failed.add(done)
                return False

            optional = [v for v in available if not ((forced_mask >> v) & 1)]
            need = take - len(forced)

            def option_generator():
                for comb in combinations(optional, need):
                    selected = tuple(forced) + comb
                    if dominance is not None:
                        sm = 0
                        for v in selected:
                            sm |= 1 << v
                        valid = True
                        for v in selected:
                            if dominance[v] & avail_mask & ~sm:
                                valid = False
                                break
                        if not valid:
                            continue
                    yield selected

            selected_options = option_generator()

        for selected in selected_options:
            sm = 0
            for v in selected:
                sm |= 1 << v
                answer[v] = time_slot

            new_done = done | sm
            if dfs(new_done, time_slot + 1):
                return True

            for v in selected:
                answer[v] = 0

        failed.add(done)
        return False

    if dfs(0, 1):
        print("YES")
        print(*answer)
    else:
        print("NO")

if __name__ == "__main__":
    main()