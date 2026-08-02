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
        u = int(next(it)); v = int(next(it))
        adj[u].append(v)
        adj[v].append(u)

    color = [-1] * (n + 1)  # 0 or 1
    ans = [0] * (n + 1)
    for start in range(1, n + 1):
        if color[start] != -1:
            continue
        # BFS for component
        q = deque([start])
        color[start] = 0
        comp = [start]
        min_v = start
        bip = True
        while q:
            u = q.popleft()
            if u < min_v:
                min_v = u
            cu = color[u]
            for v in adj[u]:
                if color[v] == -1:
                    color[v] = 1 - cu
                    q.append(v)
                    comp.append(v)
                elif color[v] == cu:
                    bip = False
                    break
            if not bip:
                break
        if not bip:
            print("NO")
            return
        # decide orientation based on min_v's color
        if color[min_v] == 0:
            # original orientation
            for v in comp:
                ans[v] = 1 if color[v] == 0 else 2
        else:
            # flipped orientation
            for v in comp:
                ans[v] = 2 if color[v] == 0 else 1

    print("YES")
    print(' '.join(str(ans[i]) for i in range(1, n + 1)))

if __name__ == "__main__":
    solve()