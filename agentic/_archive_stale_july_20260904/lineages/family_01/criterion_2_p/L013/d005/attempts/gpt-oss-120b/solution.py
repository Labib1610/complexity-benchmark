import sys
from collections import deque

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

    part = [-1] * (n + 1)          # 0 or 1 partition
    ans = [0] * (n + 1)            # final rule numbers (1 or 2)

    for start in range(1, n + 1):
        if part[start] != -1:
            continue
        # BFS this component
        q = deque([start])
        part[start] = 0
        comp_nodes = [start]
        min_node = start
        ok = True
        while q:
            u = q.popleft()
            if u < min_node:
                min_node = u
            for v in adj[u]:
                if part[v] == -1:
                    part[v] = part[u] ^ 1
                    q.append(v)
                    comp_nodes.append(v)
                elif part[v] == part[u]:
                    print("NO")
                    return
        # decide orientation so that min_node gets rule 1
        if part[min_node] == 0:
            for v in comp_nodes:
                ans[v] = 1 if part[v] == 0 else 2
        else:
            for v in comp_nodes:
                ans[v] = 1 if part[v] == 1 else 2

    print("YES")
    print(' '.join(str(ans[i]) for i in range(1, n + 1)))

if __name__ == "__main__":
    solve()