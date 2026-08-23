import sys
from collections import deque

def solve():
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

    color = [-1] * (n + 1)
    q = deque()
    for i in range(1, n + 1):
        if color[i] != -1:
            continue
        color[i] = 0
        q.append(i)
        while q:
            u = q.popleft()
            cu = color[u]
            for w in adj[u]:
                if color[w] == -1:
                    color[w] = cu ^ 1
                    q.append(w)
                elif color[w] == cu:
                    sys.stdout.write("NO\n")
                    return

    out = ['YES']
    out.append(' '.join('1' if color[i] == 0 else '2' for i in range(1, n + 1)))
    sys.stdout.write('\n'.join(out))

if __name__ == '__main__':
    solve()