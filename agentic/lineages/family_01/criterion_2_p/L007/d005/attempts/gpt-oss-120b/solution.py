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

    color_par = [ -1 ] * (n + 1)   # parity 0/1
    result = [0] * (n + 1)

    from collections import deque

    for start in range(1, n + 1):
        if color_par[start] != -1:
            continue
        # BFS this component
        q = deque([start])
        color_par[start] = 0
        comp_nodes = [start]
        min_node = start
        while q:
            u = q.popleft()
            if u < min_node:
                min_node = u
            for v in adj[u]:
                if color_par[v] == -1:
                    color_par[v] = color_par[u] ^ 1
                    q.append(v)
                    comp_nodes.append(v)
                elif color_par[v] == color_par[u]:
                    print("NO")
                    return
        # decide mapping to make min_node color 1
        flip = (color_par[min_node] == 1)  # if min_node parity is 1, we need to flip
        for v in comp_nodes:
            parity = color_par[v]
            if flip:
                parity ^= 1
            result[v] = parity + 1   # 0->1, 1->2

    # all components processed, graph bipartite
    print("YES")
    print(' '.join(str(result[i]) for i in range(1, n + 1)))

if __name__ == "__main__":
    solve()