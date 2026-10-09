import sys

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
    indeg = [0] * n
    for _ in range(m):
        a = int(next(it)) - 1
        b = int(next(it)) - 1
        adj[a].append(b)
        indeg[b] += 1

    # Kahn's algorithm
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

    if len(topo) != n:          # cycle
        print("NO")
        return

    # DSU for next free section
    parent = list(range(T + 2))   # 1..T, T+1 sentinel

    def find(x: int) -> int:
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    cnt = [0] * (T + 1)          # 1‑based
    need = [0] * n               # max predecessor section
    ans = [0] * n

    for v in topo:
        x = need[v] + 1          # minimal possible section
        s = find(x)
        if s > T:
            print("NO")
            return
        ans[v] = s
        cnt[s] += 1
        if cnt[s] == M:
            parent[s] = s + 1    # union with next
        for w in adj[v]:
            if need[w] < s:
                need[w] = s

    # output
    out = ["YES"]
    out.append(" ".join(str(ans[i]) for i in range(n)))
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()