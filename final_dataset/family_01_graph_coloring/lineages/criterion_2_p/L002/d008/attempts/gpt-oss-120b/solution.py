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

    colour = [-1] * (n + 1)          # -1 = unvisited, 0/1 = two colours

    for start in range(1, n + 1):
        if colour[start] != -1:
            continue
        # start is the smallest index of its component
        colour[start] = 0
        q = deque([start])
        while q:
            x = q.popleft()
            cx = colour[x]
            for y in adj[x]:
                if colour[y] == -1:
                    colour[y] = cx ^ 1
                    q.append(y)
                elif colour[y] == cx:
                    sys.stdout.write("NO")
                    return

    # successful colouring
    out = ['YES\n']
    phases = [str(colour[i] + 1) for i in range(1, n + 1)]
    out.append(' '.join(phases))
    sys.stdout.write('\n'.join(out))

if __name__ == "__main__":
    solve()