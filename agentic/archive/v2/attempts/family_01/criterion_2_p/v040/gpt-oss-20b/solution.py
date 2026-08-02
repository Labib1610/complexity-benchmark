import sys
from collections import deque

def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    it = iter(data)
    n = next(it)
    m = next(it)

    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = next(it)
        v = next(it)
        adj[u].append(v)
        adj[v].append(u)

    color = [-1] * (n + 1)   # 0 or 1
    res = [0] * (n + 1)

    for start in range(1, n + 1):
        if color[start] != -1:
            continue
        # BFS component
        q = deque([start])
        color[start] = 0
        comp_nodes = [start]
        while q:
            u = q.popleft()
            for v in adj[u]:
                if color[v] == -1:
                    color[v] = color[u] ^ 1
                    q.append(v)
                    comp_nodes.append(v)
                elif color[v] == color[u]:
                    # not bipartite
                    print("NO")
                    return
        # orient component so that smallest index gets 1
        min_node = min(comp_nodes)
        flip = 0
        if color[min_node] == 0:
            flip = 1
        for node in comp_nodes:
            res[node] = color[node] ^ flip  # 0->0 or 1, then +1 below

    # prepare output
    output = ['YES']
    output.append(' '.join(str(c + 1) for c in res[1:]))
    sys.stdout.write('\n'.join(output))

if __name__ == "__main__":
    solve()