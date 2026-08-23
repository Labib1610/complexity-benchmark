import sys
from collections import deque

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

    color = [-1] * n  # -1 unvisited, 0 or 1 are colors
    for start in range(n):
        if color[start] != -1:
            continue
        # BFS this component
        q = deque([start])
        color[start] = 0
        comp = [start]
        while q:
            u = q.popleft()
            cu = color[u]
            for w in adj[u]:
                if color[w] == -1:
                    color[w] = cu ^ 1
                    comp.append(w)
                    q.append(w)
                elif color[w] == cu:
                    print("NO")
                    return
        # Ensure lexicographically smallest: smallest vertex gets color 0
        min_vertex = min(comp)
        if color[min_vertex] == 1:
            for v in comp:
                color[v] ^= 1

    # Build result
    shifts = [str(c + 1) for c in color]
    print("YES")
    print(' '.join(shifts))

if __name__ == "__main__":
    solve()