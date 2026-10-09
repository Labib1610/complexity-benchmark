import sys
from collections import deque

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

    visited = [False] * (n + 1)
    temp_col = [0] * (n + 1)          # 0 / 1 temporary colours
    answer = [0] * (n + 1)

    for start in range(1, n + 1):
        if visited[start]:
            continue
        # BFS this component
        q = deque([start])
        visited[start] = True
        temp_col[start] = 0
        comp = [start]
        while q:
            u = q.popleft()
            cu = temp_col[u]
            for w in adj[u]:
                if not visited[w]:
                    visited[w] = True
                    temp_col[w] = 1 - cu
                    q.append(w)
                    comp.append(w)
                elif temp_col[w] == cu:
                    print("NO")
                    return
        # decide orientation
        min_node = min(comp)
        if temp_col[min_node] == 0:
            for v in comp:
                answer[v] = 1 if temp_col[v] == 0 else 2
        else:
            for v in comp:
                answer[v] = 2 if temp_col[v] == 0 else 1

    print("YES")
    print(' '.join(str(answer[i]) for i in range(1, n + 1)))

if __name__ == "__main__":
    solve()