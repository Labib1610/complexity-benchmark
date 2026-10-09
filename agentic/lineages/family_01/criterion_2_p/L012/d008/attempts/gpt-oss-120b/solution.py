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
        adj[v].append(u)          # constraint is symmetric: values must differ

    color = [-1] * (n + 1)        # 0 or 1
    from collections import deque
    for start in range(1, n + 1):
        if color[start] != -1:
            continue
        # BFS this component
        q = deque([start])
        color[start] = 0
        comp_nodes = [start]
        ok = True
        while q:
            u = q.popleft()
            for v in adj[u]:
                if color[v] == -1:
                    color[v] = color[u] ^ 1
                    q.append(v)
                    comp_nodes.append(v)
                elif color[v] == color[u]:
                    print("NO")
                    return
        # decide orientation to minimize lexicographic (base‑3) value
        min_node = min(comp_nodes)
        if color[min_node] == 1:          # would give value 2, swap whole component
            for node in comp_nodes:
                color[node] ^= 1

    # construct answer
    ans = [str(1 if color[i] == 0 else 2) for i in range(1, n + 1)]
    print("YES")
    print(' '.join(ans))

if __name__ == "__main__":
    solve()