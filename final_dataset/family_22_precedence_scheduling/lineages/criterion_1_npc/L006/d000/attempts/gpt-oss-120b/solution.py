import sys
import threading

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
    indeg = [0]*n
    for _ in range(m):
        a = int(next(it))-1
        b = int(next(it))-1
        adj[a].append(b)
        indeg[b] += 1

    # topological order and earliest possible layer (longest path)
    from collections import deque
    q = deque([i for i in range(n) if indeg[i]==0])
    topo = []
    earliest = [1]*n  # at least 1
    while q:
        u = q.popleft()
        topo.append(u)
        for v in adj[u]:
            if earliest[v] < earliest[u] + 1:
                earliest[v] = earliest[u] + 1
            indeg[v] -= 1
            if indeg[v]==0:
                q.append(v)
    if len(topo)!=n:
        print("NO")
        return

    # check basic feasibility: earliest must be <= T
    if max(earliest) > T:
        print("NO")
        return

    # schedule greedily
    jobs_by_release = [[] for _ in range(T+1)]
    for i in range(n):
        if earliest[i] > T:
            print("NO")
            return
        jobs_by_release[earliest[i]].append(i)

    schedule = [0]*n
    import heapq
    heap = []  # store job indices ready
    for t in range(1, T+1):
        for job in jobs_by_release[t]:
            heapq.heappush(heap, job)
        cnt = 0
        while heap and cnt < M:
            job = heapq.heappop(heap)
            schedule[job] = t
            cnt += 1
    if any(x==0 for x in schedule):
        print("NO")
    else:
        print("YES")
        print(' '.join(map(str, schedule)))

def main():
    solve()

if __name__ == "__main__":
    threading.Thread(target=main).start()