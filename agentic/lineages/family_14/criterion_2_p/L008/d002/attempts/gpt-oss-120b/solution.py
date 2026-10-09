import sys
from collections import deque

def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    it = iter(data)

    R = next(it)          # number of rooms (vertices)
    S = next(it)          # number of segments (edges) = R-1
    P = next(it)          # number of high‑priority rooms

    special = [False] * (R + 1)
    for _ in range(P):
        special[next(it)] = True

    adj = [[] for _ in range(R + 1)]
    total = 0
    for _ in range(S):
        u = next(it)
        v = next(it)
        w = next(it)
        adj[u].append((v, w))
        adj[v].append((u, w))
        total += w

    # If there is 0 or 1 special vertex, no edge is needed.
    if P <= 1:
        print(0)
        return

    degree = [0] * (R + 1)
    for v in range(1, R + 1):
        degree[v] = len(adj[v])

    q = deque()
    for v in range(1, R + 1):
        if degree[v] == 1 and not special[v]:
            q.append(v)

    while q:
        leaf = q.popleft()
        if degree[leaf] == 0:          # already removed earlier
            continue

        # find the still‑alive neighbour
        for nb, w in adj[leaf]:
            if degree[nb] > 0:
                neighbour = nb
                weight = w
                break
        else:
            continue  # should not happen

        total -= weight                # edge becomes unnecessary
        degree[leaf] = 0
        degree[neighbour] -= 1
        if degree[neighbour] == 1 and not special[neighbour]:
            q.append(neighbour)

    print(total)


if __name__ == "__main__":
    solve()