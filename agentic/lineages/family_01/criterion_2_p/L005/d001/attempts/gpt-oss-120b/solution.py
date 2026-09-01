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

    color = [ -1 ] * (n + 1)   # -1 unvisited, 0 -> state 1, 1 -> state 2
    from collections import deque

    for start in range(1, n + 1):
        if color[start] != -1:
            continue
        # start new component, assign 0 (state 1) to the smallest index vertex
        dq = deque([start])
        color[start] = 0
        while dq:
            u = dq.popleft()
            cu = color[u]
            for v in adj[u]:
                if color[v] == -1:
                    color[v] = cu ^ 1
                    dq.append(v)
                elif color[v] == cu:
                    print("NO")
                    return

    # all good
    print("YES")
    res = [str(1 if color[i] == 0 else 2) for i in range(1, n + 1)]
    print(' '.join(res))

if __name__ == "__main__":
    solve()