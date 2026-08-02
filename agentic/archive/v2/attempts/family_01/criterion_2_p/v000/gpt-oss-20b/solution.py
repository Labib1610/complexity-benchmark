import sys
from collections import deque

def solve() -> None:
    data = sys.stdin.buffer.read().split()
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

    color = [-1] * n          # 0 or 1
    answer = [0] * n          # 1 or 2

    for start in range(n):
        if color[start] != -1:
            continue
        queue = deque([start])
        color[start] = 0
        comp_nodes = [start]
        bip = True
        while queue and bip:
            u = queue.popleft()
            cu = color[u]
            for v in adj[u]:
                if color[v] == -1:
                    color[v] = cu ^ 1
                    queue.append(v)
                    comp_nodes.append(v)
                elif color[v] == cu:
                    bip = False
                    break
        if not bip:
            sys.stdout.write("NO\n")
            return
        # determine orientation
        min_node = min(comp_nodes)
        if color[min_node] == 1:
            # swap colors in this component
            for node in comp_nodes:
                color[node] ^= 1
        # set shifts
        for node in comp_nodes:
            answer[node] = color[node] + 1

    sys.stdout.write("YES\n")
    sys.stdout.write(' '.join(map(str, answer)) + '\n')

if __name__ == "__main__":
    solve()