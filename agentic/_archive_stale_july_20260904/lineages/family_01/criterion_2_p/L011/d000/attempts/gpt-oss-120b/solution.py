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

    colour = [-1] * (n + 1)          # -1 = unvisited, 0/1 = colour
    answer = [0] * (n + 1)

    for start in range(1, n + 1):
        if colour[start] != -1:
            continue
        # BFS this component
        q = deque([start])
        colour[start] = 0
        comp = [start]
        min_v = start
        while q:
            v = q.popleft()
            if v < min_v:
                min_v = v
            for to in adj[v]:
                if colour[to] == -1:
                    colour[to] = colour[v] ^ 1
                    q.append(to)
                    comp.append(to)
                elif colour[to] == colour[v]:
                    print("NO")
                    return
        # orient component so that min_v gets value 1 (colour 0)
        if colour[min_v] == 1:
            for v in comp:
                colour[v] ^= 1

    # build answer
    for i in range(1, n + 1):
        answer[i] = 1 + colour[i]   # colour 0 -> 1, colour 1 -> 2

    print("YES")
    print(' '.join(str(answer[i]) for i in range(1, n + 1)))

if __name__ == "__main__":
    solve()