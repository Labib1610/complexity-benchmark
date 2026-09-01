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

    colour = [-1] * (n + 1)          # temporary 0/1
    answer = [0] * (n + 1)           # final 1/2

    for start in range(1, n + 1):
        if colour[start] != -1:
            continue
        # BFS this component
        q = deque([start])
        colour[start] = 0
        comp = []
        while q:
            x = q.popleft()
            comp.append(x)
            for y in adj[x]:
                if colour[y] == -1:
                    colour[y] = colour[x] ^ 1
                    q.append(y)
                elif colour[y] == colour[x]:
                    print("NO")
                    return
        # decide orientation: smallest index gets colour 1
        vmin = min(comp)
        if colour[vmin] == 0:
            for v in comp:
                answer[v] = 1 if colour[v] == 0 else 2
        else:
            for v in comp:
                answer[v] = 2 if colour[v] == 0 else 1

    # all good
    print("YES")
    sys.stdout.write(' '.join(str(answer[i]) for i in range(1, n + 1)))

if __name__ == "__main__":
    solve()