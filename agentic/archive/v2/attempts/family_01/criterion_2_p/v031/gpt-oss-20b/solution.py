import sys
from collections import deque

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u].append(v)
        adj[v].append(u)

    color = [-1] * (n + 1)  # 0 or 1, -1 unvisited
    for i in range(1, n + 1):
        if color[i] != -1:
            continue
        # BFS for this component
        q = deque([i])
        comp = [i]
        color[i] = 0
        ok = True
        while q:
            u = q.popleft()
            cu = color[u]
            for v in adj[u]:
                if color[v] == -1:
                    color[v] = cu ^ 1
                    comp.append(v)
                    q.append(v)
                elif color[v] == cu:
                    # conflict
                    print("NO")
                    return
        # ensure lexicographically smallest: min node gets color 0
        min_node = min(comp)
        if color[min_node] == 1:
            for v in comp:
                color[v] ^= 1

    # all components processed
    res = [str(c + 1) for c in color[1:]]
    print("YES")
    print(" ".join(res))

if __name__ == "__main__":
    solve()