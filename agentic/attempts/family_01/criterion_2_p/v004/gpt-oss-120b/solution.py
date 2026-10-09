import sys
from collections import deque

def solve() -> None:
    data = sys.stdin.buffer.read().split()
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

    colour = [-1] * n          # provisional 0/1
    answer = [0] * n           # final 1/2

    for start in range(n):
        if colour[start] != -1:
            continue
        # BFS for this component
        q = deque([start])
        colour[start] = 0
        comp = [start]
        while q:
            x = q.popleft()
            cx = colour[x]
            for y in adj[x]:
                if colour[y] == -1:
                    colour[y] = cx ^ 1
                    q.append(y)
                    comp.append(y)
                elif colour[y] == cx:
                    sys.stdout.write("NO")
                    return

        # orient component so that its smallest vertex gets colour 0
        min_v = min(comp)
        if colour[min_v] == 1:
            for v in comp:
                colour[v] ^= 1

        for v in comp:
            answer[v] = colour[v] + 1   # 0->1, 1->2

    out = ["YES", " ".join(map(str, answer))]
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()