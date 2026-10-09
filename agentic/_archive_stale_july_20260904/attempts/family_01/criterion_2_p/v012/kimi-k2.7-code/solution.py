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

    color = [0] * (n + 1)  # provisional colors 1/2
    answer = [0] * (n + 1)

    for start in range(1, n + 1):
        if color[start] != 0:
            continue
        q = deque([start])
        color[start] = 1
        comp = [start]
        bad = False
        while q:
            u = q.popleft()
            cu = color[u]
            for v in adj[u]:
                if color[v] == 0:
                    color[v] = 3 - cu
                    q.append(v)
                    comp.append(v)
                elif color[v] == cu:
                    bad = True
                    break
            if bad:
                break
        if bad:
            sys.stdout.write("NO")
            return

        minv = min(comp)
        if color[minv] == 1:
            for v in comp:
                answer[v] = color[v]
        else:
            for v in comp:
                answer[v] = 3 - color[v]

    out = ["YES", " ".join(str(answer[i]) for i in range(1, n + 1))]
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()