import sys
from collections import deque

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u].append(v)
        adj[v].append(u)

    color = [-1] * (n + 1)          # 0 or 1
    result = [0] * (n + 1)          # 1 or 2

    for start in range(1, n + 1):
        if color[start] != -1:
            continue
        # BFS
        queue = deque([start])
        color[start] = 0
        comp_nodes = [start]
        ok = True
        while queue:
            u = queue.popleft()
            cu = color[u]
            for v in adj[u]:
                if color[v] == -1:
                    color[v] = cu ^ 1
                    queue.append(v)
                    comp_nodes.append(v)
                elif color[v] == cu:
                    ok = False
                    break
            if not ok:
                break
        if not ok:
            print("NO")
            return
        # Determine orientation
        min_node = min(comp_nodes)
        if color[min_node] == 0:
            # keep
            for node in comp_nodes:
                result[node] = color[node] + 1
        else:
            for node in comp_nodes:
                result[node] = (color[node] ^ 1) + 1

    print("YES")
    sys.stdout.write(' '.join(str(result[i]) for i in range(1, n + 1)))

if __name__ == "__main__":
    solve()