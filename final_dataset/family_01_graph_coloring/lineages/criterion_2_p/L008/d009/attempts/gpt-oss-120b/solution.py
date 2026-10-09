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
        u = int(next(it)); v = int(next(it))
        adj[u].append(v)
        adj[v].append(u)

    colour = [-1] * (n + 1)          # 0 / 1 bipartite colour
    answer = [0] * (n + 1)           # final c_i (1 or 2)

    from collections import deque

    for start in range(1, n + 1):
        if colour[start] != -1:
            continue
        # BFS this component
        q = deque([start])
        colour[start] = 0
        comp = [start]
        while q:
            v = q.popleft()
            for to in adj[v]:
                if colour[to] == -1:
                    colour[to] = colour[v] ^ 1
                    q.append(to)
                    comp.append(to)
                elif colour[to] == colour[v]:
                    print("NO")
                    return
        # decide orientation: smallest index gets c=1
        v0 = min(comp)
        flip = (colour[v0] == 1)   # if its colour is 1 we need to flip
        for v in comp:
            if flip:
                answer[v] = 1 if colour[v] == 1 else 2
            else:
                answer[v] = 1 if colour[v] == 0 else 2

    # output
    print("YES")
    print(' '.join(str(answer[i]) for i in range(1, n + 1)))

if __name__ == "__main__":
    solve()