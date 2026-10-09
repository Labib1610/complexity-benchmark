import sys
sys.setrecursionlimit(1 << 25)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        if u == v:          # self‑loop -> impossible
            print("NO")
            return
        adj[u].append(v)
        adj[v].append(u)

    colour = [-1] * (n + 1)          # -1 = unvisited, 0 or 1 otherwise
    answer = [0] * (n + 1)

    from collections import deque

    for start in range(1, n + 1):
        if colour[start] != -1:
            continue
        # start a new component
        q = deque([start])
        colour[start] = 0
        comp = [start]
        bip = True
        while q:
            v = q.popleft()
            for to in adj[v]:
                if colour[to] == -1:
                    colour[to] = colour[v] ^ 1
                    q.append(to)
                    comp.append(to)
                elif colour[to] == colour[v]:
                    bip = False
        if not bip:
            print("NO")
            return

        # make the smallest index vertex have colour 0
        min_v = min(comp)
        if colour[min_v] == 1:
            for v in comp:
                colour[v] ^= 1

    for i in range(1, n + 1):
        answer[i] = 1 if colour[i] == 0 else 2

    print("YES")
    print(' '.join(str(answer[i]) for i in range(1, n + 1)))

if __name__ == "__main__":
    solve()