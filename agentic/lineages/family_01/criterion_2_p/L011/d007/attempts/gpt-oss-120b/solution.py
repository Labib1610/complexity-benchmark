import sys
from collections import deque

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u].append(v)
        adj[v].append(u)

    color = [-1] * n          # 0 or 1
    comp_nodes = []           # list of lists of nodes per component
    ok = True

    for i in range(n):
        if color[i] != -1:
            continue
        # BFS this component
        q = deque([i])
        color[i] = 0
        nodes = [i]
        while q:
            u = q.popleft()
            for v in adj[u]:
                if color[v] == -1:
                    color[v] = color[u] ^ 1
                    q.append(v)
                    nodes.append(v)
                elif color[v] == color[u]:
                    ok = False
                    break
            if not ok:
                break
        if not ok:
            break
        comp_nodes.append(nodes)

    if not ok:
        print("NO")
        return

    # Build answer with lexicographically smallest assignment
    ans = [0] * n
    for nodes in comp_nodes:
        # find smallest index in this component
        min_node = min(nodes)
        # orientation: make min_node have value 1
        if color[min_node] == 0:
            # map 0 -> 1, 1 -> 2
            for v in nodes:
                ans[v] = 1 if color[v] == 0 else 2
        else:
            # map 1 -> 1, 0 -> 2
            for v in nodes:
                ans[v] = 1 if color[v] == 1 else 2

    print("YES")
    print(' '.join(map(str, ans)))

if __name__ == "__main__":
    solve()