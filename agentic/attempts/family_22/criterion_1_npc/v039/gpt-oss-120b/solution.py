import sys
import threading
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

    adj = [[] for _ in range(n)]
    radj = [[] for _ in range(n)]
    indeg = [0] * n
    for _ in range(m):
        a = int(next(it)) - 1
        b = int(next(it)) - 1
        adj[a].append(b)
        radj[b].append(a)
        indeg[b] += 1

    # topological order
    from collections import deque
    q = deque([i for i in range(n) if indeg[i] == 0])
    topo = []
    while q:
        v = q.popleft()
        topo.append(v)
        for w in adj[v]:
            indeg[w] -= 1
            if indeg[w] == 0:
                q.append(w)
    if len(topo) != n:          # cycle (should not happen per statement)
        print("NO")
        return

    # earliest times L
    L = [1] * n
    for v in topo:
        lv = L[v]
        for w in adj[v]:
            if L[w] < lv + 1:
                L[w] = lv + 1

    # latest times R
    R = [T] * n
    for v in reversed(topo):
        rv = R[v]
        for u in radj[v]:
            if R[u] > rv - 1:
                R[u] = rv - 1

    for i in range(n):
        if L[i] > R[i] or L[i] > T or R[i] < 1:
            print("NO")
            return

    # bucket jobs by release time
    buckets = [[] for _ in range(T + 2)]
    for i in range(n):
        buckets[L[i]].append(i)

    heap = []          # (deadline, job)
    ans = [0] * n
    scheduled = 0

    for t in range(1, T + 1):
        for job in buckets[t]:
            heapq.heappush(heap, (R[job], job))
        for _ in range(M):
            if not heap:
                break
            deadline, job = heapq.heappop(heap)
            if deadline < t:
                print("NO")
                return
            ans[job] = t
            scheduled += 1

    if scheduled != n:
        print("NO")
        return

    print("YES")
    print(' '.join(str(x) for x in ans))

def main():
    solve()

if __name__ == "__main__":
    threading.Thread(target=main).start()