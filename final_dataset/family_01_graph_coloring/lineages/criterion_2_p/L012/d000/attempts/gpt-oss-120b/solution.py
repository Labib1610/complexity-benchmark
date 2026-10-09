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

    colour = [-1] * (n + 1)          # 0 or 1, -1 = unvisited
    answer = [0] * (n + 1)          # final shifts (1 or 2)

    for start in range(1, n + 1):
        if colour[start] != -1:
            continue

        # BFS for this component
        q = deque([start])
        colour[start] = 0
        comp = [start]

        while q:
            u = q.popleft()
            cu = colour[u]
            for v in adj[u]:
                if colour[v] == -1:
                    colour[v] = cu ^ 1
                    q.append(v)
                    comp.append(v)
                elif colour[v] == cu:
                    # not bipartite
                    sys.stdout.write("NO")
                    return

        # orient component so that its smallest vertex gets shift 1
        vmin = min(comp)
        if colour[vmin] == 1:          # need to flip
            for v in comp:
                colour[v] ^= 1

        for v in comp:
            answer[v] = colour[v] + 1   # 1 or 2

    # all components processed successfully
    out = ["YES", " ".join(str(answer[i]) for i in range(1, n + 1))]
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()