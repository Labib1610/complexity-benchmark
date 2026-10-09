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

    side = [-1] * (n + 1)          # 0 or 1 for bipartition
    answer = [0] * (n + 1)         # final 1/2 values

    from collections import deque

    for start in range(1, n + 1):
        if side[start] != -1:
            continue
        # BFS this component
        q = deque([start])
        side[start] = 0
        comp = [start]
        ok = True
        while q:
            u = q.popleft()
            for v in adj[u]:
                if side[v] == -1:
                    side[v] = side[u] ^ 1
                    q.append(v)
                    comp.append(v)
                elif side[v] == side[u]:
                    print("NO")
                    return
        # choose mapping to make smallest index vertex have value 1
        min_v = min(comp)
        if side[min_v] == 0:
            # map 0->1, 1->2
            for v in comp:
                answer[v] = 1 if side[v] == 0 else 2
        else:
            # map 0->2, 1->1
            for v in comp:
                answer[v] = 2 if side[v] == 0 else 1

    # all vertices assigned
    print("YES")
    print(' '.join(str(answer[i]) for i in range(1, n + 1)))

if __name__ == "__main__":
    solve()