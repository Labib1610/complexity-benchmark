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
        for to in adj[v]:
            indeg[to] -= 1
            if indeg[to] == 0:
                q.append(to)
    if len(topo) != n:
        print("NO")
        return

    # earliest
    earliest = [1] * n
    for v in topo:
        for to in adj[v]:
            if earliest[to] < earliest[v] + 1:
                earliest[to] = earliest[v] + 1

    # longest path to a sink (len_to_end)
    len_to_end = [1] * n
    for v in reversed(topo):
        for pre in radj[v]:
            if len_to_end[pre] < len_to_end[v] + 1:
                len_to_end[pre] = len_to_end[v] + 1

    latest = [T - len_to_end[i] + 1 for i in range(n)]

    for i in range(n):
        if earliest[i] > latest[i] or earliest[i] > T or latest[i] < 1:
            print("NO")
            return

    # bucket dishes by earliest
    bucket = [[] for _ in range(T + 2)]
    for i in range(n):
        e = earliest[i]
        if e <= T:
            bucket[e].append(i)

    heap = []          # (latest, dish)
    assign = [0] * n
    for round_num in range(1, T + 1):
        for dish in bucket[round_num]:
            heapq.heappush(heap, (latest[dish], dish))
        cnt = 0
        while cnt < M and heap:
            dl, dish = heapq.heappop(heap)
            if dl < round_num:          # missed deadline
                print("NO")
                return
            assign[dish] = round_num
            cnt += 1

    if any(a == 0 for a in assign):
        print("NO")
        return

    print("YES")
    print(' '.join(map(str, assign)))

if __name__ == "__main__":
    solve()