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

    succ = [[] for _ in range(n)]
    pred = [[] for _ in range(n)]
    indeg = [0] * n
    for _ in range(m):
        a = int(next(it)) - 1
        b = int(next(it)) - 1
        succ[a].append(b)
        pred[b].append(a)
        indeg[b] += 1

    # ---------- topological order ----------
    q = deque([i for i, d in enumerate(indeg) if d == 0])
    topo = []
    while q:
        v = q.popleft()
        topo.append(v)
        for nb in succ[v]:
            indeg[nb] -= 1
            if indeg[nb] == 0:
                q.append(nb)

    if len(topo) != n:          # cycle
        print("NO")
        return

    pos_in_topo = [0] * n
    for idx, v in enumerate(topo):
        pos_in_topo[v] = idx

    # ---------- labeling ----------
    label = [0] * n
    # process in reverse topological order
    for v in reversed(topo):
        # collect labels of successors
        labs = [label[u] for u in succ[v]]
        if not labs:
            label[v] = 1
            continue
        labs.sort(reverse=True)
        # keep only M largest
        if len(labs) > M:
            labs = labs[:M]
        # find smallest missing positive integer
        present = set()
        for x in labs:
            if x <= M + 1:
                present.add(x)
        cur = 1
        while cur in present:
            cur += 1
        label[v] = cur

    # ---------- order by label ----------
    order = list(range(n))
    order.sort(key=lambda x: (label[x], pos_in_topo[x]))

    # ---------- list scheduling ----------
    slot = [0] * n
    used = []          # used[i] = number of tasks in slot i+1
    for v in order:
        earliest = 1
        for p in pred[v]:
            if slot[p] + 1 > earliest:
                earliest = slot[p] + 1
        # ensure used list is long enough
        while len(used) < earliest:
            used.append(0)
        # move to first slot with free capacity
        while used[earliest - 1] >= M:
            earliest += 1
            if len(used) < earliest:
                used.append(0)
        slot[v] = earliest
        used[earliest - 1] += 1

    makespan = max(slot)
    if makespan > T:
        print("NO")
        return

    # output
    print("YES")
    print(' '.join(str(slot[i]) for i in range(n)))

if __name__ == "__main__":
    solve()