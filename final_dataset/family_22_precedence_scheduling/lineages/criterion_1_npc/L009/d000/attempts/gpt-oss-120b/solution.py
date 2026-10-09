import sys
import heapq

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    M = int(next(it))
    T = int(next(it))
    m = int(next(it))

    adj = [[] for _ in range(n + 1)]
    radj = [[] for _ in range(n + 1)]
    indeg = [0] * (n + 1)

    for _ in range(m):
        a = int(next(it)); b = int(next(it))
        adj[a].append(b)
        radj[b].append(a)
        indeg[b] += 1

    # ---------- topological order & earliest ----------
    from collections import deque
    q = deque([i for i in range(1, n + 1) if indeg[i] == 0])
    topo = []
    L = [1] * (n + 1)          # earliest, 1‑based
    while q:
        v = q.popleft()
        topo.append(v)
        for w in adj[v]:
            if L[w] < L[v] + 1:
                L[w] = L[v] + 1
            indeg[w] -= 1
            if indeg[w] == 0:
                q.append(w)

    if len(topo) != n:        # cycle
        print("NO")
        return

    # ---------- latest ----------
    R = [T] * (n + 1)
    for v in reversed(topo):
        for w in adj[v]:
            if R[v] > R[w] - 1:
                R[v] = R[w] - 1

    for i in range(1, n + 1):
        if L[i] > R[i]:
            print("NO")
            return

    # ---------- greedy scheduling ----------
    start_at = [[] for _ in range(T + 2)]   # slots are 1..T
    for i in range(1, n + 1):
        start_at[L[i]].append(i)

    heap = []          # (deadline, job)
    assigned = [0] * (n + 1)

    for slot in range(1, T + 1):
        for job in start_at[slot]:
            heapq.heappush(heap, (R[job], job))
        for _ in range(M):
            if not heap:
                break
            deadline, job = heapq.heappop(heap)
            if deadline < slot:
                print("NO")
                return
            assigned[job] = slot

    if any(assigned[i] == 0 for i in range(1, n + 1)):
        print("NO")
        return

    # ---------- output ----------
    out = ["YES"]
    out.append(" ".join(str(assigned[i]) for i in range(1, n + 1)))
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()