import sys
from collections import deque

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    k = int(next(it))

    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u].append(v)
        adj[v].append(u)

    colour = [-1] * (n + 1)          # -1 = unvisited, 0/1 = colour
    answer = []                     # vertices of the larger colour class per component

    for start in range(1, n + 1):
        if colour[start] != -1:
            continue
        q = deque([start])
        colour[start] = 0
        part = [[], []]              # vertices of colour 0 and 1 in this component
        part[0].append(start)

        while q:
            v = q.popleft()
            cv = colour[v]
            for to in adj[v]:
                if colour[to] == -1:
                    colour[to] = cv ^ 1
                    part[colour[to]].append(to)
                    q.append(to)
                # the input guarantees bipartiteness, no conflict check needed

        # keep the larger colour class
        if len(part[0]) >= len(part[1]):
            answer.extend(part[0])
        else:
            answer.extend(part[1])

    if len(answer) < k:
        sys.stdout.write("NO\n")
    else:
        sys.stdout.write("YES\n")
        sys.stdout.write(' '.join(map(str, answer[:k])) + '\n')


if __name__ == "__main__":
    solve()