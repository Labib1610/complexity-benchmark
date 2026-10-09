import sys
from collections import deque

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    k = int(next(it))

    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(it)); v = int(next(it))
        adj[u].append(v)
        adj[v].append(u)

    colour = [-1] * (n + 1)
    answer = []

    for start in range(1, n + 1):
        if colour[start] != -1:
            continue
        q = deque([start])
        colour[start] = 0
        part = [[], []]          # part[0] and part[1]
        while q:
            v = q.popleft()
            part[colour[v]].append(v)
            for nb in adj[v]:
                if colour[nb] == -1:
                    colour[nb] = colour[v] ^ 1
                    q.append(nb)
        # add the larger colour class of this component
        if len(part[0]) >= len(part[1]):
            answer.extend(part[0])
        else:
            answer.extend(part[1])

    if len(answer) >= k:
        sys.stdout.write("YES\n")
        sys.stdout.write(" ".join(map(str, answer[:k])) + "\n")
    else:
        sys.stdout.write("NO\n")

if __name__ == "__main__":
    solve()