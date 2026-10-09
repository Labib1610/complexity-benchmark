import sys
sys.setrecursionlimit(1 << 25)

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
    pred = [[] for _ in range(n)]
    indeg = [0] * n
    for _ in range(m):
        a = int(next(it)) - 1
        b = int(next(it)) - 1
        adj[a].append(b)
        pred[b].append(a)
        indeg[b] += 1

    # Kahn's algorithm
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

    # DSU for next free room
    parent = list(range(T + 2))   # 1..T, T+1 sentinel

    def find(x: int) -> int:
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    cnt = [0] * (T + 1)
    room = [0] * n

    for v in topo:
        lb = 1
        for p in pred[v]:
            rp = room[p] + 1
            if rp > lb:
                lb = rp
        r = find(lb)
        if r > T:
            print("NO")
            return
        room[v] = r
        cnt[r] += 1
        if cnt[r] == M:
            parent[r] = find(r + 1)   # union with next

    print("YES")
    print(' '.join(str(room[i]) for i in range(n)))

if __name__ == "__main__":
    solve()