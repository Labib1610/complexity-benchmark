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

    colour = [0] * (n + 1)          # final answer, 0 = unassigned, else 1 or 2
    temp = [ -1 ] * (n + 1)         # temporary 0/1 during BFS
    from collections import deque

    for start in range(1, n + 1):
        if colour[start]:
            continue
        # BFS this component
        q = deque([start])
        temp[start] = 0
        comp = [start]
        ok = True
        while q:
            v = q.popleft()
            for to in adj[v]:
                if temp[to] == -1:
                    temp[to] = temp[v] ^ 1
                    q.append(to)
                    comp.append(to)
                elif temp[to] == temp[v]:
                    print("NO")
                    return
        # decide orientation so that start gets colour 1
        if temp[start] == 0:
            map0, map1 = 1, 2
        else:
            map0, map1 = 2, 1
        for v in comp:
            colour[v] = map0 if temp[v] == 0 else map1
            temp[v] = -1          # reset for possible future use (not needed)

    # all done
    print("YES")
    print(' '.join(str(colour[i]) for i in range(1, n + 1)))

if __name__ == "__main__":
    solve()