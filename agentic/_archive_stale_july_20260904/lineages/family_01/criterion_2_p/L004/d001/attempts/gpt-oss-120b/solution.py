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

    color_par = [-1] * (n + 1)          # parity 0/1 within component
    answer = [0] * (n + 1)              # final tier 1/2
    from collections import deque

    for start in range(1, n + 1):
        if color_par[start] != -1:
            continue
        # BFS this component
        q = deque([start])
        color_par[start] = 0
        comp_nodes = [start]
        bipartite = True
        while q:
            u = q.popleft()
            for v in adj[u]:
                if color_par[v] == -1:
                    color_par[v] = color_par[u] ^ 1
                    q.append(v)
                    comp_nodes.append(v)
                elif color_par[v] == color_par[u]:
                    bipartite = False
        if not bipartite:
            print("NO")
            return
        # decide orientation for lexicographically smallest assignment
        min_node = min(comp_nodes)
        flip = color_par[min_node]          # if 1, we swap colors
        for node in comp_nodes:
            answer[node] = 1 + (color_par[node] ^ flip)

    print("YES")
    print(' '.join(str(answer[i]) for i in range(1, n + 1)))

if __name__ == "__main__":
    solve()