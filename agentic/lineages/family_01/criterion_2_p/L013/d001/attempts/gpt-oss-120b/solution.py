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

    colour = [-1] * (n + 1)          # temporary 0/1
    answer = [0] * (n + 1)

    for start in range(1, n + 1):
        if colour[start] != -1:
            continue
        # BFS of a new component
        q = deque([start])
        colour[start] = 0
        comp = []
        min_vertex = start
        while q:
            x = q.popleft()
            comp.append(x)
            if x < min_vertex:
                min_vertex = x
            cx = colour[x]
            for y in adj[x]:
                if colour[y] == -1:
                    colour[y] = cx ^ 1
                    q.append(y)
                elif colour[y] == cx:
                    sys.stdout.write("NO")
                    return
        # orient so that min_vertex gets colour 0 (=> final 1)
        if colour[min_vertex] == 1:
            for v in comp:
                colour[v] ^= 1
        for v in comp:
            answer[v] = 1 if colour[v] == 0 else 2

    out = ["YES", " ".join(str(answer[i]) for i in range(1, n + 1))]
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()