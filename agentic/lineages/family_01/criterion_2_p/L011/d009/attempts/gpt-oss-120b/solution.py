import sys
sys.setrecursionlimit(1 << 25)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(it)); v = int(next(it))
        adj[u].append(v)
        adj[v].append(u)

    if m == 0:
        # all 1s is optimal
        print("YES")
        print(" ".join(["1"] * n))
        return

    col = [-1] * (n + 1)          # -1 = unvisited, 0/1 = parity colour
    ans = [0] * (n + 1)           # final states, 1-indexed
    from collections import deque

    for start in range(1, n + 1):
        if col[start] != -1:
            continue
        # BFS this component
        q = deque([start])
        col[start] = 0
        verts = []
        ok = True
        while q:
            v = q.popleft()
            verts.append(v)
            for to in adj[v]:
                if col[to] == -1:
                    col[to] = col[v] ^ 1
                    q.append(to)
                elif col[to] == col[v]:
                    print("NO")
                    return
        # decide which assignment is lexicographically smaller
        verts.sort()   # ensure increasing index order
        seqA = [1 if col[v] == 0 else 2 for v in verts]
        seqB = [2 if col[v] == 0 else 1 for v in verts]
        if seqA <= seqB:
            for v, val in zip(verts, seqA):
                ans[v] = val
        else:
            for v, val in zip(verts, seqB):
                ans[v] = val

    print("YES")
    print(" ".join(str(ans[i]) for i in range(1, n + 1)))

if __name__ == "__main__":
    solve()