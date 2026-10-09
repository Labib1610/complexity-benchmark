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

    color = [-1] * (n + 1)          # 0 or 1
    comp_nodes = []                # list of lists of nodes per component
    ok = True

    from collections import deque
    for start in range(1, n + 1):
        if color[start] != -1:
            continue
        # BFS this component
        q = deque([start])
        color[start] = 0
        nodes = [start]
        while q:
            u = q.popleft()
            cu = color[u]
            for v in adj[u]:
                if color[v] == -1:
                    color[v] = cu ^ 1
                    q.append(v)
                    nodes.append(v)
                elif color[v] == cu:
                    ok = False
                    break
            if not ok:
                break
        if not ok:
            break
        comp_nodes.append(nodes)

    if not ok:
        print("NO")
        return

    # orient each component so that its smallest index gets color 0 (=> period 1)
    for nodes in comp_nodes:
        min_node = min(nodes)
        if color[min_node] == 1:          # need to flip
            for v in nodes:
                color[v] ^= 1

    # produce answer: color 0 -> 1, color 1 -> 2
    ans = [str(color[i] + 1) for i in range(1, n + 1)]
    print("YES")
    print(' '.join(ans))

if __name__ == "__main__":
    solve()