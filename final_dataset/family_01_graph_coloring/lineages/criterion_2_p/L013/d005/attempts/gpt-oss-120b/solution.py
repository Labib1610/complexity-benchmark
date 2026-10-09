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

    colour = [-1] * n          # -1 = unvisited, 0 or 1 otherwise
    for start in range(n):
        if colour[start] != -1:
            continue
        colour[start] = 0      # smallest vertex of component gets 0
        q = deque([start])
        while q:
            u = q.popleft()
            cu = colour[u]
            for w in adj[u]:
                if colour[w] == -1:
                    colour[w] = cu ^ 1
                    q.append(w)
                elif colour[w] == cu:
                    print("NO")
                    return

    # all good
    print("YES")
    out = [str(c + 1) for c in colour]
    print(' '.join(out))

if __name__ == "__main__":
    solve()