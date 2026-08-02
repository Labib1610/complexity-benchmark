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
    for start in range(1, n + 1):
        if color[start] != -1:
            continue
        q = deque([start])
        color[start] = 0
        comp = [start]
        while q:
            u = q.popleft()
            cu = color[u]
            for v in adj[u]:
                if color[v] == -1:
                    color[v] = cu ^ 1
                    q.append(v)
                    comp.append(v)
                elif color[v] == cu:
                    sys.stdout.write("NO")
                    return
        # ensure smallest node in component gets color 0
        minnode = min(comp)
        if color[minnode] == 1:
            for node in comp:
                color[node] ^= 1

    out = ["YES"]
    seq = [str(1 if color[i] == 0 else 2) for i in range(1, n + 1)]
    out.append(" ".join(seq))
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()