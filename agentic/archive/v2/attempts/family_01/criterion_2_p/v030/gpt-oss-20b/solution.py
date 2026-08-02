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

    color = [-1] * (n + 1)          # provisional 0/1
    ans = [0] * (n + 1)             # final 1/2
    comp_nodes = []

    for start in range(1, n + 1):
        if color[start] != -1:
            continue
        queue = deque([start])
        color[start] = 0
        nodes = [start]
        bip = True
        while queue:
            u = queue.popleft()
            for v in adj[u]:
                if color[v] == -1:
                    color[v] = color[u] ^ 1
                    queue.append(v)
                    nodes.append(v)
                elif color[v] == color[u]:
                    bip = False
                    break
            if not bip:
                break
        if not bip:
            print("NO")
            return
        # decide orientation
        min_node = min(nodes)
        if color[min_node] == 0:
            # 0->1, 1->2
            for v in nodes:
                ans[v] = color[v] + 1
        else:
            # flip: 1->1, 0->2
            for v in nodes:
                ans[v] = (color[v] ^ 1) + 1

    print("YES")
    print(' '.join(str(ans[i]) for i in range(1, n + 1)))

if __name__ == "__main__":
    solve()