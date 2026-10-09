import sys
sys.setrecursionlimit(1 << 25)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u].append(v)
        adj[v].append(u)

    visited = [False] * n
    colour = [0] * n          # 0 / 1 inside component
    answer = [0] * n

    from collections import deque

    for start in range(n):
        if visited[start]:
            continue
        # BFS this component
        q = deque([start])
        visited[start] = True
        colour[start] = 0
        comp = [start]
        ok = True
        while q:
            v = q.popleft()
            cv = colour[v]
            for to in adj[v]:
                if not visited[to]:
                    visited[to] = True
                    colour[to] = cv ^ 1
                    q.append(to)
                    comp.append(to)
                else:
                    if colour[to] == cv:
                        ok = False
                        break
            if not ok:
                break
        if not ok:
            print("NO")
            return
        # decide mapping for this component
        s = min(comp)          # smallest index
        if colour[s] == 0:
            # colour 0 -> type 1, colour 1 -> type 2
            for v in comp:
                answer[v] = 1 if colour[v] == 0 else 2
        else:
            # swap
            for v in comp:
                answer[v] = 1 if colour[v] == 1 else 2

    # all components processed
    print("YES")
    print(' '.join(map(str, answer)))

if __name__ == "__main__":
    solve()