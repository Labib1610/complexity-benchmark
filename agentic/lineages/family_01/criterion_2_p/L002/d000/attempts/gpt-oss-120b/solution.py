import sys
sys.setrecursionlimit(1 << 25)

def solve() -> None:
    data = sys.stdin.buffer.read().split()
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

    color = [-1] * (n + 1)          # 0 or 1
    result = [0] * (n + 1)          # final shift (1 or 2)

    from collections import deque

    for start in range(1, n + 1):
        if color[start] != -1:
            continue
        # BFS this component
        q = deque([start])
        color[start] = 0
        comp = [start]
        ok = True
        while q:
            u = q.popleft()
            cu = color[u]
            for v in adj[u]:
                if color[v] == -1:
                    color[v] = cu ^ 1
                    q.append(v)
                    comp.append(v)
                elif color[v] == cu:
                    print("NO")
                    return
        # ensure smallest index in component gets shift 1 (color 0)
        min_node = min(comp)
        if color[min_node] == 1:
            # flip whole component
            for v in comp:
                color[v] ^= 1
        # store result
        for v in comp:
            result[v] = color[v] + 1

    # all components processed without conflict
    print("YES")
    print(' '.join(str(result[i]) for i in range(1, n + 1)))

if __name__ == "__main__":
    solve()