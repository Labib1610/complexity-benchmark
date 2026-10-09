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

    colour = [-1] * (n + 1)          # -1 = unvisited, 0/1 = colour
    answer = [0] * (n + 1)           # final configuration (1 or 2)

    from collections import deque

    for start in range(1, n + 1):
        if colour[start] != -1:
            continue
        # BFS this component
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
                    print("NO")
                    return
        # decide orientation: smallest vertex gets 1
        min_v = min(comp)
        if colour[min_v] == 0:
            # colour 0 -> 1, colour 1 -> 2
            for v in comp:
                answer[v] = 1 if colour[v] == 0 else 2
        else:
            # swap
            for v in comp:
                answer[v] = 1 if colour[v] == 1 else 2

    # all good
    print("YES")
    print(' '.join(str(answer[i]) for i in range(1, n + 1)))

if __name__ == "__main__":
    solve()