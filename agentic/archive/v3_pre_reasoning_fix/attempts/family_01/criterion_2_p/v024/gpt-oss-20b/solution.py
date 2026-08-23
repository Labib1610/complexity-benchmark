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
        if u == v:
            print("NO")
            return
        adj[u].append(v)
        adj[v].append(u)

    color = [0] * (n + 1)  # 0 uncolored, 1 or 2
    for start in range(1, n + 1):
        if color[start] != 0:
            continue
        # start new component, assign start color 1
        dq = deque([start])
        color[start] = 1
        while dq:
            u = dq.popleft()
            cu = color[u]
            for v in adj[u]:
                if color[v] == 0:
                    color[v] = 3 - cu  # opposite color
                    dq.append(v)
                elif color[v] == cu:
                    print("NO")
                    return

    # output
    print("YES")
    print(' '.join(str(color[i]) for i in range(1, n + 1)))

if __name__ == "__main__":
    solve()