import sys
from collections import deque

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    M = int(next(it))
    T = int(next(it))
    m = int(next(it))

    preMask = [0] * n          # bitmask of direct predecessors
    for _ in range(m):
        a = int(next(it)) - 1
        b = int(next(it)) - 1
        preMask[b] |= 1 << a

    FULL = (1 << n) - 1
    # BFS
    q = deque()
    q.append(0)
    parent = {0: -1}          # previous mask
    chosen = {0: 0}            # subset scheduled to reach this mask
    depth = {0: 0}

    while q:
        mask = q.popleft()
        d = depth[mask]
        if d == T:            # cannot use more slots
            continue

        # compute ready jobs
        ready = 0
        for i in range(n):
            if not (mask >> i) & 1:
                if (preMask[i] & mask) == preMask[i]:
                    ready |= 1 << i

        # enumerate non‑empty subsets of ready
        s = ready
        while s:
            if s.bit_count() <= M:
                new_mask = mask | s
                if new_mask not in depth:
                    parent[new_mask] = mask
                    chosen[new_mask] = s
                    depth[new_mask] = d + 1
                    q.append(new_mask)
            s = (s - 1) & ready

    if FULL not in depth or depth[FULL] > T:
        print("NO")
        return

    # reconstruct schedule
    slots = [0] * n
    cur = FULL
    order = []          # list of subsets, last slot first
    while cur != 0:
        order.append(chosen[cur])
        cur = parent[cur]
    order.reverse()     # now first slot first

    for slot_idx, subset in enumerate(order, start=1):
        s = subset
        while s:
            lsb = s & -s
            job = (lsb.bit_length() - 1)
            slots[job] = slot_idx
            s ^= lsb

    # slots for jobs not scheduled (should not happen) stay 0 – but all are scheduled
    print("YES")
    print(' '.join(str(slots[i]) for i in range(n)))

if __name__ == "__main__":
    solve()