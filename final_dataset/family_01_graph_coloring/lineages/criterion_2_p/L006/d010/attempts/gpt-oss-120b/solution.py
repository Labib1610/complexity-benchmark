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
        if u == v:
            print("NO")
            return
        adj[u].append(v)
        adj[v].append(u)

    color = [-1] * n          # 0 or 1
    answer = [0] * n
    visited = [False] * n

    from collections import deque

    for start in range(n):
        if visited[start]:
            continue
        # BFS this component
        q = deque([start])
        color[start] = 0
        visited[start] = True
        comp = [start]
        ok = True
        while q:
            u = q.popleft()
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    color[v] = 1 - color[u]
                    q.append(v)
                    comp.append(v)
                else:
                    if color[v] == color[u]:
                        print("NO")
                        return
        # decide orientation for lexicographically smallest
        comp.sort()
        # build two possible assignments for this component
        # option A: s = 1 + color
        # option B: s = 1 + (1 - color) = 2 - color
        better = None  # 0 for A, 1 for B
        for v in comp:
            a = 1 + color[v]
            b = 2 - color[v]
            if a < b:
                better = 0
                break
            if b < a:
                better = 1
                break
        if better is None:
            better = 0  # both equal (should not happen unless component empty)
        for v in comp:
            if better == 0:
                answer[v] = 1 + color[v]
            else:
                answer[v] = 2 - color[v]

    print("YES")
    print(' '.join(map(str, answer)))

if __name__ == "__main__":
    solve()