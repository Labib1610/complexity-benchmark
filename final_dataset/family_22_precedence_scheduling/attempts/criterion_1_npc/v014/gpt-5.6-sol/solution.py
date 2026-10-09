import sys
import heapq
from collections import deque

sys.setrecursionlimit(1_000_000)


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    it = iter(data)
    n = next(it)
    M = next(it)
    T = next(it)
    m = next(it)

    if n == 0:
        print("YES")
        print()
        return

    if M <= 0 or T <= 0 or n > M * T:
        print("NO")
        return

    succ = [[] for _ in range(n)]
    pred = [[] for _ in range(n)]
    indeg = [0] * n
    outdeg = [0] * n

    for _ in range(m):
        a = next(it) - 1
        b = next(it) - 1
        succ[a].append(b)
        pred[b].append(a)
        indeg[b] += 1
        outdeg[a] += 1

    q = deque(i for i in range(n) if indeg[i] == 0)
    topo = []
    deg = indeg[:]

    while q:
        u = q.popleft()
        topo.append(u)
        for v in succ[u]:
            deg[v] -= 1
            if deg[v] == 0:
                q.append(v)

    if len(topo) != n:
        print("NO")
        return

    bottom = [1] * n
    for u in reversed(topo):
        best = 0
        for v in succ[u]:
            if bottom[v] > best:
                best = bottom[v]
        bottom[u] = best + 1

    if max(bottom) > T:
        print("NO")
        return

    top = [1] * n
    for u in topo:
        nt = top[u] + 1
        for v in succ[u]:
            if nt > top[v]:
                top[v] = nt

    def forward_greedy(mode):
        d = indeg[:]
        heap = []

        def key(v):
            if mode == 0:
                return (-bottom[v], -outdeg[v], v)
            if mode == 1:
                return (-bottom[v], -top[v], v)
            if mode == 2:
                return (-outdeg[v], -bottom[v], v)
            return (v,)

        for v in range(n):
            if d[v] == 0:
                heapq.heappush(heap, (key(v), v))

        ans = [0] * n
        done = 0
        slot = 0

        while heap:
            slot += 1
            batch = []
            for _ in range(min(M, len(heap))):
                _, u = heapq.heappop(heap)
                batch.append(u)
                ans[u] = slot
                done += 1

            for u in batch:
                for v in succ[u]:
                    d[v] -= 1
                    if d[v] == 0:
                        heapq.heappush(heap, (key(v), v))

        if done == n and slot <= T:
            return ans
        return None

    for mode in range(4):
        ans = forward_greedy(mode)
        if ans is not None:
            print("YES")
            print(*ans)
            return

    def reverse_greedy(mode):
        d = outdeg[:]
        heap = []

        def key(v):
            if mode == 0:
                return (-top[v], -indeg[v], v)
            if mode == 1:
                return (-top[v], -bottom[v], v)
            return (-indeg[v], -top[v], v)

        for v in range(n):
            if d[v] == 0:
                heapq.heappush(heap, (key(v), v))

        ans = [0] * n
        done = 0
        slot = T

        while heap:
            if slot <= 0:
                return None

            batch = []
            for _ in range(min(M, len(heap))):
                _, u = heapq.heappop(heap)
                batch.append(u)
                ans[u] = slot
                done += 1

            for u in batch:
                for p in pred[u]:
                    d[p] -= 1
                    if d[p] == 0:
                        heapq.heappush(heap, (key(p), p))
            slot -= 1

        if done == n:
            return ans
        return None

    for mode in range(3):
        ans = reverse_greedy(mode)
        if ans is not None:
            print("YES")
            print(*ans)
            return

    pred_mask = [0] * n
    succ_mask = [0] * n
    for u in range(n):
        pm = 0
        for p in pred[u]:
            pm |= 1 << p
        pred_mask[u] = pm

        sm = 0
        for v in succ[u]:
            sm |= 1 << v
        succ_mask[u] = sm

    full_mask = (1 << n) - 1
    available = 0
    for v in range(n):
        if indeg[v] == 0:
            available |= 1 << v

    answer = [0] * n
    failed = set()

    def dfs(done, avail, slot):
        if done == full_mask:
            return True

        remaining_slots = T - slot
        remaining_jobs = n - done.bit_count()

        if remaining_slots <= 0 or remaining_jobs > remaining_slots * M:
            return False

        state = (done, slot)
        if state in failed:
            return False

        avail_count = avail.bit_count()
        if avail_count == 0:
            failed.add(state)
            return False

        mandatory = 0
        x = avail
        while x:
            bit = x & -x
            v = bit.bit_length() - 1
            if bottom[v] > remaining_slots:
                failed.add(state)
                return False
            if bottom[v] == remaining_slots:
                mandatory |= bit
            x ^= bit

        mandatory_count = mandatory.bit_count()
        take = min(M, avail_count)

        if mandatory_count > take:
            failed.add(state)
            return False

        need = take - mandatory_count
        optional = avail & ~mandatory

        def try_selection(selected):
            new_done = done | selected
            new_avail = avail & ~selected

            y = selected
            candidates = 0
            while y:
                bit = y & -y
                u = bit.bit_length() - 1
                candidates |= succ_mask[u]
                y ^= bit

            candidates &= ~new_done
            y = candidates
            while y:
                bit = y & -y
                v = bit.bit_length() - 1
                if pred_mask[v] & ~new_done == 0:
                    new_avail |= bit
                y ^= bit

            y = selected
            while y:
                bit = y & -y
                answer[bit.bit_length() - 1] = slot + 1
                y ^= bit

            if dfs(new_done, new_avail, slot + 1):
                return True

            y = selected
            while y:
                bit = y & -y
                answer[bit.bit_length() - 1] = 0
                y ^= bit
            return False

        if need == 0:
            if try_selection(mandatory):
                return True
            failed.add(state)
            return False

        groups_dict = {}
        x = optional
        while x:
            bit = x & -x
            v = bit.bit_length() - 1
            signature = succ_mask[v]
            groups_dict.setdefault(signature, []).append(v)
            x ^= bit

        groups = list(groups_dict.values())
        groups.sort(
            key=lambda g: (
                -bottom[g[0]],
                -outdeg[g[0]],
                g[0]
            )
        )

        suffix_sizes = [0] * (len(groups) + 1)
        for i in range(len(groups) - 1, -1, -1):
            suffix_sizes[i] = suffix_sizes[i + 1] + len(groups[i])

        def choose_groups(index, left, chosen):
            if left == 0:
                return try_selection(mandatory | chosen)
            if index == len(groups) or suffix_sizes[index] < left:
                return False

            group = groups[index]
            upper = min(len(group), left)
            lower = max(0, left - suffix_sizes[index + 1])

            prefix_masks = [0] * (upper + 1)
            pm = 0
            for i in range(upper):
                pm |= 1 << group[i]
                prefix_masks[i + 1] = pm

            for count in range(upper, lower - 1, -1):
                if choose_groups(
                    index + 1,
                    left - count,
                    chosen | prefix_masks[count]
                ):
                    return True
            return False

        if choose_groups(0, need, 0):
            return True

        failed.add(state)
        return False

    if dfs(0, available, 0):
        print("YES")
        print(*answer)
    else:
        print("NO")


if __name__ == "__main__":
    main()