import sys
from collections import deque


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    m = int(input_data[1])
    k = int(input_data[2])

    head = [-1] * (n + 1)
    to = [0] * (2 * m)
    nxt = [0] * (2 * m)
    edge_cnt = 0

    idx = 3
    for _ in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx + 1])
        idx += 2

        to[edge_cnt] = v
        nxt[edge_cnt] = head[u]
        head[u] = edge_cnt
        edge_cnt += 1

        to[edge_cnt] = u
        nxt[edge_cnt] = head[v]
        head[v] = edge_cnt
        edge_cnt += 1

    visited = [False] * (n + 1)
    color = [-1] * (n + 1)
    chosen = []

    for i in range(1, n + 1):
        if not visited[i]:
            visited[i] = True
            color[i] = 0
            part0 = [i]
            part1 = []
            queue = deque([i])

            while queue:
                u = queue.popleft()
                c = color[u]
                e = head[u]
                while e != -1:
                    v = to[e]
                    if not visited[v]:
                        visited[v] = True
                        color[v] = 1 - c
                        if color[v] == 0:
                            part0.append(v)
                        else:
                            part1.append(v)
                        queue.append(v)
                    e = nxt[e]

            if len(part0) >= len(part1):
                chosen.extend(part0)
            else:
                chosen.extend(part1)

    if len(chosen) >= k:
        sys.stdout.write("YES\n")
        sys.stdout.write(" ".join(map(str, chosen[:k])) + "\n")
    else:
        sys.stdout.write("NO\n")


if __name__ == "__main__":
    solve()