import sys
sys.setrecursionlimit(1 << 25)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it)); m = int(next(it))
    adj = [[] for _ in range(n+1)]
    for _ in range(m):
        u = int(next(it)); v = int(next(it))
        adj[u].append(v)
        adj[v].append(u)

    color = [ -1 ] * (n+1)          # 0 or 1
    answer = [0] * (n+1)

    from collections import deque

    for start in range(1, n+1):
        if color[start] != -1:
            continue
        # BFS this component
        q = deque([start])
        color[start] = 0
        comp = [start]
        ok = True
        while q:
            u = q.popleft()
            for v in adj[u]:
                if color[v] == -1:
                    color[v] = color[u] ^ 1
                    q.append(v)
                    comp.append(v)
                elif color[v] == color[u]:
                    print("NO")
                    return
        # decide orientation for lexicographically smallest
        min_vertex = min(comp)
        # if min_vertex currently has parity 0, keep mapping 0->1,1->2
        # else swap
        if color[min_vertex] == 0:
            for v in comp:
                answer[v] = 1 if color[v] == 0 else 2
        else:
            for v in comp:
                answer[v] = 1 if color[v] == 1 else 2

    # isolated vertices (no edges) are already handled: they form a component of size 1,
    # min_vertex == that vertex, color = 0, so assigned 1.

    print("YES")
    print(' '.join(str(answer[i]) for i in range(1, n+1)))

if __name__ == "__main__":
    solve()