import sys
import collections
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
    indeg = [0]*n
    outdeg = [0]*n
    for _ in range(m):
        a = int(next(it))-1
        b = int(next(it))-1
        adj[a].append(b)
        radj[b].append(a)
        indeg[b] += 1
        outdeg[a] += 1

    # topological order
    q = collections.deque([i for i in range(n) if indeg[i]==0])
    topo = []
    while q:
        u = q.popleft()
        topo.append(u)
        for v in adj[u]:
            indeg[v] -= 1
            if indeg[v]==0:
                q.append(v)
    if len(topo)!=n:
        print("NO")
        return

    # earliest slots
    E = [1]*n
    for u in topo:
        for v in adj[u]:
            if E[v] < E[u]+1:
                E[v] = E[u]+1

    # latest slots
    L = [T]*n
    for u in reversed(topo):
        for v in adj[u]:
            if L[u] > L[v]-1:
                L[u] = L[v]-1

    for i in range(n):
        if E[i] > L[i] or E[i] > T or L[i] < 1:
            print("NO")
            return

    # bucket jobs by earliest start
    bucket = [[] for _ in range(T+2)]
    for i in range(n):
        bucket[E[i]].append(i)

    assigned = [0]*n
    heap = []  # (L, job)
    for slot in range(1, T+1):
        for job in bucket[slot]:
            heapq.heappush(heap, (L[job], job))
        cnt = 0
        while cnt < M and heap:
            deadline, job = heapq.heappop(heap)
            if deadline < slot:   # missed deadline
                print("NO")
                return
            assigned[job] = slot
            cnt += 1

    if any(a==0 for a in assigned):
        print("NO")
        return

    print("YES")
    print(' '.join(str(assigned[i]) for i in range(n)))

if __name__ == "__main__":
    solve()